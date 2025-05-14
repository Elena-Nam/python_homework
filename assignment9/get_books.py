from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
import json


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep(5)  # Wait for content to load

# Step 1: Find all <li> elements that represent search results
search_items = driver.find_elements(By.TAG_NAME, "li")

# Filter only those that have the correct class
search_items = [item for item in search_items if "cp-search-result-item" in item.get_attribute("class")]

# Step 2: Prepare the results list
results = []

# Step 3: Main loop to extract Title, Authors, Format-Year
for item in search_items:
    # Title
    try:
        title = item.find_element(By.CSS_SELECTOR, "h2.cp-title span.title-content").text
    except:
        title = "N/A"

    # Authors (can be more than one)
    try:
        author_elements = item.find_elements(By.CSS_SELECTOR, "span.cp-by-author-block a.author-link")
        authors = "; ".join([a.text for a in author_elements])
    except:
        authors = "N/A"

    # Format and Year
    try:
        format_year = item.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info-primary").text
    except:
        format_year = "N/A"

    # Append dictionary to results
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })

# Step 4: Create DataFrame and print
df = pd.DataFrame(results)
print(df)


# Task 4
# Step 1. Save to csv
os.makedirs("assignment9", exist_ok=True)
df.to_csv("assignment9/get_books.csv", index=False)

# Step 2. Save to json
with open("assignment9/get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=2)

driver.quit()
