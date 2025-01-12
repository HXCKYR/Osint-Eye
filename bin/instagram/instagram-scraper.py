import requests
import json

def get_user_input():
  """Prompts the user for input and performs basic sanitization."""
  while True:
    user_input = input("Enter the INSTAGRAM id or user_name (avoid special characters): ")
    # Basic sanitization (remove potentially problematic characters)
    sanitized_input = user_input.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("|", "").replace("<", "").replace(">", "")
    return sanitized_input

if __name__ == "__main__":
  url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"
  user_input = get_user_input()
  querystring = {"username_or_id_or_url": user_input}

  headers = {
        "x-rapidapi-key": "990120e17dmsh4b3657040ff1ca1p1bd2aajsnb9f251758b32",  # Replace with your actual API key (avoid sharing publicly)
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)

  if response.status_code == 200:
    data = response.json()

    # Choose a descriptive filename to avoid overwriting existing files
    filename = f"instagram-json/{user_input}.json"

    with open(filename, 'w', encoding='utf-8') as outfile:
      json.dump(data, outfile, indent=4)  # Pretty-print JSON for readability
      print(f"API response saved to: {filename}")
  else:
    print(f"Error retrieving data: {response.status_code}")
