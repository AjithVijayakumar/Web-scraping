from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

url = "https://www.imdb.com/chart/top/"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")       # run without opening browser window
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Anti-bot detection setup
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/118.0.5993.90 Safari/537.36"
)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)

    movies = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')
    data = []

    for movie in movies:
        try:
            rank = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text.split(".")[0]
        except:
            rank = "N/A"

        try:
            title = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text.split(".")[1]
        except:
            title = "N/A"
            
        
        try:
            year = movie.find_element(By.CSS_SELECTOR, 'span.cli-title-metadata-item:nth-of-type(1)').text
        except:
            year = "N/A"

        try:
            rating = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
        except:
            rating = "N/A"

        data.append({
            "Rank": rank,
            "Title": title,
            "Year": year,
            "Rating": rating
        })

    df = pd.DataFrame(data)
    df.to_csv("imdb_top_250.csv", index=False, encoding="utf-8")
    print(f"✅ Scraping complete!")
    print(f" Saved {len(df)} movies to imdb_top_250.csv")

except Exception as e:
    print("⚠️ Could not load movie data properly.")
    print("Error:", e)

finally:
    driver.quit()