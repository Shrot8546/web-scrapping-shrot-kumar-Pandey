# University Data Web Scraper

This project is a web scraper that extracts data from the website of an international university, including information about the university, its courses, and scholarships. The data is then formatted and saved to an Excel file.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

## Getting Started

1. Clone the repository or download the project files.
2. Open the project in your preferred Python environment (e.g., Jupyter Notebook, Google Colab, or a local Python IDE).
3. Locate the `university-data-scraper.py` file and open it.
4. Update the `university_url` variable to the URL of the international university you want to scrape data from.
5. Run the script to generate the `university_data.xlsx` file.

## Usage

The web scraper script performs the following tasks:

1. Sends a request to the specified university website and retrieves the HTML content.
2. Parses the HTML content using BeautifulSoup to extract the following information:
   - University name, website, address, phone, and email
   - Course information (name and description)
   - Scholarship information (name and description)
3. Stores the extracted data in a pandas DataFrame.
4. Saves the DataFrame to an Excel file named `university_data.xlsx`.

The generated Excel file can be found in the same directory as the script. You can then submit this file, along with the web scraping script and a brief report, as required by the assignment.

## Customization

If you need to modify the web scraping script to adapt to the structure of a different university website, you can update the following parts of the code:

- The CSS selectors used to find the relevant HTML elements (e.g., `"div", {"class": "address"}`).
- The data extraction logic to handle any differences in the website's HTML structure.
- The DataFrame creation and Excel file saving process, if necessary.

Make sure to test the script thoroughly and review the generated Excel file to ensure the data is accurate and complete.

## Contribution

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
