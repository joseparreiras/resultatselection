from resultat import *
import inquirer
import os

out_dir = "data/"

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

# Ask user for type
type_question = [
    inquirer.List('type',
                  message="What election type do you want?",
                  choices=election_types
                  ),
]
type = inquirer.prompt(type_question)['type']  # Get type from input

# Scrape all available dates
url = "https://resultatselection.belgium.be/fr/search/%s" % type  # Append type to URL
browser.get(url)  # Open URL
time.sleep(1)  # Wait for page to load
text = browser.page_source  # Get HTML source
dom = etree.HTML(text)  # Parse HTML source

election_dates = dom.xpath(
    '//select[@id="select_election_date"]/option/@data-slug')[1:]  # Election dates

# Ask user for date
date_question = [
    inquirer.List('date',
                  message="What election type do you want?",
                  choices=election_dates
                  ),
]
date = inquirer.prompt(date_question)['date']  # Get date from input

# Scrape all available regions
# Append type and date to URL
url = "https://resultatselection.belgium.be/fr/search/%s/%s" % (type, date)
browser.get(url)  # Open URL
time.sleep(1)  # Wait for page to load
text = browser.page_source  # Get HTML source
dom = etree.HTML(text)  # Parse HTML source

district_type = dom.xpath(
    '//select[@id="select_election_description"]/option/@data-slug')[1:]  # Election's district type

# Ask user for region
district_question = [
    inquirer.List('district',
                  message="What district type do you want?",
                  choices=district_type
                  ),
]
district = inquirer.prompt(district_question)[
    'district']  # Get district type from input

# Scrape all available communes
data = download_election(type, date, district, browser, out_dir)

# create output directory if not exists
os.path.isdir(out_dir) or os.makedirs(out_dir)
data.to_csv(out_dir+'resultat.csv')
