
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tkinter import *

headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likGecko) Chrome/51.0.2704.64 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'}

def scrape_hotel_data(city, checkIn, checkOut, order):
    url = f'https://www.booking.com/searchresults.html?ss={city}&checkin={checkIn}&checkout={checkOut}'
    # Make a GET request to the provided URL
    response = requests.get(url,headers=headers)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all hotel elements on the page
    hotel_elements = soup.findAll('div', {'data-testid' : 'property-card'})
    print(len(hotel_elements))
    # List to store hotel data dictionaries
    hotels_data = []

    # Iterate over each hotel element
    for hotel_elem in hotel_elements:
        # Dictionary to store data of current hotel
        hotel_data = {}

        # Extract hotel name
        hotel_name_elem = hotel_elem.find('div', {'data-testid' : 'title'})
        hotel_data['name'] = hotel_name_elem.text.strip() if hotel_name_elem else 'NOT GIVEN'

        # Extract hotel rating
        hotel_rating_elem = hotel_elem.find('div', class_='a3b8729ab1 d86cee9b25')
        hotel_data['rating'] = hotel_rating_elem.text.strip()[10:] if hotel_rating_elem else 'NOT GIVEN'

        # Extract hotel location
        hotel_location_elem = hotel_elem.find('span', class_='aee5343fdb def9bc142a')
        hotel_data['location'] = hotel_location_elem.text.strip() if hotel_location_elem else 'NOT GIVEN'
        # Extract hotel location
        hotel_location_elem = hotel_elem.find('span', {'data-testid': 'distance'})
        hotel_data['distance'] = hotel_location_elem.text.strip() if hotel_location_elem else 'NOT GIVEN'

        # Extract hotel price
        hotel_price_elem = hotel_elem.find('span', attrs={'data-testid':"price-and-discounted-price"})
        a = hotel_price_elem.text.strip()
        hotel_data['price'] = a if a else 'NOT GIVEN'

        # Extract hotel confort
        hotel_location_elem = hotel_elem.find('span', class_='a3332d346a')
        hotel_data['comfort'] = hotel_location_elem.text.strip()[8:] if hotel_location_elem else '-'


        # Append hotel data to list
        hotels_data.append(hotel_data)

    return sorted(hotels_data, key=lambda a: a[order], reverse=True)

# hotels = pd.DataFrame(assd)
# hotels.head()
# hotels.to_csv('test_hotels.csv', header=True, index=False)