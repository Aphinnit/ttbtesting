from PageObjectLibrary import PageObject
from utils.generic_keywords import *

class logInPage(PageObject):
    """
    WebElements and keywords for the loginPage.
    """
    _locators = {
        # Mention locators here
        "login_page":"xpath://h2[contains(.,'Login Page')]",
        "username":"xpath://input[contains(@id,'username')]",
        "password":"xpath://input[contains(@id,'password')]",
        "login_button":"xpath://button[contains(.,'Login')]"
       
    }

    def _is_current_page(self):
        """
        Validate the user is on the loginPage.
        """
        if not verify_element_on_load(self.locator.login_page):
            print("Loading Login Page")

        element1 = verify_element_on_load(self.locator.username)
        element2 = verify_element_on_load(self.locator.password)
        if element1 and element2 is True:
            print("User is on log In Page")
        else:
            print("User is not on log In Page")
            return False
        return True
    
    def user_enters_username(self,csv):
        """
        enter the username in the username text box on logIn Page
        param: tomsmith
        """
        self.selib.input_text(self.locator.username,csv)

    def user_enters_password(self,csv):
        """
        enter the password in the password text box on logIn Page
        param: SuperSecretPassword!
        """
        self.selib.input_text(self.locator.password,csv)

    def user_clicks_on_login_button(self):
        """
        User click on the logIn Button
        """
        verify_element_and_click(self.locator.login_button)

   
    
    
   
    
    