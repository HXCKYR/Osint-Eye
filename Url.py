import requests

url = "https://breachdirectory.p.rapidapi.com/"
user_input = input("Enter an EMAIL ADDRESS or USERNAME or DOMAIN : ")

querystring = {"func":"auto","term": user_input}

headers = {
        "x-rapidapi-key": "990120e17dmsh4b3657040ff1ca1p1bd2aajsnb9f251758b32",
        "x-rapidapi-host": "breachdirectory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
