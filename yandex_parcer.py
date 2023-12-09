



from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.by import By
import json
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CollectCompanies:

    def __init__(self) -> None:
        self.url = "https://yandex.ru/maps/-/CDehJS-Q"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.element_find = None
        self.element_click = None
        self.company_name = None
        self.company_link = None
        self.companies_data_json = None
        self.name_and_link = None

    
        

    def download_scroll_list(self):
        
        
        
        for i in range(1, 10000):
            try:
                
                self.element_find = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[7]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul/li[{i}]/div/div/div/div")
                
            except:
                    
                self.element_find = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[7]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul/li[{i-1}]/div/div/div/div")
                sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView();", self.element_find)
                sleep(3)
               
                
    def collect_company_list(self):
        for i in range(1, 10000):
            sleep(5)
                
            self.element_click = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[7]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul/li[{i}]/div/div/div/div")
            
            self.element_click.click()
            self.company_name = self.driver.find_element(By.CLASS_NAME, "card-title-view__title-link")
            print(self.company_name.text)
            sleep(1)
            self.company_link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, ".")
            # self.company_link = self.driver.find_element(By.CLASS_NAME , 'business-urls-view__link')
            print(self.company_link[-1].get_attribute('href'))
            # try:
            #     with open("companies_data.json", "r+") as file:
            #         self.companies_data_json = json.load(file)
            #     print("read JSON")
            # except Exception as e:
            #     print(e)


            # self.name_and_link = {self.company_name.text: self.company_link.get_attribute("href")}
            # self.companies_data_json.update(self.name_and_link)
            # try:
            #     with open("companies_data.json", "w") as file:
            #         json.dump(self.companies_data_json, file, ensure_ascii=False, indent=4)
            # except Exception as e:
            #     print("write JSON")
            sleep(2)
            
    
    


            
    def select_random_user_agent(self):
        with open("list_of_user_agents.txt") as file:
            data_users = file.readlines()
        random_user = random.choice(data_users)
        print(random_user)
        return random_user
        
    def webdriver_run(self):
        self.driver.get(url=self.url)
        self.driver.set_window_size(1920,1080)

        

run_yandex = CollectCompanies()
run_yandex.webdriver_run()
run_yandex.collect_company_list()
