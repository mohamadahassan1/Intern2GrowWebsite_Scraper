import requests
import json
from bs4 import BeautifulSoup

# Get the HTML of the website
response = requests.get('https://intern2grow.onrender.com/programs')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Get all of the programs on the website
programs = soup.find_all('div', class_='program-wrapper')

# Create a list to store the scraped data
scraped_data = []

# Iterate over the programs and scrape the data
for program in programs:
    program_name = program.find('h3').text
    program_description = program.find('p').text
    program_skills = program.find_all('span', class_='skill-wrapper')

    # Create a dictionary to store the program data
    program_data = {
        'name': program_name,
        'description': program_description,
        'skills': [skill.text for skill in program_skills]
    }

    # Add the program data to the scraped_data list
    scraped_data.append(program_data)

# Export the scraped data to a JSON file
with open('programs.json', 'w') as f:
    json.dump(scraped_data, f, indent=4)