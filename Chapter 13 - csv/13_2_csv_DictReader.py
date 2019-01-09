import csv

'''
first_name,last_name,address,city,state,zip_code
Tyrese,Hirthe,1404 Turner Ville,Strackeport,NY,19106-8813
Jules,Dicki,2410 Estella Cape Suite 061,Lake Nickolasville,ME,00621-7435
Dedric,Medhurst,6912 Dayna Shoal,Stiedemannberg,SC,43259-2273
'''

# the first line has the columns name aka the keys
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',') # you can give the delimiter
    for line in reader:
        print("the line is:", line)
        print(line["first_name"]),
        print(line["last_name"])
        
if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)

'''
the line is: {'state': 'NY', 'zip_code': '19106-8813', 'city': 'Strackeport', 'last_name': 'Hirthe', 'address': '1404 Turner Ville', 'first_name': 'Tyrese'}
Tyrese
Hirthe
the line is: {'state': 'ME', 'zip_code': '00621-7435', 'city': 'Lake Nickolasville', 'last_name': 'Dicki', 'address': '2410 Estella Cape Suite 061', 'first_name': 'Jules'}
Jules
Dicki
the line is: {'state': 'SC', 'zip_code': '43259-2273', 'city': 'Stiedemannberg', 'last_name': 'Medhurst', 'address': '6912 Dayna Shoal', 'first_name': 'Dedric'}
Dedric
Medhurst
'''