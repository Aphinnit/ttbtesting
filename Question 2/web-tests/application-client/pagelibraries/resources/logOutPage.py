from PageObjectLibrary import PageObject
from utils.generic_keywords import *

class logOutPage(PageObject):
    """
    WebElements and keywords for the logOutPage.
    """
    _locators = {
        # Mention locators here
        "logout_page":"xpath://h2[contains(.,'Secure Area')]",
        "logout_button":"xpath://i[contains(.,'Logout')]"
       
    }

    def _is_current_page(self):
        """
        Validate the user is on the loginPage.
        """
        if not verify_element_on_load(self.locator.logout_page):
            print("Loading Logout Page")

        element1 = verify_element_on_load(self.locator.logout_page)
        element2 = verify_element_on_load(self.locator.logout_page)
        if element1 and element2 is True:
            print("User is on log Out Page")
        else:
            print("User is not on log Out Page")
            return False
        return True

    def user_clicks_on_logout_button(self):
        """
        User click on the logOut Button
        """
        verify_element_and_click(self.locator.logout_button)
   
    
    
   
    
    