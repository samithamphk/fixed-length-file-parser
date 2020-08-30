import json
import string
import random
from files import helper


def read_file_specification(path, is_print=True):
    spec_file = helper.read_json_file(path)
    if is_print:
        print(spec_file)
    return spec_file



def create_fixed_length_word(word, offset, filler, is_header=False):
    if is_header:
        fillpos = offset - len(word)  # fillpos is the number of places to fill for a cell
        if fillpos > 0:
            word += filler * fillpos
    else:
        ran_num = random.randint(1, offset)
        word = string.ascii_lowercase[0:ran_num]
        fillpos = offset - ran_num
        if fillpos > 0:
            word += filler * fillpos
    return word


def create_a_row(row_num, filler, spec):
    row_list = list()
    for col in range(0, len(spec['ColumnNames'])):
        word = ''
        offset = int(spec['Offsets'][col])
        if row_num == 0:  # create a word in header
            word = create_fixed_length_word(spec['ColumnNames'][col], offset, filler, True)
        else:  # create a word in a regular row
            word = create_fixed_length_word('', offset, filler)
        row_list.append(word)  # add cell to a row
    row = ''.join(row_list)
    return row


def generate_fixed_length_content(numlines, spec, filler=' '):
    out_list = list()  # list of lists as the primary data structure for the content
    for row_num in range(0, numlines + 1):
        row = create_a_row(row_num, filler, spec)
        out_list.insert(row_num, row)  # add row to the list of lists
    return out_list


def save_fixed_length_file(output_path, content, eol=None):
    with open(file=output_path, mode='w', encoding='windows-1252') as fwf:
        for line in content:
            fwf.write(line)
            if eol is not None:
                fwf.write(eol)  # usually '\n' for end of line




