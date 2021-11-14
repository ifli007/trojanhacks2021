import requests
import json

def genre(genreName):
    url = "https://unogs-unogs-v1.p.rapidapi.com/api.cgi"

    querystring = {"t":"genres"}

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': "12c015ea2emsh468e55f49ef1dd9p17b899jsn1a848f446dda"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    genre = response.json()

    with open('data.txt', 'w') as outfile:
        json.dump(genre, outfile)

    print(type(genre[genreName]))
    print(genre[0][genreName])

def movies(genre_id, ):
    import requests

    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q":"get:new7-!1900,2021-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!{downloadable}","t":"ns","cl":"all","st":"adv","ob":"Relevance","p":"1","sa":"and"}

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': "12c015ea2emsh468e55f49ef1dd9p17b899jsn1a848f446dda"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
if __name__ == "__main__":
