import pandas as pd
from flask import Flask, request, jsonify

# WIP!!! 
# this code returns html of dataframes based off which function is selected
# first time using flask please bare with me lol

search = Flask(__name__)

@search.route('/search', methods=['POST'])
def output():
    data = request.json
    option = data.get('option')
    # valid option values are: 'all', 'title', 'id', publisher', 'year', 'availability'
    # idea - frontend javascript should have buttons, properly labelled, and when clicked
    # sends a value to this python program
    # input should be prompted after option is selected
    match option:
            case 'all':
                result = search_all() 
                # no input
            case 'title':
                result = search_title(data.get('input')) 
                # input = title
            case 'id':
                result = search_id(data.get('input')) 
                # input = videogameid
            case 'publisher':
                result = search_publisher(data.get('input')) 
                # input = publisher
            case 'year':
                result = search_year(data.get('first_input'), data.get('second_input'))
                # input = start year (first_input) & end year (second_input)
            case 'available':
                result = search_available()
                # no input
        
    jsonify(result.to_html())

def search_all():
    return pd.read_csv('VideoGames.csv')

def search_title(title):
    df = pd.read_csv('VideoGames.csv')
    return df[df['Title'].str.contains(title, case=False, na=False)]

def search_id(id):
    df = pd.read_csv('VideoGames.csv')
    return df[(df['VideoGameID'] == id)]

def search_publisher(publisher):
    df = pd.read_csv('VideoGames.csv')
    return df[df['Publisher'].str.contains(publisher, case=False, na=False)]

def search_year(start_year, end_year):
    df = pd.read_csv('VideoGames.csv')
    return df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
 
def search_available():
    df = pd.read_csv('VideoGames.csv')
    return df[(df['Availability'] == 'Available')]
    