from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

# Set up a headless browser
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Load the page
url = 'url'
driver.get(url)

# Wait for a short time to ensure JavaScript content is loaded (you may need to adjust this)
driver.implicitly_wait(5)

# Get the page source
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Your provided JavaScript path for the parent div
js_path_parent = '#__next > div > div > div.css-ommd71-Box.e1m6xhuh0 > div.css-n5x25a-Box.e1m6xhuh0 > div.css-34t0qr-Box.e1m6xhuh0 > div.css-bk9xu4-Box.ee2o81s0 > div > div:nth-child(3) > div'

# Use BeautifulSoup to find the desired element for the parent div
parent_div = soup.select_one(js_path_parent)

# Your provided JavaScript path for the child divs
js_path_child = '#__next > div > div > div.css-ommd71-Box.e1m6xhuh0 > div.css-n5x25a-Box.e1m6xhuh0 > div.css-34t0qr-Box.e1m6xhuh0 > div.css-bk9xu4-Box.ee2o81s0 > div > div:nth-child(3) > div > div'

# Use BeautifulSoup to find all the child divs
child_divs = parent_div.select(js_path_child)

# Your provided JavaScript path for the 3rd div (constant)
js_path_3rd_div = 'div.css-gclp3x-Box.e1yh5p92'

# Construct a dynamic selector for all h3 elements within the 3rd div
h3_selector = f'{js_path_3rd_div} h3'

# Construct a dynamic selector for the span within the 3rd div with the attribute data-testid="offer-guest-text"
span_selector = f'{js_path_3rd_div} [data-testid="offer-guest-text"]'

# Construct a dynamic selector for the button within the 3rd div with the attribute data-testid="cancellation-policy-message"
button_selector = f'{js_path_3rd_div} [data-testid="cancellation-policy-message"]'

# Construct a dynamic selector for the span within the 3rd div with the attribute data-testid="amount"
amount_selector = f'{js_path_3rd_div} [data-testid="amount"]'

# Construct a dynamic selector for the span within the 3rd div with the attribute data-testid="currency-symbol" and class "css-14s162u-Text.e1j4w3aq0"
currency_symbol_selector = f'{js_path_3rd_div} [data-testid="currency-symbol"].css-14s162u-Text.e1j4w3aq0 sup'

# Construct a dynamic selector for the span within the 3rd div with the class "css-1wta3u5-Box"
boolean_value_selector = f'{js_path_3rd_div} span.css-1jr3e3z-Text-BadgeText.e34cw120'

# List to store rate information
rates = []

# Iterate through each child div
for child_div in child_divs:
    # Extract room name
    room_name_selector = 'div.css-1grjpsc-Box-Flex.e1pfwvfi0 > div.css-1npdra2-Box-Flex.e1pfwvfi0 > div > div.css-v9e3m6-Hide.e1iw1znz0 > h3'
    room_name = child_div.select_one(room_name_selector).text.strip()

    # Extract rate names from the 3rd div
    rate_names = [rate_name.text.strip() for rate_name in child_div.select(h3_selector)]

    # Extract guest details from the 3rd div
    guest_details = child_div.select_one(span_selector).text.strip()

    # Extract the number of guests using regular expression
    guests_match = re.search(r'(\d+) guests', guest_details)
    num_guests = int(guests_match.group(1)) if guests_match else None

    # Extract cancellation details from the 3rd div
    cancellation_details = child_div.select_one(button_selector).text.strip()

    # Extract currency amount from the 3rd div
    currency_amount = child_div.select_one(amount_selector).text.strip()

    # Extract currency symbol from the 3rd div
    currency_symbol = child_div.select_one(currency_symbol_selector).text.strip()

    # Extract boolean value from the 3rd div
    boolean_value = child_div.select_one(boolean_value_selector).text.strip() == 'Top Deal'

    # Create a JSON object for each rate and guest
    for rate_name in rate_names:
        rate_info = {
            'Room_name': room_name,
            'Rate_name': rate_name,
            'Number_of_Guests': num_guests,
            'Cancellation_policy': cancellation_details,
            'Price': currency_amount,
            'Currency': currency_symbol,
            'Boolean_value': boolean_value
        }

        # Append the rate information to the list
        rates.append(rate_info)

# Print or use the rates list as needed
print('Rates Information:', rates)
