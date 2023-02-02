from resultat import *
import os

out_dir = "data/"
# create output directory if not exists
os.path.isdir(out_dir) or os.makedirs(out_dir)

url = "https://resultatselection.belgium.be/fr/"

# Start browser
browser = webdriver.Firefox()  # Start browser
time.sleep(1)  # Wait for browser to start
browser.get(url)  # Open URL
time.sleep(1)  # Wait for page to load
text = browser.page_source  # Get HTML source

dom = etree.HTML(text)  # Parse HTML source

# Get all available options
election_types = dom.xpath(
    '//select[@id="select_election_type"]/option/@data-slug')[1:]  # Election types

for type in election_types:
    # Scrape all available dates
    url = "https://resultatselection.belgium.be/fr/search/%s" % type  # Append type to URL
    browser.get(url)  # Open URL
    time.sleep(1)  # Wait for page to load
    text = browser.page_source  # Get HTML source
    dom = etree.HTML(text)  # Parse HTML source

    election_dates = dom.xpath(
        '//select[@id="select_election_date"]/option/@data-slug')  # Election dates

    for date in election_dates:
        # Scrape all available regions
        # Append type and date to URL
        url = "https://resultatselection.belgium.be/fr/search/%s/%s" % (
            type, date)
        browser.get(url)  # Open URL
        time.sleep(1)  # Wait for page to load
        text = browser.page_source  # Get HTML source
        dom = etree.HTML(text)  # Parse HTML source

        election_descriptions = dom.xpath(
            '//select[@id="select_election_description"]/option/@data-slug')  # Election descriptions
        for description in election_descriptions:
            print('Downloading (%s,%s,%s)' % (type, date, description))
            # Download data for (type, date, description)
            data = download_election(type, date, description, browser)
            os.path.isdir(out_dir+'%s/%s/' % (type, date)
                          ) or os.makedirs(out_dir+'%s/%s/' % (type, date))
            data.to_csv(out_dir+'%s/%s/%s.csv' %
                        (type, date, description), index=False)

browser.close()  # Close browser
