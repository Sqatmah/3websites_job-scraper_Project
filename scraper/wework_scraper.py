import requests
from bs4 import BeautifulSoup

def scrape_wework_jobs():
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.select("section.jobs li:not(.view-all)")
    job_data = []

    for job in jobs:
        try:
            title = job.find("span", class_="title").text.strip()
            company = job.find("span", class_="company").text.strip()
            location = job.find("span", class_="region").text.strip()
            link = "https://weworkremotely.com" + job.find("a")["href"]
            job_data.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Link": link,
                "Source": "We Work Remotely"
            })
        except Exception:
            continue

    return job_data
