from files import helper, generator, parser

defaults = helper.read_json_file('../static/app_defaults.json')
print(defaults)

# 1. Read the spec file
spec = generator.read_file_specification(defaults['specification_file_path'], True)

# 2. Generate the content
num_lines = defaults['numlines']
output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=spec)

# 3. Save the file to disk
generator.save_fixed_length_file(output_path=defaults['data_file_path'], content=output_text, encoding=spec['FixedWidthEncoding'], eol=None)

# 4. Get the fixed length file meta data
meta_data = helper.get_file_metadata(spec, defaults['data_file_path'])

# 5. Parse the file, set is_save=False if no csv is required
parser.parse_file(defaults, spec, num_lines, meta_data, is_save=True)
