# google-maps-scraper
The Google Maps Scraper is a Python web scraper that extracts business names and phone numbers from Google Maps based on two input parameters: business type and location.


## Usage
  1. Clone this repository to your local machine:
  ```
  git clone https://github.com/martoast/google-maps-scraper.git
  ```
  2. Install the required Python packages:
  ```
  pip install -r requirements.txt
  ```
  3. Run the scraper with the following command:
  ```
  python3 scraper.py --business_type "<business-type>" --location "<location>"
  python3 scraper.py --business_type "RealEstate Developers" --location "San Diego"
  ```
  Replace <business-type> with the type of business you want to scrape (e.g., "restaurant", "hair salon", "grocery store") and <location> with the location you want to search (e.g., "New York City", "Los Angeles", "London").
  
  4. Wait for the scraper to finish. The output file will be saved in CSV format in the output/ folder.
  

##Output
The scraper outputs a CSV file with two columns: "Business Name" and "Phone Number". Each row corresponds to a business that matches the input parameters.
  
## Limitations
The Google Maps Scraper relies on web scraping, which means that it is subject to limitations imposed by Google Maps' Terms of Service and rate limits. Use this tool responsibly and ethically, and ensure that your use of the scraper complies with all applicable laws and regulations.

## Contributing
If you find a bug or want to suggest a new feature, please open an issue in the repository or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
