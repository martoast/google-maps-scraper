import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import argparse

parser = argparse.ArgumentParser(description='Scrape businesses from Google Maps')
parser.add_argument('industry', help='Industry to search for')
parser.add_argument('city', help='City to search in')
args = parser.parse_args()

industry = args.industry
city = args.city

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.google.com/maps')

# Wait for the search box to load
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'searchboxinput'))
)

# Type the search query and press Enter
search_query = f'{industry} in {city}'
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'hfpxzc'))
)
    
# Initialize the output list
output = []
urls = []

while True:
    # Find all the businesses in the search results
    businesses = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'hfpxzc'))
    )

    time.sleep(2)

    # Store the URLs of the businesses
    for business in businesses:
        url = business.get_attribute('href')
        if url not in urls:
            urls.append(url)

    # Scroll down to load more businesses
    driver.execute_script("arguments[0].scrollIntoView();", businesses[-1])
    time.sleep(2)

    # Break the loop if no new businesses are loaded
    new_businesses = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'hfpxzc'))
    )
    if len(new_businesses) == len(businesses):
        break


# Visit each business URL and scrape the data
for url in urls:
    driver.get(url)

    try:
        name = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'fontHeadlineLarge'))
        ).text
    except Exception as e:
        name = ""

    try:
        phone = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-item-id*='phone:']"))
        ).text
    except Exception as e:
        phone = ""
        
    if name and phone:
        print(name, phone)
        output.append((name, phone))

# Close the driver
driver.quit()

csv_filename = f'{city}.csv'
# Write the output to a CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Phone'])
    writer.writerows(output)

print("Scraping completed.")
