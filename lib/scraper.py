from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')

# Extract a specific heading
heading = doc.select('.heading-financier')
print(heading[0].contents[0].strip())

# Extract course titles
courses = doc.select('.heading-60-black.color-black.mb-20')

for course in courses:
    print(course.contents[0].strip())