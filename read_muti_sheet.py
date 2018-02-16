import pyexcel
import json

book_dict = pyexcel.get_book_dict(file_name="bank.xlsx")
#isinstance(book_dict, OrderedDict)

for key, item in book_dict.items():
    print(json.dumps({key: item}))

print(book_dict["Sheet1"][0][0])
book_dict["Sheet1"][0][0] = "AAA"
#book_dict["Sheet3"][0][0] = "BBB"

pyexcel.save_book_as(bookdict = book_dict, dest_file_name="muti_sheet.xls")