import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Student/Desktop/webdriver/chromedriver.exe')
driver.get('http://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='css-6kffxp eb77b220'):
    name = a.find('h5')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
print(results)
