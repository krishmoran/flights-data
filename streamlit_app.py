import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', 'ec8b3258-14ab-45dc-a702-e8b727e29f55')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://chrome.browserless.io/webdriver',
        options=chrome_options
    )

    driver.get("https://www.amazon.com")

    st.code(driver.page_source)

