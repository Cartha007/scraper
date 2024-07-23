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


def main():
    search_url = "https://www.imdb.com/find/?q="
    search_ref = "&ref_=nv_sr_sm"
    print('Enter movie name to search')
    search = input('>').split(" ")
    search_url += '%20'.join(search)
    print(search_url)



if __name__ == '__main__':
    # print('Starting script...')
    check_internet_connection()
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        print('Script ended.')