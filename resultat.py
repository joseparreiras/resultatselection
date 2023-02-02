from selenium import webdriver
from lxml import etree
import pandas as pd
import time
from tqdm import tqdm


def get_download_url(query, format="Csv"):
    """
    Function to get download URL from query.

    Args:
        query (str): id of the commune
        format (str, optional): format to download the data. Defaults to "Csv".

    Returns:
        str: url to download the data 
    """
    return "https://resultatselection.belgium.be/fr/Results/DataResult?electionLevelId=%s&dataType=%s" % (query, format)


def download_election(type, date, district, browser=None, wait_time=2):
    """
    Download the election data for a given type, date and district type using Selenium.

    Args:
        type (str): Election type
        date (str): Election date
        district (str): Election's district type
        browser (selenium.webdriver.firefox.webdriver.WebDriver, optional): Selenium browser. Defaults to None (Open new).
        wait_time (int, optional): Time for browser to wait between requests (in seconds). Defaults to 2.
    """

    # Starting URL
    url = "https://resultatselection.belgium.be/fr/search/%s/%s/%s" % (
        type, date, district)

    # Use selenium to browse the website
    if browser is None:
        browser = webdriver.Firefox()  # Start browser
        time.sleep(wait_time)  # Wait for browser to start
    browser.get(url)  # Open URL
    time.sleep(wait_time)  # Wait for page to load
    text = browser.page_source  # Get HTML source
    if browser is None:
        browser.close()  # Close browser

    dom = etree.HTML(text)  # Parse HTML source

    # Get list of hrefs and names from buttons
    href_list = dom.xpath(
        '//*[@class="btn btn-outline-primary btn-xl-alt w-100 d-flex align-items-center my-2"]/@href')[:-1]
    name_list = dom.xpath(
        '//*[@class="btn btn-outline-primary btn-xl-alt w-100 d-flex align-items-center my-2"]/span/text()')
    # Transform hrefs into IDs
    id_list = [h.split('/')[-1] for h in href_list]

    table = pd.DataFrame()  # Start a table to store the data

    # Loop over all IDs to download data
    for i in tqdm(range(len(id_list))):
        id = id_list[i]  # Get ID
        name = name_list[i]  # Get name
        download_url = get_download_url(id)  # Get download URL
        new_rows = pd.read_csv(download_url, sep=';')  # Read CSV file
        new_rows[district] = name  # Add district name
        table = pd.concat((table, new_rows))  # Append to table

    table['date'] = date  # Add election date to the table
    table['election'] = type  # Add election type to the table
    return table
