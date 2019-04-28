"""
This file is a basic script that takes the CSV format presented as the following:

Ran off on da Plug Twice, Plies, 153878.641, [{"line":"Fuck a shooter I'm my own shooter","milliseconds":"12660","lrc_timestamp":"[00:12.66]"},{"line":"All this ice I'm my own jeweler","milliseconds":"15830","lrc_timestamp":"[00:15.83]"},{"line":"Six lawyers and they all Jewish","milliseconds":"18430","lrc_timestamp":"[00:18.43]"}.......]

and transform it into a json file for uploading

Considerations:
the line
"""
import json

import pandas as pd




def open_and_read(filepath):
    # Open the files as csv_file variable
    data_df =pd.read_csv(filepath)
def clean(data):
    data = list(data)
    for pos,char in enumerate(data):
        if data[pos -1] == '"' and char == '"' or data[pos -1] == '"' and char == '[' or data[pos -1] == '"' and char == ']' :
            del data[pos -1]
        if  data[pos -1] == ']' and char == '"':
            del data[pos]   
            
        
    data =  ''.join(data)
    data = data.strip("").strip("'")
    # print(data)
    return data
def get_lyric_and_indices(str):
    starts = []
    stops = []
    lyrics_list = []
    
    for i in range(len(cleaned_file)):
        if cleaned_file[i-1] == ',' and cleaned_file[i] == '[':
            # print(i)
            starts.append(i) 
        if cleaned_file[i-1] == '}' and cleaned_file[i]== ']':
            stops.append(i+1)
            # print(i) 

    for i in range(len(stops)):
        lyrics_list.append(cleaned_file[starts[i]:stops[i]].strip())

    # print('{} {}'.format(len(starts), len(stops)))
    lyrics_list = [eval(x) for x in lyrics_list]

    return(starts,stops,lyrics_list)

def jsonify(cleaned_file):
    clean_dict = {}
    # print(cleaned_file)
    (get_lyric_and_indices(cleaned_file))
    # print(beginnings)


    # print({'title': top_half.split(',')[0], 'artist': top_half.split(',')[1], 'duration':top_half.split(',')[2]})
    
    

# 4-6


# def load(data):
#     pass


if __name__ == "__main__":
    # file_loaded = open_and_read('./DataSet.csv')
    print(pd.read_csv('./DataSet.csv'))
    # cleaned_file = clean(file_loaded)
    # jsonify(cleaned_file)
    