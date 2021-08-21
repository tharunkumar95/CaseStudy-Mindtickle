import requests
import json
import csv

# search for movies in the web and get the response in json format
movie_name = input("Please enter a movie name, to see it's full details: ")
movie_response = requests.get('http://www.omdbapi.com/?apikey=926c06e4&t=' + movie_name)
json_data = json.loads(movie_response.text)

# open a csv file (movies.csv, in this case) for writing in the present working directory
csv_file = open('movies.csv', 'w')
csv_writer = csv.writer(csv_file)


# write the headers and values to the csv file
for header, value in json_data.items():
    csv_writer.writerow([header])
    csv_writer.writerow([value])

# closing the session
csv_file.close()

