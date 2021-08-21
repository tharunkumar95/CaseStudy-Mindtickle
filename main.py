import requests
import json
import csv

# search for movies in the web and get the response in json format
movie_name = 'Avengers'
movie_response = requests.get('http://www.omdbapi.com/?apikey=926c06e4&t=' + movie_name)
json_data = json.loads(movie_response.text)

# open a csv file (movies.csv, in this case) for writing in the present working directory
csv_data = csv.writer(open('movies.csv', 'w+', newline=''))

# write the headers and values to the csv file
for header, value in json_data.items():
    csv_data.writerow([header])
    csv_data.writerow([value])


