import requests
from bs4 import BeautifulSoup

def scrape_python_jobs():
    url = "https://www.python.org/jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.select(".list-recent-jobs li")
    job_data = []

    for job in jobs:
        try:
            title = job.find("h2").text.strip()
            company = job.find("span", class_="listing-company-name").text.strip()
            location = job.find("span", class_="listing-location").text.strip()
            link = "https://www.python.org" + job.find("a")["href"]
            job_data.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Link": link,
                "Source": "Python.org"
            })
        except Exception:
            continue

    return job_data
