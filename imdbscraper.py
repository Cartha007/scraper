from bs4 import BeautifulSoup
import requests, sys, json, csv


def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=15)
        if response.status_code == 200:
            print("Internet connection is available.")
        else:
            print("Internet connection is not available.")
    except requests.ConnectionError:
        print("No internet connection available. You need an internet connection to run this script.")
        sys.exit()
