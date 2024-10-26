import requests
import json

def get_website_url():
  """Prompts the user for a website URL and validates it."""
  while True:
    url = input("Enter a website URL (e.g., https://www.kali.org): ")
    if url.startswith("http") and "." in url:
      return url
    else:
      print("Invalid URL format. Please try again.")

def scrape_website_contacts(url, api_key):
  """Scrapes contacts from the provided website using RapidAPI."""
  base_url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"
  querystring = {
    "query": url,
    "match_email_domain": "false",  # Optional: set to "true" if you only want emails matching the domain
    "external_matching": "false"  # Optional: set to "true" for enhanced matching (may require a paid plan)
  }
  headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "website-contacts-scraper.p.rapidapi.com"
  }

  try:
    response = requests.get(base_url, headers=headers, params=querystring)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"An error occurred while scraping contacts: {e}")
    return None  # Or handle the error differently

def save_scraped_data(data, filename):
  """Saves the scraped data (contacts) to a JSON file."""
  try:
    with open(filename, 'w', encoding='utf-8') as outfile:
      json.dump(data, outfile, indent=4)  # Pretty-print JSON for readability
    print(f"Scraped contacts saved to: {filename}")
  except OSError as e:
    print(f"Error saving data: {e}")

if __name__ == "__main__":
  url = get_website_url()
  api_key = "990120e17dmsh4b3657040ff1ca1p1bd2aajsnb9f251758XXX"  # Replace with your actual API key

  scraped_data = scrape_website_contacts(url, api_key)

  if scraped_data:
    filename = f"site-json/{url.replace('https://', '').replace('http://', '')}.json"  # Generate descriptive filename
    save_scraped_data(scraped_data, filename)
  else:
    print("Error retrieving contact data (or API returned non-200 status code).")
