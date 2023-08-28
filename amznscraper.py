from bs4 import BeautifulSoup
import requests
import sys


def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=10)
        if response.status_code == 200:
            print("Internet connection is available.")
        else:
            print("Internet connection is not available.")
    except requests.ConnectionError:
        print("No internet connection available. You need an internet connection to run this script.")
        sys.exit()


def getProductInfo(url):
    # Headers for request
    HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(url, headers=HEADERS).text
    # print(webpage) # Check the request status without the .text
    soup = BeautifulSoup(webpage, 'html.parser')
    # print(soup)
    
    # Fetch links as list of Tag Objects
    links = soup.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    # print(links)
    
    for link in links:
        # link = links[0].get('href')
        product_list = 'https://amazon.com' + link.get('href')
        # print(product_list)
        
        new_webpage = requests.get(product_list, headers=HEADERS).text
        # print(new_webpage)
        
        new_soup = BeautifulSoup(new_webpage, 'html.parser')
        # print(new_soup)
        
        #Title
        pTitle = new_soup.find('span', attrs={'id': 'productTitle'}).text.strip()
        # print(pTitle)
        
        #Price
        pPrice = new_soup.find('div', attrs={'id': 'corePrice_feature_div'})
        pPrice = pPrice.find('span', attrs={'class', 'a-offscreen'}).text.strip()
        # print(pPrice)
        
        #Ratings
        pRating = new_soup.find('span', attrs={'class': 'a-icon-alt'}).text.strip()
        # print(pRating)
        
        #Number of ratings
        pTotalRating = new_soup.find('span', attrs={'id': 'acrCustomerReviewText'}).text.strip()
        # print(pTotalRating)
        
        # Delivery date
        pDelivery = new_soup.find('div', attrs={'id': 'mir-layout-DELIVERY_BLOCK'}).text.strip() #deliveryBlockContainer
        # print(pDelivery)
        pDeliverTo = new_soup.find('div', attrs={'id': 'deliveryBlockContainer'}).find('a', attrs={'class': 'a-link-normal'}).text.strip()
        # print(pDeliverTo)
        
        # Shipping month
        pShipFee = new_soup.find('span', attrs={'class': 'a-size-base a-color-secondary'}).text.strip()
        # print(pShipFee)
        
        #Availability
        availability = new_soup.find('div', attrs={'id': 'availability'}).text.strip()
        # print(availability)
        
        print('\n')
        print(f'Product Title: {pTitle}')
        print(f'Price: {pPrice}')
        print(f'Availability: {availability}')
        print(f'Rating: {pRating} ({pTotalRating})')
        print(f'Delivery: {pDelivery}')
        print(f'{pDeliverTo}')
        print(f'Shipping: {pShipFee} \n')
    

def main():
    print('''====== Cartha's Amazon Scraper ======\n''')
    print('Enter your keyword to search for')
    search = input('>').split(" ")
    main_url = "https://www.amazon.com/s?k="
    for i in range(len(search)):
        main_url += search[i] + '+'
    
    print('Searching for products, please wait...')
    getProductInfo(main_url)
    
    # url = "https://www.amazon.com/s?k=monitor&crid=3FVHM69NCLXFG&sprefix=mo%2Caps%2C1745&ref=nb_sb_noss_2"

    import requests

    


if __name__ == '__main__':
    # print('Starting script...')
    check_internet_connection()
    main()
    print('Script ended.')