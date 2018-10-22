import pandas as pd
import argparse
import os


parser = argparse.ArgumentParser()

#-db DATABASE -c Collection Name -f imported file
#parser.add_argument("-host", "--hostname", dest = "hostname", default = "xyz.edu", help="Server name")
parser.add_argument("-db", "--database", dest = "db", default = "data_loader", help="Database name")
parser.add_argument("-c", "--collection",dest ="collection", help="Collection name")
parser.add_argument("-f", "--file",dest ="file", help="File name")

args = parser.parse_args()

def convert_excel_csv(file):
    xls_sig = b'\x09\x08\x10\x00\x00\x06\x05\x00'
    xlsx_sig = b'\x50\x4B\x05\06'
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    with open(file, 'rb') as f:
        # try:
            f.seek(512)       # Seek to the offset.
            bytes = f.read(8) # Capture the specified number of bytes.

            if bytes == xls_sig:
                df = pd.read_excel(args.file)  # sheetname is optional
                df.to_csv('/Users/hung_yilai/PycharmProjects/CSVTest/csv/%s.csv' % (filename), index=False)  # index=False prevents pandas to write row index
                print("file is xls")
                return '/Users/hung_yilai/PycharmProjects/CSVTest/csv/%s.csv' % (filename)
        #
            else:
                f.seek(-22,2)  # Seek to the offset.
                bytes = f.read(4)  # Capture the specified number of bytes.

                if bytes == xlsx_sig:
                    df = pd.read_excel(args.file)  # sheetname is optional
                    df.to_csv('/Users/hung_yilai/PycharmProjects/CSVTest/csv/%s.csv' % (filename),
                              index=False)  # index=False prevents pandas to write row index
                    print("file is xlsx")
                return '/Users/hung_yilai/PycharmProjects/CSVTest/csv/%s.csv' % (filename)


convert_excel_csv(args.file)


# # oneliner
# pd.read_excel('my_file', sheetname='my_sheet_name').to_csv('output_file_name', index=False)