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

load_dotenv()


class AppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up WebDriver and get google login credentials from arguments"""
        cls.google_email = os.getenv("GMAIL")
        cls.google_password = os.getenv("GOOGLE_PASSWORD")

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
    def google_button(self: "AppTest"):
        google_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, "oauth__google-button"))
        )
        return google_button

    def setUp(self):
        """Set up a new WebDriver for each test"""
        self.driver = webdriver.Chrome()
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

    def test_googleoauth_flow(self: "AppTest"):
        self.google_button.click()
        time.sleep(5)

        email_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//input[@type='email']"))
        )
        email_input.send_keys(self.google_email)  # Use your test email
        email_input.send_keys(Keys.RETURN)
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
