from PageObjectLibrary import PageObject
from utils.generic_keywords import *


class registerScreen(PageObject):
    """
    elements and keywords for the registerScreen.
    """
    _locators = {
        # Mention locators here
        
        "email_address":'//android.widget.EditText[@resource-id="text_input_login_email_address"]',
        "password":'//android.widget.EditText[@resource-id="text_input_login_password"]',
        "register_button":'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'
    }

    def _is_current_screen(self):
        """ Validate the user is on the register screen """

        try:
            # Check if the element is present on the page
            self.aplib.wait_until_page_contains_element(self.locator.email_address, 5)
            print("User is on Register Screen")
            return True
        except:
            # Element not found, handle the case
            print("User is not Register Screen")
            return False
    
    def user_enters_email_address(self,email):
        """
        enter the email address in the email address text box on Register Page
        param: minimal-todo@gmail.com
        """
        self.aplib.wait_until_page_contains_element(self.locator.email_address, 5)
        self.aplib.input_text(self.locator.email_address,email)

    def user_enters_password(self,password):
        """
        enter the password in the password text box on SignIn Page
        param: ttbtest123!
        """
        self.aplib.wait_until_page_contains_element(self.locator.password, 5)
        self.aplib.input_text(self.locator.password,password)

    def user_clicks_on_register_button(self):
        """
        click register button
        """
        self.aplib.wait_until_page_contains_element(self.locator.register_button, 5)
        self.aplib.click_element(self.locator.register_button)
    
    