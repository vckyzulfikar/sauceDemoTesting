from selenium.webdriver.common.by import By
from pageObjects.confirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='inventory_item_name ']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)