import pandas as pd
from scraper.remoteok_scraper import scrape_remoteok_jobs
from scraper.wework_scraper import scrape_wework_jobs
from scraper.pythonjobs_scraper import scrape_python_jobs
from utils.file_handler import save_to_excel
from utils.email_sender import send_email_with_attachment

import schedule
import time

def main():
    jobs = []
    jobs += scrape_remoteok_jobs()
    jobs += scrape_wework_jobs()
    jobs += scrape_python_jobs()
    
    # ✅ Save and get Excel file path
    excel_path = save_to_excel(jobs)

    # ✅ Send email with attachment
    send_email_with_attachment(
        recipient_email="sqatmah@gmail.com",  # 🔁 CHANGE THIS
        subject="📊 Daily Job Scraper Report",
        body="Attached is today's job scraping report with jobs from multiple sources.",
        attachment_path=excel_path
    )

def job():
    print("⏰ Scraping jobs...")
    main()
    print("✅ Done.")

# ✅ Schedule once a day at 8:00 AM
schedule.every().day.at("08:00").do(job)

# ✅ Run continuously
while True:
    schedule.run_pending()
    time.sleep(60)
