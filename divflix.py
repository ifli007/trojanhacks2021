import json
import requests

names = {
    '1' : ["African-American Comedies", "African-American Stand-up Comedy"],
    '2' : ["Asian Movies", "Asian Action Films", "Asian Programmes", "Southeast Asian Films"],
    '3' : ["Latin American Films", "Latin American TV Shows",
        "Latin American Comedies"],
    '4' : ["Gay & Lesbian Comedies", "Gay & Lesbian Documentaries",
        "Gay & Lesbian Dramas", "Gay and Lesbian Films"]
}
id = {
    '1' : [4906, 10778],
    '2' : [78104, 77232, 78103, 9196],
    '3' : [1613, 67708, 3996],
    '4' : [7120, 4720, 500, 5977]
}

def genre(genreName):

    with open('data.txt') as json_file:
        genre = json.load(json_file)

    pretty_genre = json.dumps(genre, indent = 2, sort_keys = True)

    #print(pretty_genre)
    for i in genre['ITEMS']:
        if genreName in i:
            return i[genreName]


def movies(genreId, n = 5):

    url = "https://unogsng.p.rapidapi.com/search"

    querystring = {"genrelist": str(genreId),
        "start_year":"1972","orderby":"rating",
    "audiosubtitle_andor":"or","limit": str(n),"subtitle":"english",
    "audio":"english","end_year":"2021"}

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': "12c015ea2emsh468e55f49ef1dd9p17b899jsn1a848f446dda"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

if __name__ == "__main__":

    print("Welcome to Divflix!\n\nLet's explore diversity on Netflix!")
    continu = True
    while(continu):

        print("1: African-American\n2: Asian-American\n3: Latinx")
        print("4: LGBTQ")

        choiceOne = input("Enter the number of your chosen category: ");

        print("\nWhich category/categories would you like to see?")

        for i in range(len(names[choiceOne])):
            print(str(i + 1) + ": " + str(names[choiceOne][i]))

        choiceTwo = input("Enter the numbers separated by spaces: ")
        choiceTwo = choiceTwo.split()

        array_data = []
        array_data.clear()

        for i in choiceTwo:
            array_data.append(movies(id[choiceOne][int(i) - 1]))

        for i in range(len(array_data)):
            print("")
            print(names[choiceOne][int(choiceTwo[i]) - 1] + ":")

            if(array_data[i]['total'] < 1):
                print("None available in that category :( ")
                continue

            for j in array_data[i]["results"]:
                print('')
                print("     Title: " + str(j['title']))
                print("     Year released: " + str(j['year']))

        #print(type(json_dict))

        #dict = json.load(json_dict)
        #print(json_dict)

        ans = input("Explore more? y/n: ")

        if(ans != 'Y' and ans != 'y'):
            continu = False;
