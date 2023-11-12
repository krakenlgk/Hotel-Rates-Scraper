# Hotel Rates Scraper

This Python script allows you to scrape hotel rates and related information from a web page using Selenium and BeautifulSoup. It is particularly designed to extract details such as room names, rate names, guest information, cancellation details, currency amount, currency symbol, and a boolean value indicating whether it's a "Top Deal."

## How to Use

1. **Install Dependencies:**
   Make sure you have Python installed on your machine. Install the required Python packages using:

   ```bash
   pip install selenium beautifulsoup4
2. Update the `url` variable in the script with the URL of the hotel page you want to scrape.
3. Run the script:
   ```bash
   python hotel_rates_scraper.py
  The script will launch a headless browser, navigate to the specified URL, and extract information about room rates, guest details, cancellation policies, and more.
4. View the results:
The script will print the extracted information in a structured JSON format. You can also modify the script to save the data to a file or integrate it with other applications as needed.

## Customize
Feel free to customize the script according to your specific requirements. You can adjust the JavaScript paths, selectors, or add new features based on the structure of the web page you are working with.

