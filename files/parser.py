from files import helper


def get_indices(offset_list):
    lastpos = int(offset_list[0])
    index_list = [(0, lastpos)]
    for i in range(1, len(offset_list)):
        offset = int(offset_list[i])
        index_list.append((lastpos, lastpos + offset))
        lastpos += offset
    return index_list


def parse_line(line, index_list):
    return [line[pos[0]:pos[1]].rstrip() for pos in index_list]


def extract_line_from_string(index, line_size, content):
    stpos = index * line_size
    endpos = stpos + line_size
    return content[stpos:endpos]


# extract values
def parse_file(defaults, spec, num_lines, meta_data, is_save=True):
    if meta_data['file_size'] > 2e+9: # Dont process file sizes over 2GB
        print("File size too big to process")
    else:
        print("Parsing the file ...")
        prime_list = list()
        content = helper.read_text_file(file_path=defaults['data_file_path'], encoding=spec['FixedWidthEncoding'])
        index_list = get_indices(spec['Offsets']) # offset indices of cells in a row
        for i in range(0, num_lines):
            line = extract_line_from_string(index=i, line_size=meta_data['line_size'], content=content)
            row = parse_line(line, index_list)
            prime_list.append(row)
        print("Finished parsing the file\n")
        print("First ten rows of the file")
        print(prime_list[0:11])
        if is_save:
            helper.save_as_csv(data=prime_list, file_path = defaults['output_file_path'], encoding=spec['DelimitedEncoding'])
            print('csv file saved')


