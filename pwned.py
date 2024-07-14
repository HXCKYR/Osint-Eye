import requests

url = "https://breachdirectory.p.rapidapi.com/"
user_input = input("Enter an EMAIL ADDRESS or USERNAME or DOMAIN : ")

querystring = {"func":"auto","term": user_input}

headers = {
        "x-rapidapi-key": "d794df38bdmshce76243e0dc0a0fp1ec171jsn94d6013742e1",
        "x-rapidapi-host": "breachdirectory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
