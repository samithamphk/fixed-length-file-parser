from files import helper


def get_indices(offset_list):
    """
    Create a list of tuples to define start, end positions fixed length words
    :param offset_list: list of offsets from the fixed length file specification
    :return:
    """
    last_pos = int(offset_list[0])
    index_list = [(0, last_pos)]
    for i in range(1, len(offset_list)):
        offset = int(offset_list[i])
        index_list.append((last_pos, last_pos + offset))
        last_pos += offset
    return index_list


def parse_line(line, index_list, filler=' '):
    """
    Extract words from a (string) line of a fixed length file
    :param filler:
    :param line:
    :param index_list: start, end positions of (offset) words in a line
    :return: string list
    """
    return [line[pos[0]:pos[1]].rstrip(filler) for pos in index_list]


def extract_line_from_string(index, line_size, content):
    """
    Extract line from the content (string).
    :param index: start position of a line in the content
    :param line_size: byte size of a single line
    :param content: string representation of fixed length file content
    :return:
    """
    stpos = index * line_size
    endpos = stpos + line_size
    return content[stpos:endpos]


def parse_file(defaults, spec, num_lines, meta_data, is_save=True):
    """
    Parse a fixed length file
    :param defaults: dictionary containing specification file path and i/o file paths
    :param spec: fixed length file specification dictionary
    :param num_lines: number of entries the fixed length file have
    :param meta_data: dictionary that specify fixed length file size and size of a line
    :param is_save: boolean to save the output as a csv
    """
    if meta_data['file_size'] > 2e+9: # Dont process file sizes over 2GB
        print("File size too big to process")
    else:
        print("Parsing the file ...")
        prime_list = list()
        content = helper.read_text_file(file_path=defaults['data_file_path'], encoding=spec['FixedWidthEncoding'])
        index_list = get_indices(spec['Offsets']) # offset indices of cells in a row
        for i in range(0, num_lines): # read line by line
            line = extract_line_from_string(index=i, line_size=meta_data['line_size'], content=content)
            row = parse_line(line, index_list) # list of words
            prime_list.append(row)
        print("Finished parsing the file\n")
        print("First ten rows of the file")
        print(prime_list[0:11])
        if is_save:
            helper.save_as_csv(data=prime_list, file_path = defaults['output_file_path'], encoding=spec['DelimitedEncoding'])
            print('csv file saved')


