import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""


from selenium import webdriver
from selenium.webdriver.common.by import By

#scrape flight information from a google flight link with selenium
def scrape_flight_info(flight_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', 'ec8b3258-14ab-45dc-a702-e8b727e29f55')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://chrome.browserless.io/webdriver',
        options=chrome_options
    )

    driver.get(flight_url)
    html = driver.find_element(by = By.XPATH, value = '//body[@id = "yDmH0d"]').text.split('\n')
    return html

# create a form and submission in streamlit to use the above function
st.write('Enter a Google Flights URL to scrape flight information:')
flight_url = st.text_input('URL', 'https://www.google.com/travel/flights/search?hl=en#flt=JFK.LAX.2021-12-25;c:USD;e:1;sd:1;t:f;tt:o')
if st.button('Scrape'):
    st.write('Scraping flight information...')
    page_source = scrape_flight_info(flight_url)
    st.write(page_source)
    st.write('Done!')

