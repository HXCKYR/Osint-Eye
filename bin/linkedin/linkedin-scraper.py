import requests
import json


def get_user_input():
  """Prompts the user for a LinkedIn profile URL."""
  while True:
    user_input = input("Enter a LinkedIn profile URL: ")
    # Basic validation (check if the URL starts with "https://www.linkedin.com/in/")
    if user_input.startswith("https://www.linkedin.com/in/"):
      return user_input
    else:
      print("Invalid URL. Please enter a valid LinkedIn profile URL.")


if __name__ == "__main__":
  url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
  linkedin_url = get_user_input()  # Get user input
  querystring = {
      "linkedin_url": linkedin_url,
      "include_skills": "false",
      "include_certifications": "false",
      "include_publications": "false",
      "include_honors": "false",
      "include_volunteers": "false",
      "include_projects": "false",
      "include_patents": "false",
      "include_courses": "false",
      "include_organizations": "false",
      "include_company_public_url": "false"
  }
  headers = {
      "x-rapidapi-key": "d794df38bdmshce76243e0dc0a0fp1ec171jsn94d601374XXX",  # Replace with your actual API key (avoid sharing publicly)
      "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)

  # Check for successful response (status code 200)
  if response.status_code == 200:
      data = response.json()

      # Choose a descriptive filename based on the profile URL (optional)
      filename = f"linkedin-json/{linkedin_url.split('/')[-1]}.json"

      # Save the JSON data to a file
      with open(filename, 'w', encoding='utf-8') as outfile:
          json.dump(data, outfile, indent=4)  # Pretty-print JSON for readability
          print(f"API response saved to: {filename}")
  else:
      print(f"Error retrieving data: {response.status_code}")
