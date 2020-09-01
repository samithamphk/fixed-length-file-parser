import json
import string
import random
from files import helper


def read_file_specification(path, is_print=True):
    """
    Return a dictionary by reading a fixed length file specification in json.
    :param path:
    :param is_print: print out the contents if True
    :return:
    """
    spec_file = helper.read_json_file(path)
    if is_print:
        print(spec_file)
    return spec_file


def create_fixed_length_word(word, offset, filler, is_header=False):
    """
    Generate a fixed length word (for a given row,column) according to the offset limits.
    :param word: Column name from the file specification. '' otherwise
    :param offset: collumn offset from the specification
    :param filler: filling character for fixed length word. defaults to ' '
    :param is_header:
    :return: string
    """
    if is_header:
        fill_pos = offset - len(word)  # fill_pos is the number of places to fill for a cell
        if fill_pos > 0:
            word += filler * fill_pos  # create fixed length header word
    else:
        ran_num = random.randint(1, offset)  # 1<= random number <= offset
        word = string.ascii_lowercase[0:ran_num]  # extract the first ran_num long string from the alphabet
        fill_pos = offset - ran_num
        if fill_pos > 0:
            word += filler * fill_pos  # creates a fixed length word
    return word


def create_a_row(row_num, filler, spec):
    """
    Generate a fixed length string for a row in the fixed length file.
    :param row_num: 0 for the header, anything else is a data row
    :param filler: filler character
    :param spec: dictionary specifying fixed length file
    :return: fixed length string
    """
    row_list = list()  # list to hold the fixed length words in a row
    for col in range(0, len(spec['ColumnNames'])):
        word = ''
        offset = int(spec['Offsets'][col])  # read the offset value from the file specification
        if row_num == 0:  # create a word in header
            word = create_fixed_length_word(spec['ColumnNames'][col], offset, filler, True)
        else:  # create a word in a regular row
            word = create_fixed_length_word('', offset, filler)
        row_list.append(word)
    row = ''.join(row_list)  # create row string
    return row


def generate_fixed_length_content(numlines, spec, filler=' '):
    """
    Generate file content of given number or rows.
    :param numlines: user provided number to determine file size
    :param spec: fixed length file specification dictionary
    :param filler: filler character for content
    :return: list of list
    """
    out_list = list()  # list of lists as the primary data structure to hold the content
    for row_num in range(0, numlines + 1):
        row = create_a_row(row_num, filler, spec)
        out_list.insert(row_num, row)
    return out_list


def save_fixed_length_file(output_path, content, encoding, eol=None):
    """
    Write a fixed length file from the given content
    :param output_path:
    :param content: list of list
    :param encoding: defaults to windows-1252 from the file specification
    :param eol: defaults to ' '
    """
    with open(file=output_path, mode='w', encoding=encoding) as fwf:
        for line in content:
            fwf.write(line)
            if eol is not None:
                fwf.write(eol)
