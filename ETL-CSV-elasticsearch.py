"""
This file is a basic script that takes the CSV format presented as the following:

Ran off on da Plug Twice, Plies, 153878.641, [{"line":"Fuck a shooter I'm my own shooter","milliseconds":"12660","lrc_timestamp":"[00:12.66]"},{"line":"All this ice I'm my own jeweler","milliseconds":"15830","lrc_timestamp":"[00:15.83]"},{"line":"Six lawyers and they all Jewish","milliseconds":"18430","lrc_timestamp":"[00:18.43]"}.......]

and transform it into a json file for uploading

Considerations:
the line
"""
import json


def open_and_read(filename):
    # Open the files as csv_file variable
    song_dict = []
    with open(filename) as csv_file:

        data_from_file = csv_file.readlines()[1]
        data_from_file = list(data_from_file)
        return data_from_file
def clean(data):
    for pos,word in enumerate(data):
        # print('hit')
        if data[pos -1] == '"' and word == '"' or data[pos -1] == '"' and word == '[' or data[pos -1] == '"' and word == ']':
            del data[pos -1]
        if  data[pos -1] == ']' and word == '"':
            print('hit')
            del data[pos]    
        
    return ''.join(data)



def 


if __name__ == "__main__":
    file_loaded = open_and_read('./DataSet.csv')
    cleaned_file = clean(file_loaded)