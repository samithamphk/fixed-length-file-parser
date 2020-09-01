import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from files import helper, generator, parser
import argparse


def get_arguments(def_numlines):
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number", required=True, help="Number of lines to be generated in the fixed length file")
    args = vars(ap.parse_args())
    if args['number'] == 0 or args["number"] is None:
        print("Number of records can not be empty!")
        print("Set number of records to 10 (default value)")
        args['number'] = def_numlines
    return int(args['number'])


if __name__ == "__main__":
    # Read the defaults
    defaults = helper.read_json_file('../static/app_defaults.json')

    # 1. Read the spec file
    spec = generator.read_file_specification(defaults['specification_file_path'], True)

    # 2. Generate the content
    num_lines = get_arguments(def_numlines=defaults['numlines'])
    output_text = generator.generate_fixed_length_content(numlines=num_lines, spec=spec)

    # 3. Save the file to disk
    generator.save_fixed_length_file(output_path=defaults['data_file_path'], content=output_text,
                                     encoding=spec['FixedWidthEncoding'], eol=None)

    # 4. Get the fixed length file meta data
    meta_data = helper.get_file_metadata(spec, defaults['data_file_path'])

    # 5. Parse the file, set is_save=False if no csv is required
    parser.parse_file(defaults, spec, num_lines, meta_data, is_save=True)
