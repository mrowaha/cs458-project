import time
import unittest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
load_dotenv()

class AppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up WebDriver and get google login credentials from arguments"""
        cls.spotify_email = os.getenv("SPOTIFY_EMAIL")
        cls.spotify_password = os.getenv("SPOTIFY_PASSWORD")

    @property
    def email_input_field(self: "AppTest"):
        email_input_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "#credentials__email-input input"))
        )
        return email_input_field

    @property
    def password_input_field(self: "AppTest"):
        password_input_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "#credentials__password-input input"))
        )
        return password_input_field

    @property
    def sign_in_button(self: "AppTest"):
        sign_in_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, "credentials__sign-in-button"))
        )
        return sign_in_button

    @property
    def spotify_button(self: "AppTest"):
        spotify_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, "oauth__spotify-button"))
        )
        return spotify_button

    def setUp(self):
        """Set up a new WebDriver for each test"""
        options = Options()
        # options.add_argument("-profile")
        # options.add_argument(os.path.expanduser("~/snap/firefox/common/.mozilla/firefox/vucz17wc.default-1739580418569"))  # Replace with your profile name

        gecko_path = os.path.abspath("./geckodriver") 
        service = Service(gecko_path)
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        """Close WebDriver after each test"""
        self.driver.quit()

    # def test_incomplete_fields(self: "AppTest"):
    #     self.sign_in_button.click()
    #     email_error_toast = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.presence_of_element_located(
    #             (By.ID, "credentials__email-error"))
    #     )
    #     self.assertIsNotNone(
    #         email_error_toast, "Email Error Toast should be visible")

    #     password_error_toast = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.presence_of_element_located(
    #             (By.ID, "credentials__password-error"))
    #     )
    #     self.assertIsNotNone(password_error_toast,
    #                          "Password Erorr Toast should be visible")

    # def test_unauthorized_login(self: "AppTest"):
    #     self.email_input_field.send_keys("a")
    #     self.password_input_field.send_keys("b")
    #     self.sign_in_button.click()
    #     unauth_error_toast = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.presence_of_element_located(
    #             (By.ID, "login__unauthorized"))
    #     )
    #     self.assertIsNotNone(unauth_error_toast,
    #                          "Unauthorized should be visible")

    # def test_successful_login(self: "AppTest"):
    #     self.email_input_field.send_keys("john.doe@example.com")
    #     self.password_input_field.send_keys("P@ssw0rd123")
    #     self.sign_in_button.click()

    #     expected_url = "http://localhost:3000/dashboard"
    #     WebDriverWait(self.driver, 10).until(
    #         lambda d: d.current_url == expected_url)
    #     self.assertEqual(self.driver.current_url, expected_url,
    #                      "Expected Url after successful login should be /dashboard")

    def test_spotifyoauth_flow(self: "AppTest"):
        self.spotify_button.click()

        email_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, "login-username"))
        )
        email_input.send_keys(self.spotify_email)

        password_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, "login-password"))
        )
        password_input.send_keys(self.spotify_password)
        time.sleep(2)

        sign_in_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, "login-button"))
        )
        sign_in_button.click()

        # now we expect to be redirected to dashboard and have welcome message visible
        welcome_message = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, "dashboard__welcome-user"))
        )
        self.assertIsNotNone(welcome_message,
                             "User should be authorized via spotify oauth")


if __name__ == '__main__':
    unittest.main()
