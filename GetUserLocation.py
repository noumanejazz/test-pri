import requests

def get_location()
    try:
        response = requests.get('https://api.ipgeolocation.io/api/ipgeo?apiKey=YOUR_API_KEY')
        data = response.json()
        return data['country_name']
    except Exception as e:
        return f'Error: {str(e)}'

print(get_location())