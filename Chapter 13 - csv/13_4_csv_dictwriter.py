import csv

def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]  # first the column names, aka keys
    for values in data[1:]: # from 1 to the end
        inner_dict = dict(zip(fieldnames, values)) # make a dict
        my_list.append(inner_dict) # data is a list of maps

    print("final list",my_list)
    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)


'''
first_name,last_name,city
Tyrese,Hirthe,Strackeport
Jules,Dicki,Lake Nickolasville
Dedric,Medhurst,Stiedemannberg

'''