import requests
from bs4 import BeautifulSoup
import pandas as pd
# Replace with the URL of the university website you're scraping
university_url = "https://www.kluniversity.in/"
#use the link based on the university you want 

# Send a request to the website and get the HTML content
response = requests.get(university_url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Scrape the university details
university_name = soup.find("h1").text.strip()
university_website = university_url

# Handle missing address element
address_element = soup.find("div", {"class": "address"})
if address_element:
    university_address = address_element.text.strip()
else:
    university_address = "N/A"

# Handle missing phone element
phone_element = soup.find("div", {"class": "phone"})
if phone_element:
    university_phone = phone_element.text.strip()
else:
    university_phone = "N/A"

# Handle missing email element
email_element = soup.find("div", {"class": "email"})
if email_element:
    university_email = email_element.text.strip()
else:
    university_email = "N/A"

# Scrape course information
courses = []
course_sections = soup.find_all("div", {"class": "course-item"})
for course_section in course_sections:
    course_name = course_section.find("h3").text.strip()
    course_description = course_section.find("p").text.strip()
    courses.append({"Course Name": course_name, "Course Description": course_description})

# Scrape scholarship information
scholarships = []
scholarship_sections = soup.find_all("div", {"class": "scholarship-item"})
for scholarship_section in scholarship_sections:
    scholarship_name = scholarship_section.find("h3").text.strip()
    scholarship_description = scholarship_section.find("p").text.strip()
    scholarships.append({"Scholarship Name": scholarship_name, "Scholarship Description": scholarship_description})

# Create a DataFrame to hold the data
data = {
    "University Name": [university_name],
    "University Website": [university_website],
    "University Address": [university_address],
    "University Phone": [university_phone],
    "University Email": [university_email],
    "Courses": [courses],
    "Scholarships": [scholarships]
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("university_data.xlsx", index=False, sheet_name="University Info")

# Download the Excel file
from google.colab import files
files.download('university_data.xlsx')
