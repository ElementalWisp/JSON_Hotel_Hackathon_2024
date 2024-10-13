'''
Hackathon 2024
Developed by Anthony Jackson and Amy Phan
'''

import requests
import json
import os
from contextlib import redirect_stdout
from dotenv import load_dotenv

def main():
	city = input('Enter your city: ')
	state = input('Enter your state: ')
	query = input('Anything specific you want in your hotel?: ')
	check_in_date = input('Check in date (YYYY-MM-DD): ')
	check_out_date = input('Check out date (YYYY-MM-DD): ')
	
	load_dotenv()
	headers = {
		'engine': 'google_hotels',
		'q': query,
		'check_in_date': check_in_date,
		'check_out_date': check_out_date,
		'location': f'{city}, {state}',
		'api_key': os.getenv("API_KEY")
	}
	
	url = 'https://serpapi.com/search?engine=google_hotels'
	r = requests.get(url, headers)
	rJSON = r.json()
	
	with open('results.json', 'w') as f:
		with redirect_stdout(f):
			print(json.dumps(rJSON, indent=4))
	
	if 'search_metadata' in rJSON:
		if 'json_endpoint' in rJSON['search_metadata']:
			print(rJSON['search_metadata']['json_endpoint'])
	
if __name__ == "__main__":
	main()