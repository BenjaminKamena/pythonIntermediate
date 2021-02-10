from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\SAFAIDS-ZM\Desktop\Dufuna\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")
event_times = driver.find_elements_by_css_selector(".shrubbery time")
event_names = driver.find_elements_by_css_selector(".shrubbery li a")
events = {}
for n in range(len(event_times)):
 events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()
search = driver.find_element_by_name("search")
search.send_keys("Kamena")
search.send_keys(Keys.ENTER)
driver.close()
#driver.quit()