
import csv

# with open('mycsv.csv', 'w', newline='') as f:
#     thewriter = csv.Writer(f)
#
#     thewriter.writerow(['col1', 'col2', 'col3'])
#     thewriter.writerow(['one', 'two', 'three'])

with open('mycsvDic.csv', 'w', newline='') as f:
    fields = ['column1', 'column2', 'column3']
    thewriter = csv.DictWriter(f, fieldnames=fields)

    thewriter.writeheader()

    thewriter.writerow({'column1':'one', 'column2':'two', 'column3':'three'})