import json
import os
import csv


# json file reader
def read_json_file(path):
    with open(file=path, mode='r') as sf:
        json_file = json.load(sf)
        return json_file


# get file meta data
def get_file_metadata(spec, file_path):
    file_size = os.stat(file_path).st_size  # in bytes
    line_size = sum(list(map(int, spec['Offsets'])))  # in bytes
    return {'file_size': file_size, 'line_size': line_size}


def read_text_file(file_path, encoding):
    with open(file=file_path, mode='r', encoding=encoding) as fwf:
        content = fwf.read()
    return content


# save csv file
def save_as_csv(data, file_path, encoding, newline='\n'):
    with open(file=file_path, mode="w", encoding=encoding, newline=newline) as lilf:
        writer = csv.writer(lilf)
        writer.writerows(data)
