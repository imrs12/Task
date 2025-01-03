# 6 - Use the requests library to fetch data from a public API (e.g., JSONPlaceholder, Weather API, Quotes API). Parse and display specific information.

import requests  # pip install requests

def fetch_random_person_from_fakerapi():
    url = "https://fakerapi.it/api/v1/persons?_locale=en_US&_quantity=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        person = data['data'][0]
        print(f"Name: {person['firstname']} {person['lastname']}")
        print(f"Gender: {person['gender']}")
        print(f"Email: {person['email']}")
        print(f"Phone: {person['phone']}")
        print(f"Birthday: {person['birthday']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


fetch_random_person_from_fakerapi()