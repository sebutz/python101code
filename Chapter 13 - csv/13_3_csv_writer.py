import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file: # open for writing
        writer = csv.writer(csv_file, delimiter=',') # delimiter
        for line in data:
            writer.writerow(line)  # write row after row
            
if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)

'''
first_name,last_name,city
Tyrese,Hirthe,Strackeport
Jules,Dicki,Lake Nickolasville
Dedric,Medhurst,Stiedemannberg
'''