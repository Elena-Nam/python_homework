# 9.2
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# driver.get("https://en.wikipedia.org/wiki/Web_scraping")

# element = driver.find_element(By.TAG_NAME, "h1")
# print(element.text)
# title = driver.title # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
# print(title)
# body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one
# if body:
#     links = body.find_elements(By.CSS_SELECTOR,'a') # Find all the links in the body.
#     if len(links) > 0:
#         print("href: ", links[0].get_attribute('href'))  # getting the value of an attribute

# main_div = body.find_element(By.CSS_SELECTOR,'div[id="mw-content-text"]')
# if main_div:
#     bolds = main_div.find_elements(By.CSS_SELECTOR,'b')
#     if len(bolds) > 0:
#         print("bolds: ",bolds[0].text)

# # Extract all images with their src attributes
# images = [(img.get_attribute('src')) for img in body.find_elements(By.CSS_SELECTOR,'img[src]')] # all img elements with a src attribute
# print("Image Sources:", images)
# # hmm, this example uses a list comprehension.  We haven't talked about those.  This is the same as:
# image_entries = driver.find_elements(By.CSS_SELECTOR,'img[src]')
# images = []
# for img in image_entries:
#     images.append(img.get_attribute('src'))

# print("Image Sources:", images)
# driver.quit()


# 9.3 
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# robots_url = "https://en.wikipedia.org/robots.txt"
# driver.get(robots_url)
# print(driver.page_source)
# driver.quit()

# 9.4
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Web_scraping")  # this much you've seen before

# see_also_h2 = driver.find_element(By.CSS_SELECTOR,'[id="See_also"]') # our starting point
# links = []
# if (see_also_h2):
#     parent_div = see_also_h2.find_element(By.XPATH, '..') # up to the parent div
#     if parent_div:
#         see_also_div = parent_div.find_element(By.XPATH,'following-sibling::div' ) # over to the div with all the links
#         link_elements = see_also_div.find_elements(By.CSS_SELECTOR, 'a')
#         for link in link_elements:
#             print(f"{link.text}: {link.get_attribute('href')}")
#             name = link.text.strip()
#             url = link.get_attribute("href")
#             if name and url:
#                 links.append({"name": name, "url": url})


# driver.quit()

# import csv

# # Save extracted data to a CSV file
# with open('scraped_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Link"])
#     for link in links:
#         writer.writerow([link["name"], link["url"]])


# Save data to a JSON file
# data = {"links": links}
# with open('scraped_data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
      