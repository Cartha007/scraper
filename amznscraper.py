from bs4 import BeautifulSoup
import requests

def main():
    print('starting script...')
    url = "https://www.amazon.com/s?k=monitor&crid=3FVHM69NCLXFG&sprefix=mo%2Caps%2C1745&ref=nb_sb_noss_2"

    # Headers for request
    HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(url, headers=HEADERS).text
    # print(webpage)
    soup = BeautifulSoup(webpage, 'html.parser')
    # print(soup)
    
    # Fetch links as list of Tag Objects
    links = soup.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    # print(links)
    
    link = links[0].get('href')
    product_list = 'https://amazon.com' + link
    # print(product_list)
    
    new_webpage = requests.get(product_list, headers=HEADERS).text
    # print(new_webpage)
    
    new_soup = BeautifulSoup(new_webpage, 'html.parser')
    # print(new_soup)
    #Title
    pTitle = new_soup.find('span', attrs={'id': 'productTitle'}).text.strip()
    print(pTitle)
    #Price
    pPrice = new_soup.find('div', attrs={'id': 'corePrice_feature_div'})
    pPrice = pPrice.find('span', attrs={'class', 'a-offscreen'}).text.strip()
    # print(pPrice)
    #Ratings
    pRating = new_soup.find('span', attrs={'class': 'a-icon-alt'}).text
    # print(pRating)
    #Number of ratings
    pTotalRating = new_soup.find('span', attrs={'id': 'acrCustomerReviewText'}).text
    # print(pTotalRating)
    # Delivery date
    pDelivery = new_soup.find('div', attrs={'id': 'mir-layout-DELIVERY_BLOCK'}).text #deliveryBlockContainer
    # print(pDelivery)
    pDeliverTo = new_soup.find('div', attrs={'id': 'deliveryBlockContainer'}).find('a', attrs={'class': 'a-link-normal'}).text.strip()
    # print(pDeliverTo)
    pShipFee = new_soup.find('span', attrs={'class': 'a-size-base a-color-secondary'}).text
    # print(pShipFee)
    availability = new_soup.find('div', attrs={'id': 'availability'}).text.strip()
    print(availability)
    
    
    # items = soup.find_all('div', class_='s-list-col-right')
    # itemTitle = item.find('span', class_='a-size-medium a-color-base a-text-normal')
    # for index, item in enumerate(items):
    #     itemTitle = item.find('h2', class_='a-size-mini')
    #     print(index, itemTitle.text)
    #     print('')
    print('Script ended.')


if __name__ == '__main__':
    print('''====== Cartha's Amazon Scraper ======''')
    main()