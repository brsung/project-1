
import requests
from bs4 import BeautifulSoup

# Ask the user to enter their website you want to scrape
url = input("Please enter the website you want to scrape: ")


# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(f"website found")
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #this part of the spesific place you want to go from is wrong
    # Find all article titles (example: <h2> tags with class 'title')
    title = soup.find_all('h2', class_='title')

    # Loop through the titles and print them
    for title in titles:
        print(title.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
