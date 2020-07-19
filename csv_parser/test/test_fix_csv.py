from csv_parser.code.fix_csv import fieldname_data

def test_fieldname_data():

    expected_data = 'Reading|Make|Model|Type|Value'
    assert fieldname_data('test_file.csv') == expected_data



