#Package import
import csv
import pymongo
import sys


'''Fuction'''
#import csv file
def load_csv(filename):
    data_set=[]
    with open(filename) as file:
        reader=csv.DictReader(file)
        for line in reader:
            data_set.append(dict(line))
    return data_set

#Insert documents into MongoDB
def import_to_db(data_array,collection):
    for row in data_array:
            collection.insert_one(row)
            print(row)

#Display the inserted data
def show_inserted(reader):
    for row in reader:
        dict_row = dict(row)
        print(dict_row)
#Main
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        # Connect to MongoDB
        conn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = conn[sys.argv[1]]
        collection = db[sys.argv[2]]

        file_path = sys.argv[3]

        document_array = load_csv(file_path)
        import_to_db(document_array, collection)

        print("----------- Data Load is done ------------")


    except IOError:
        print("Cannot find the file")
    except pymongo.errors.ConfigurationError:
        print("Something is incorrectly configured")
    except pymongo.errors.ConnectionFailure:
        print("Connection fails")
    except :
        print("Unexpected error")


'''Main execution'''
if __name__=="__main__":
    sys.exit(main())

# cursor=collection.find()
# for data in cursor:
#     print(data)
