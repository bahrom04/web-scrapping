from bs4 import BeautifulSoup
import requests

url = 'https://www.olx.uz/transport/legkovye-avtomobili/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

card_divs = soup.find_all('div', {'data-cy': True})

data_list = []

for card_div in card_divs:
    data_dict = {
        'id': card_div['id'],
        'title': card_div.find('h6', class_='css-16v5mdi er34gjf0').text,
        'price': card_div.find('p', {'data-testid': 'ad-price'}).text,
        'location_date': card_div.find('p', {'data-testid': 'location-date'}).text,
        'image_url': card_div.find('img')['src']
    }

    data_list.append(data_dict)


for data_dict in data_list:
    print(data_dict)





# import requests
# from bs4 import BeautifulSoup

# urls = [
#     "https://www.olx.uz/transport/legkovye-avtomobili/"
# ]

# data_list = []

# response = requests.get(urls)
# if response.status_code == 200:
#     html = response.text

#     # Parse the HTML content
#     soup = BeautifulSoup(html, 'html.parser')

#     # Extract data from the page and create a dictionary
#     data_dict = {
#         'id': soup.find('div', {'data-cy': 'l-card'})['id'],
#         'title': soup.find('h6', class_='css-16v5mdi er34gjf0').text,
#         'price': soup.find('p', {'data-testid': 'ad-price'}).text,
#         'location_date': soup.find('p', {'data-testid': 'location-date'}).text,
#         'image_url': soup.find('img')['src'],
#         'url': urls
#         # Add more fields as needed
#     }

#     # Append the dictionary to the list
#     data_list.append(data_dict)

# # Print or use the data_list as needed
# for data_dict in data_list:
#     print(data_dict)
