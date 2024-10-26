import requests
import json

def get_user_input(prompt):
  """Prompts the user for input and validates it (optional)."""
  while True:
    user_input = input(prompt)
    # Add validation here if needed (e.g., check phone number format)
    return user_input

if __name__ == "__main__":
  url = "https://truecaller4.p.rapidapi.com/api/v1/getDetailsBulk"

  # Get user input for either countryCode or phoneNumber
  country_or_phone_choice = input("Enter 'c' for country code or 'p' for phone number: ")
  if country_or_phone_choice.lower() == 'c':
    country_code = get_user_input("Enter country code (e.g., IN): ")
    phone_number = ""  # Set phone number to empty string if country code is chosen
  elif country_or_phone_choice.lower() == 'p':
    phone_number = get_user_input("Enter phone number (including country code): ")
    country_code = "IN"  # Set country code to empty string if phone number is chosen
  else:
    print("Invalid choice. Please enter 'c' or 'p'.")
    exit()

  querystring = {"phoneNumbers": "1",  # Assuming you only want details for one number
                 "countryCode": country_code,
                 "phoneNumber": phone_number}

  headers = {
      "x-rapidapi-key": "d794df38bdmshce76243e0dc0a0fp1ec171jsn94d601374XXX",  # Replace with your actual API key (avoid sharing publicly)
      "x-rapidapi-host": "truecaller4.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)

  if response.status_code == 200:
    data = response.json()

    # Choose a descriptive filename to avoid overwriting existing files
    filename = f"number-json/{country_code}_{phone_number}.json"

    with open(filename, 'w', encoding='utf-8') as outfile:
      json.dump(data, outfile, indent=4)  # Pretty-print JSON for readability
      print(f"API response saved to: {filename}")
  else:
    print(f"Error retrieving data: {response.status_code}")
