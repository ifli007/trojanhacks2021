import requests
import pandas as pd
url = "https://unogsng.p.rapidapi.com/search"

headers = {
    'x-rapidapi-host': "unogsng.p.rapidapi.com",
    'x-rapidapi-key': "8601889d50mshf7c262565f897abp155216jsn44fcb7a5cc47"
    }

response = requests.request("GET", url, headers=headers)
x=response.text
with open('text.txt', 'w') as f:
    for line in x:
        f.write(line)

with open('text.txt') as f:
    lines = f.readlines()
    csv_file = open("testcsv.csv", "w")
    csv_file.write(''.join(lines))

csv_file.close()
