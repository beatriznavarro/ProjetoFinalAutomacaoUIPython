from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    class_title_page = 'title'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_changes(url))

    def has_title(self, title_text):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_page == title_text

    def check_page(self, url, title_text):
        return self.is_url(url) and self.has_title(title_text)
