# 🚀 Job Scraper — Your Ultimate Python Job Listings Aggregator

**Job Scraper** is a powerful and flexible Python application that aggregates remote and local job listings from multiple top job boards like **RemoteOK**, **WeWorkRemotely**, and **LinkedIn**. It automatically collects, organizes, and styles job data in Excel files and even sends daily email updates directly to your inbox — saving you hours of tedious job hunting!

---

## ✨ Features

- 🔍 **Multi-site scraping:** Collects job postings from various trusted sources for broader coverage  
- 🎯 **Role & location filters:** Focus on specific roles like *Python Developer* or *Junior Software Engineer* and locations like *Jordan*  
- 📊 **Styled Excel output:** Generates professional, well-formatted Excel files with separate sheets per source, including bold headers and color highlights  
- 📧 **Automated daily email reports:** Sends your freshly scraped job listings every day so you never miss out  
- ⏰ **Scheduled scraping:** Runs automatically once per day using Python scheduling or Windows Task Scheduler  
- 🧩 **Extensible & modular:** Easily add more scrapers or customize email content to fit your needs  

---

## 🛠️ Setup & Installation

Follow these simple steps to get up and running in no time:

1. **Clone this repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/job-scraper.git
   cd job-scraper


2. Create a virtual environment (highly recommended)

On Windows:
python -m venv venv
venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate


3.Install the required dependencies:
pip install -r requirements.txt



4. Configure your email settings
Update the SMTP server, sender email, and receiver email in utils/email_sender.py to enable daily reports.


5.Run the scraper manually:
python main.py


Optional) Set up automatic daily scraping
Use Windows Task Scheduler, cron jobs, or Python’s built-in scheduler as demonstrated in main.py to automate scraping and emailing.





📁 Project Structure

job-scraper/
│
├── main.py               # Entry point with scheduler
├── requirements.txt      # Python dependencies
├── README.md             # This file
│
├── scraper/              # Web scrapers for different job sites
│   ├── remoteok_scraper.py
│   ├── wework_scraper.py
│   └── pythonjobs_scraper.py
│
├── utils/                # Utilities for file handling and email
│   ├── file_handler.py
│   └── email_sender.py
│
├── data/                 # Folder to store output Excel files
└── .gitignore




💡 How to Extend
Want to add more job sources or customize filtering criteria?

Add new scraper modules inside scraper/

Ensure each job dictionary includes a "Source" field

Update main.py to include your new scraper

Adjust email content or Excel styling in utils/ as needed



🙌 Contributions & Feedback
Contributions, feature requests, and bug reports are welcome! Feel free to open issues or submit pull requests.


⚖️ License
This project is open-source and available under the MIT License.


🚀 Let’s get you the job you deserve — one scrape at a time!

Let me know if you want me to help you write a LICENSE file or anything else!



