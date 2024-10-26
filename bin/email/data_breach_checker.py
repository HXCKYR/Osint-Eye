import requests
import json

def get_email_input():
  """Prompts the user for their email address and returns it."""
  while True:
    email = input("Enter your email address: ")
    if "@" in email and "." in email:
      return email
    else:
      print("Invalid email format. Please try again.")

def check_data_breach(email, api_key):
  """Checks the provided email for data breaches using the RapidAPI."""
  url = "https://data-breach-checker.p.rapidapi.com/api/breach"
  querystring = {"email": email}
  headers = {
      "x-rapidapi-key": api_key,
      "x-rapidapi-host": "data-breach-checker.p.rapidapi.com"
  }

  try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return None  # Or handle the error differently

if __name__ == "__main__":
  email = get_email_input()
  api_key = "d794df38bdmshce76243e0dc0a0fp1ec171jsn94d601374XXX"  # Replace with your actual API key
  data = check_data_breach(email, api_key)

  if data:
    # Choose a descriptive filename to avoid overwriting existing files
    filename = f"email-json/{email}.json"

    try:
      with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)  # Pretty-print JSON for readability
        print(f"API response saved to: {filename}")
    except OSError as e:
      print(f"Error saving data: {e}")
  else:
      print(f"Error retrieving data (or API returned non-200 status code).")
