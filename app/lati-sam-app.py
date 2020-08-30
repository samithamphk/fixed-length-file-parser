import os
from files import helper, generator, parser

# if __name__ == "main":
print("in main .....")
defaults = helper.read_json_file('../static/app_defaults.json')
print(defaults)

# 1. Read the spec file
spec = generator.read_file_specification(defaults['specification_file_path'], True)

# 2. Generate the content
num_lines = defaults['numlines']
output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=spec)

# 3. Save the file to disk
generator.save_fixed_length_file(output_path=defaults['data_file_path'], content=output_text, eol=None)


# 4. Get the fixed length file meta data
# file_size = os.stat(defaults['data_file_path']).st_size # in bytes
# line_size=sum(list(map(int,spec['Offsets']))) # in bytes
# numlines_check = file_size/line_size # This assumes '' as EOL
# print("num lines = ", numlines_check)
# if numlines_check == num_lines:
#     pass
# else:
#     print('This implementation does not support other EOL character')
meta_data = helper.get_file_metadata(spec, defaults['data_file_path'])
parser.parse_file(defaults, spec, num_lines, meta_data, is_save=True)