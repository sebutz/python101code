import csv

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj) # get a reader object from the file object
    # the reader object allows iteration
    for row in reader:
        print(" ".join(row)) # each row is a list of words (commas are not taken into consideration)
    
    
if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2014-02-26.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)