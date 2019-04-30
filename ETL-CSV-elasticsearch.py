"""
This file is a basic script that takes the CSV format presented as the following:

Ran off on da Plug Twice, Plies, 153878.641, [{"line":"Fuck a shooter I'm my own shooter","milliseconds":"12660","lrc_timestamp":"[00:12.66]"},{"line":"All this ice I'm my own jeweler","milliseconds":"15830","lrc_timestamp":"[00:15.83]"},{"line":"Six lawyers and they all Jewish","milliseconds":"18430","lrc_timestamp":"[00:18.43]"}.......]

and transform it into a dataframe

Considerations:
the line
"""
import json

import pandas as pd



# Helper function
def strip_and_tokenize(string):
    string = string.split(' ')
    string = [re.sub('[^0-9a-zA-Z]+', '', s) for s in string]
    return ' '.join(string)

def cleaner(dataframe,results):
    just_lyrics = []
    lyric_info_list = dataframe['lrc'].to_list()
    # The lyrics are stored in a list that is encasulated in a string, so using an eval() statement
    # makes sense here if this is expected behavior
    lyric_info_list= [eval(lyric) for lyric in lyric_info_list]

    # Note that a list compresention with a function could have been used here 
    for lyrics in lyric_info_list:
       just_lyrics.append([lyric['line'] for lyric in lyrics])
    just_lyrics = [' '.join(lyrics).lower() for lyrics in just_lyrics]
    just_lyrics = [strip_and_tokenize(lyrics) for lyrics in just_lyrics]
    dataframe = dataframe.join(pd.DataFrame(results))
    dataframe = dataframe.join(pd.DataFrame(just_lyrics))
    dataframe.columns = ['title','artist', 'duration','lrc', 'anger', 'fear','joy', 'sadness', 'surprise', 'cleaned_lyrics']
    dataframe.drop(['lrc'], axis=1,inplace=True)
    return dataframe
# print(indicoio.emotion(just_lyrics,top_n='6'))


data = cleaner(data_df,results)

def loader(cleaned_dataframe):
    
    def gendata():
        for song in cleaned_dataframe:
            yield {
                "_index": "songs",
                "_type": "document",
                "doc": song,
            }
    
    
    
    helpers.bulk(es,gendata())