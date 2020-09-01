import unittest
from files import helper, generator, parser



#
# # 3. Save the file to disk
# generator.save_fixed_length_file(output_path=defaults['data_file_path'], content=output_text, eol=None)
#
# # 4. Get the fixed length file meta data
# meta_data = helper.get_file_metadata(spec, defaults['data_file_path'])
#
# # 5. Parse the file, set is_save=False if no csv is required
# parser.parse_file(defaults, spec, num_lines, meta_data, is_save=True)


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.defaults = helper.read_json_file('../static/app_defaults.json')
        self.spec = generator.read_file_specification(self.defaults['specification_file_path'], True)

    def tearDown(self):
        self.defaults=None
        self.spec=None

    def test_generate_content_size(self):
        num_lines = self.defaults['numlines']
        output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=self.spec)
        self.assertEqual(len(output_text)-1, num_lines)# minus 1 for header

    def test_generate_content_create_rows(self):
        num_lines = self.defaults['numlines']
        output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=self.spec)
        self.assertEqual(len(output_text) - 1, num_lines)  # minus 1 for header

    def test_parse_file(self):
        pass



if __name__ == '__main__':
    unittest.main()