# 🎬 IMDb Movie Rating Scraper

## 📖 Overview
The **IMDb Movie Rating Scraper** is a Python automation project that collects data from IMDb’s **Top 250 Movies** list.  
It uses **Selenium WebDriver** to extract movie details like rank, title, release year, and IMDb rating from dynamically loaded web content.  
All extracted data is neatly saved into a **CSV file** for further analysis or integration into other systems.

---

## 🚀 Features
- 🔹 **Dynamic Content Handling** – Uses Selenium to load and extract JavaScript-rendered data.  
- 🔹 **Comprehensive Movie Data** – Retrieves movie rank, name, release year, and IMDb rating.  
- 🔹 **CSV Export** – Saves the results in a structured CSV file (`imdb_top250.csv`).  
- 🔹 **Headless Mode** – Runs silently without opening a browser window.  
- 🔹 **Expandable** – Can be extended to fetch genres, cast, or plot summaries from each movie page.

---

## 🧰 Technologies Used
- **Python 3.x** – Programming language used for scripting.  
- **Selenium** – For browser automation and web scraping.  
- **pandas** – For data organization and CSV export.  
- **webdriver_manager** – For automatic ChromeDriver installation and management.

---

## ⚙️ Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AjithVijayakumar/Web-scraping.git
   cd imdb-movie-rating-scraper
