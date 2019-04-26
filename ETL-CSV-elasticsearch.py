"""
This file is a basic script that takes the CSV format presented as the following:

Ran off on da Plug Twice, Plies, 153878.641, [{"line":"Fuck a shooter I'm my own shooter","milliseconds":"12660","lrc_timestamp":"[00:12.66]"},{"line":"All this ice I'm my own jeweler","milliseconds":"15830","lrc_timestamp":"[00:15.83]"},{"line":"Six lawyers and they all Jewish","milliseconds":"18430","lrc_timestamp":"[00:18.43]"}.......]

and transform it into a json file for uploading

Considerations:
the line
"""
import json

import pandas as pd
def open_and_read(filename):
    # Open the files as csv_file variable
    with open(filename) as csv_file:

        data_from_file = csv_file.readlines()[1]
        data_from_file = list(data_from_file)
        return data_from_file
def clean(data):
    for pos,word in enumerate(data):
        if data[pos -1] == '"' and word == '"' or data[pos -1] == '"' and word == '[' or data[pos -1] == '"' and word == ']' :
            del data[pos -1]
        if  data[pos -1] == ']' and word == '"':
            del data[pos]    
        
    data =  ''.join(data)
    data = data.strip("").strip("'")
    return data
def get_lyric_and_indices(str):
    start = 0
    stop = 0
    for i in range(len(cleaned_file)):
        if cleaned_file[i-1] == ',' and cleaned_file[i] == '[':
            start = i 
        if cleaned_file[i-1] == '}' and cleaned_file[i]== ']':
            stop = i+1
    str_lyrics= cleaned_file[start:stop]
    return(start,stop,eval(str_lyrics))
    
def jsonify(cleaned_file):
    clean_dict = {}
    # print(cleaned_file)
    begin,end,lyrics =(get_lyric_and_indices(cleaned_file))

    # print(''.join(str_lyrics))
    

# 4-6


# def load(data):
#     pass


if __name__ == "__main__":
    file_loaded = open_and_read('./DataSet.csv')
    cleaned_file = clean(file_loaded)
    jsonify(cleaned_file)
    