import unittest
from files import helper, generator

class GeneratorTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()



