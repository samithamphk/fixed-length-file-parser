import unittest
from files import helper, generator


class GeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.defaults = helper.read_json_file('../static/app_defaults.json')
        self.spec = generator.read_file_specification(self.defaults['specification_file_path'], True)

    def tearDown(self):
        self.defaults = None
        self.spec = None

    def test_generate_content_size(self):
        num_lines = self.defaults['numlines']
        output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=self.spec)
        self.assertEqual(len(output_text) - 1, num_lines)  # minus 1 for header

    def test_generate_content_create_rows(self):
        num_lines = self.defaults['numlines']
        output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=self.spec)
        self.assertEqual(len(output_text) - 1, num_lines)  # minus 1 for header

    def test_create_a_data_row_len(self):
        row_number = 1
        row = generator.create_a_row(row_num=row_number, filler=' ', spec=self.spec)
        self.assertEqual(len(row), sum(map(int, self.spec["Offsets"])))

    def test_create_a_data_row_filler(self):
        row_number = 1
        row = generator.create_a_row(row_num=row_number, filler=' ', spec=self.spec)
        offsets = map(int, self.spec["Offsets"])

        t1 = offsets[0]
        t2 = sum(offsets[0:2])
        t3 = sum(offsets[0:3])
        t4 = sum(offsets[0:4])

        self.assertTrue(row[t1] == ' ' or row[t2] == ' ' or row[t3] == ' ' or row[4] == ' ')


if __name__ == '__main__':
    unittest.main()
