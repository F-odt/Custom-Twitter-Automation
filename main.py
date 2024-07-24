import requests
import credentials as cr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class KanyeQuoteTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.quote = None

    def get_kanye_quote(self):
        response = requests.get("https://api.kanye.rest/")
        if response.status_code == 200:
            self.quote = response.json()['quote']
        else:
            self.quote = "Failed to get a Kanye quote. Ye must be busy."

    def tweet_kanye_quote(self):
        self.driver.get("https://x.com/login")

        # Wait for the sign-in element to be clickable and click it
        sign_in_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))
        )
        sign_in_element.click()

        # Wait for the username field, then enter username
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(cr.email, Keys.RETURN)

        try:
            # Wait for the password field and enter password
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(cr.password, Keys.RETURN)

        except TimeoutException:
            # If password field is not found, handle alternative login flow
            username_field_2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
            )
            username_field_2.send_keys(cr.username, Keys.RETURN)

            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(cr.password, Keys.RETURN)

            time.sleep(5)

        # Wait for the tweet box to be present
        tweet_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']"))
        )

        # Type the tweet and post it
        tweet_box.send_keys(f"Kanye West once said: '{self.quote}' #KanyeQuote")
        tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)


# Initialize the bot and post a Kanye quote
bot = KanyeQuoteTwitterBot()
bot.get_kanye_quote()
print(f"Kanye Quote: {bot.quote}")
bot.tweet_kanye_quote()
