import requests as req
from bs4 import BeautifulSoup
import csv

url = 'https://realpython.github.io/fake-jobs/'
res = req.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

results = soup.find(id='ResultsContainer')

def get_detail(job_elements):
    job_details = []
    for job_element in job_elements:
        detail = []
        title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('h3', class_='company')
        location_element = job_element.find('p', class_='location')
        links = job_element.find_all('a')
        link = links[1].get('href')
        detail.extend([
            title_element.text.strip(), company_element.text.strip(), 
            location_element.text.strip(), link
        ])
        job_details.append(detail)
    return job_details

def print_jobs(job_elements):
    job_details = get_detail(job_elements)
    for detail in job_details:
        for line in detail:
            print(line)
        print()

job_elements = results.find_all('div', class_='card-content')
# print(job_elements)

python_jobs = results.find_all(
    'h2', string=lambda title: 'python' in title.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print_jobs(python_job_elements)
job_details = get_detail(python_job_elements)

# Extra : Writing to a CSV file
with open('scraped_link.csv', 'w',newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Job Title', 'Company Name', 'Location', 'Apply Link'])
    csv_writer.writerows(job_details)
