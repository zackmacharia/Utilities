import csv, argparse

def main():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('src_file', help='name of source csv file')
        parser.add_argument('new_file', help='name of new csv file')
        parser.add_argument('new_delimiter', help='enclose special characters such as a semi-colon in quotes')
        args = parser.parse_args()
        find_delimiter(args.src_file)
        parse_csv(args.src_file, args.new_file, args.new_delimiter)


def fieldname_data(src_file):
    """
        This function reads a csv file and returns the fieldnames
    """

    with open(src_file, 'r', newline='') as csvfile:
        fieldnames = next(csvfile)
        return fieldnames

def find_delimiter(src_file):
    """
        This function reads the fieldnames in a csv file and returns the delimiter
    """

    fieldname_string = fieldname_data(src_file).strip()

    for item in fieldname_string:
        if item.isalnum() is False:  # assumes fieldnames are in alphanumeric format
            find_delimiter = item
            break
    return find_delimiter

def fieldnames_list(src_file):
    """
        This functions takes a fieldname presented as a single string and splits it to individual text representing each colum.
        Example: 
        Input Data: ['Reading|Make|Model|Type|Value'] - returned from using DictReader fieldname method
        Output Data: ['Reading', 'Make', 'Model', 'Type', 'Value']
    """

    fieldname_string = fieldname_data(src_file).strip()
    delimiter = find_delimiter(src_file)
    fieldname_list = fieldname_string.split(delimiter)

    return fieldname_list
    
def parse_csv(src_file, new_file, new_delimiter):
    with open(src_file, 'r', newline='', encoding='utf-8') as ofile:

        fieldnames = fieldnames_list(src_file)
        reader = csv.DictReader(ofile, fieldnames=fieldnames, delimiter=find_delimiter(src_file))

        with open(new_file, 'w', newline='', encoding='utf-8') as nfile:
            writer = csv.DictWriter(nfile, fieldnames=fieldnames, delimiter=new_delimiter)

            for line in reader:
                writer.writerow(line)


main()