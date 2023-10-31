from selenium import webdriver

class Browser():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(50)
    driver.maximize_window()
    
    def fechar_browser(self):
        self.driver.quit()

    def limpar_browser(self):
            self.driver.delete_all_cookies()
            self.driver.refresh()