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

2. **Install dependencies**
    ```bash
    pip install selenium pandas webdriver-manager


3. **Run the script**
    ```bash
    python imdb_scraper_full.py


4. **Output**
The data will be saved as:

    imdb_top250.csv

5. **💾 Example Output**
   
   | Rank | Title                    | Year | Rating |
   | 1    | The Shawshank Redemption | 1994 | 9.2    |
   | 2    | The Godfather            | 1972 | 9.2    |
   | 3    | The Dark Knight          | 2008 | 9.0    |

<img width="321" height="97" alt="image" src="https://github.com/user-attachments/assets/710f682d-03a7-4689-b47e-a66c6f76352b" />


6. **🪄 Use Cases**

    Movie rating and trend analysis

    Personal film tracking system

    Training dataset for recommendation engines

    Data visualization and dashboards

7. **🧩 Future Enhancements**

    Scrape genres, directors, and cast information.

    Add a scheduling feature for periodic scraping.

    Create an interactive dashboard using Streamlit or Flask.

8. **🏁 Conclusion**

    The IMDb Movie Rating Scraper automates the process of collecting movie data from IMDb.
    It provides a robust and efficient foundation for analytics, visualization, and recommendation-based applications.






