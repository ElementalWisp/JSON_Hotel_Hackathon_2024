'''
Hackathon 2024
Developed by Anthony Jackson and Amy Phan
---Proof of concept---
'''

import requests
import json
import os
from contextlib import redirect_stdout
from dotenv import load_dotenv

def main():
	city = input('Enter the city: ')
	state = input('Enter the state: ')
	query = input('Keywords/tags: ')
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
	
if __name__ == "__main__":
	main()