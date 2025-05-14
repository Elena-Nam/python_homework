from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://owasp.org/www-project-top-ten/'
driver.get(url)

time.sleep(2)

vulnerabilities = []

elements = driver.find_elements(By.XPATH, "//ul/li/a[contains(@href, '/Top10/')]")

for element in elements:
    vulnerability = {
        'title': element.text.strip(),
        'href': element.get_attribute('href')
    }
    vulnerabilities.append(vulnerability)

for vuln in vulnerabilities:
    print(f"Title: {vuln['title']}, Link: {vuln['href']}")

csv_file = 'owasp_top_10.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'href'])
    writer.writeheader()
    writer.writerows(vulnerabilities)

print(f" Data written to {csv_file}")

driver.quit()
