from selenium.webdriver.common.by import By
from Utilities.LoggingSetup import BaseClass
from Utilities.BrowserCall import setup
from pageObjects.confirmPage import ConfirmPage
from pageObjects.checkoutPage import CheckOutPage


class Testing(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        # Login Page
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Shop Page
        log.info("Getting All Items Name")
        confirmPage = CheckOutPage(self.driver)
        cards = confirmPage.getCardTitles()
        for card in cards:
            cardText = card.text
            log.info(cardText)

        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Checkout Basket
        self.driver.find_element(By.ID, "shopping_cart_container").click()

        # Confirm Items
        log.info("List Items on Basket")
        cart_lists = self.driver.find_elements(By.XPATH, "//div/a/div[@class='inventory_item_name']")
        cartText = [cart.text for cart in cart_lists]

        price_lists = self.driver.find_elements(By.XPATH, "//div/div[@class='inventory_item_price']")
        priceText = [price.text for price in price_lists]
        log.info("Item is: %s, Price is: %s", cartText, priceText)

        # Verifications item in baskets
        assert "Sauce Labs Backpack" in cartText, "Sauce Labs Backpack tidak ditemukan dalam cart_list"
        assert "Sauce Labs Bike Light" in cartText, "Sauce Labs Bike Light tidak ditemukan dalam cart_list"

        # Checkout
        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.ID, "first-name").send_keys("Vicky")
        self.driver.find_element(By.ID, "last-name").send_keys("Zulfikar")
        self.driver.find_element(By.ID, "postal-code").send_keys("16418")

        self.driver.find_element(By.ID, "continue").click()

        # Confirm List Item for Payment
        log.info("List Items on Basket")
        cart_lists = self.driver.find_elements(By.XPATH, "//div/a/div[@class='inventory_item_name']")
        cartText = [cart.text for cart in cart_lists]

        price_lists = self.driver.find_elements(By.XPATH, "//div/div[@class='inventory_item_price']")
        priceText = [price.text for price in price_lists]
        log.info("Item is: %s, Price is: %s", cartText, priceText)

        assert "Sauce Labs Backpack" in cartText, "Sauce Labs Backpack tidak ditemukan dalam cart_list"
        assert "Sauce Labs Bike Light" in cartText, "Sauce Labs Bike Light tidak ditemukan dalam cart_list"

        # Confirm Price Total
        total = 0
        for prices in price_lists:
            harga = float(prices.text.replace("$", ""))
            total += harga

        log.info(f"Item Total is: {total}")

        # SUM Total + Tax
        tax = 3.20
        sumTotal = total+tax

        log.info(f"Total Price is: {sumTotal}")

        # Button Finish
        self.driver.find_element(By.ID, "finish").click()

        completeOrder = self.driver.find_element(By.XPATH, "//div/h2[@class='complete-header']").text
        assert "Thank you for your order!" in completeOrder
        log.info(f"Complete Order: {completeOrder}")

        self.driver.find_element(By.ID, "back-to-products").click()