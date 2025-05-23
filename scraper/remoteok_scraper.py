import requests
from bs4 import BeautifulSoup

def scrape_remoteok_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    jobs = soup.find_all("tr", class_="job")

    job_data = []
    for job in jobs:
        try:
            title = job.find("h2").text.strip()
            company = job.find("h3").text.strip()
            location = job.find("div", class_="location").text.strip()
            link = "https://remoteok.com" + job["data-href"]
            job_data.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Link": link,    # <-- comma here fixes syntax error
                "Source": "RemoteOK",
            })
        except Exception:
            continue

    return job_data
