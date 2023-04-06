import urllib
import csv

def retrieve_data(url, fname):
    """
    Retrieve a file from the specified url and save it in a local file 
    called fname.
    """
    
    # grab the data and parse it
    filedata = urllib.request.urlopen(url) 
    to_write = filedata.read()
    
    # write to file
    with open(fname, "wb") as f:
        f.write(to_write)

        
def read_data(path):
    """
    read downloaded data from a .csv file, and return a list of tuples. 
    each tuple represents a link between states.
    Args:
        path: string (Path of the file in which data is present)
    Returns:
        data: list of tuples which represents the data
    """
    with open(path, "r", encoding='utf8') as f:
        reader = csv.reader(f)
        return [(row[0], row[1]) for row in list(reader)]

def describe(data, n):
    row = data[n]
    return "Element {} of the Hamilton data set is {}. This means that {} mentions {} in a song.".format(n, row, row[0].capitalize(), row[1].capitalize())


def data_to_dictionary(data):
def data_to_dictionary(data):
    convert = {}
    for item in data:
        if item[0] in convert:
            convert[item[0]].append(item[1])
        else:
            convert[item[0]]=[item[1]]
    return dict(convert)
