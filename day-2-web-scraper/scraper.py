import requests as req
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
res = req.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

results = soup.find(id='ResultsContainer')

def print_jobs(job_elements):
    for job_element in job_elements:
        title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('h3', class_='company')
        location_element = job_element.find('p', class_='location')
        print(
            title_element.text.strip(), company_element.text.strip(), 
            location_element.text.strip(), sep='\n', end='\n'*2
        )

job_elements = results.find_all('div', class_='card-content')
# print_jobs(job_elements)

python_jobs = results.find_all(
    'h2', string=lambda title: 'python' in title.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print_jobs(python_job_elements)
