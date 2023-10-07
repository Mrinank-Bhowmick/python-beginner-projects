from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv

# Step 1 : Login to LinkedIn

# Open Chrome and Login LinkedIn Login Site

driver = webdriver.Chrome()  #Used for accessing web browsers
url = 'https://www.linkedin.com/home'
driver.get(url)
sleep(3)


email_field = driver.find_element('id','session_key')
email_field.send_keys("YOUR_EMAIL_HERE")
sleep(3)

password_field = driver.find_element('name','session_password')
password_field.send_keys("YOUR_PASSWORD_HERE")
sleep(3)

login_field = driver.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
login_field.click()
sleep(3)


#Step 2 : Search for the profile

search_field = driver.find_element('xpath', '//*[@id="global-nav-typeahead"]/input')
search_query = input('What Profile you want to scrape ?')   #seach query like "Software Engineer"
search_field.send_keys(search_query)
sleep(3)
search_field.send_keys(Keys.RETURN)  #presses  enter
sleep(3)
people_link = driver.find_element('xpath','//a[contains(@href, "/search/results/people/") and contains(text(), "See all people results")]')
people_link.send_keys(Keys.RETURN)
sleep(4)


#step 3 : extracting data
def Geturl():
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    profiles = page_source.find_all('a', class_='app-aware-link')

    profile_list = []

    for profile in profiles:
        profile_url = profile['href']
        if "/in/" in profile_url:
            if profile_url not in profile_list:
                profile_list.append(profile_url)

    return profile_list




#defining the range to scrape the pages

number_of_page = int(input("Enter Number of pages you want to scrape: "))

url_all_page =[]

for page in range(number_of_page):
    url_one_page = Geturl()
    sleep(2)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)
    next_button = driver.find_element('xpath', '//button[@aria-label="Next"]')
    driver.execute_script("arguments[0].click();", next_button)
    url_all_page = url_all_page + url_one_page
    sleep(2)


# Step 4: Scraping the entire data and storing it

with open('output1.csv', 'w', newline='') as file_output:
    headers = ['Name', 'Job Title', 'Location', 'URL']
    writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writeheader()

    for linkedin_URL in url_all_page:
        driver.get(linkedin_URL)
        print('- Accessing profile:', linkedin_URL)

        sleep(2)
        page_source = BeautifulSoup(driver.page_source, "html.parser")
        try:
            name_element = page_source.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words')
            name = name_element.get_text(strip=True) if name_element else 'N/A'

            title_element = page_source.find('div', class_='text-body-medium break-words')
            title = title_element.get_text(strip=True) if title_element else 'N/A'

            location_element = page_source.find('span', class_='text-body-small inline t-black--light break-words')
            location = location_element.get_text(strip=True) if location_element else 'N/A'

            if search_query.lower() in title.lower():
                writer.writerow({headers[0]: name, headers[1]: title, headers[2]: location, headers[3]: linkedin_URL})

                print('--- Profile name:', name)
                print('--- Profile title:', title)
                print('--- Profile location:', location)
                print('\n')

        except:
            pass

print('Mission Completed!')