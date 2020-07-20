from csv_parser.code.fix_csv import (fieldname_data, find_delimiter, fieldnames_list)

def test_fieldname_data(csv_test_file):

    expected_output = 'Reading|Make|Model|Type|Value'
    assert fieldname_data(csv_test_file) == expected_output

def test_find_delimiter(csv_test_file):

    expected_output = '|'
    assert find_delimiter(csv_test_file) == expected_output

def test_fieldnames_list(csv_test_file):

    expected_output = ['Reading', 'Make', 'Model', 'Type', 'Value']
    assert fieldnames_list(csv_test_file) == expected_output
