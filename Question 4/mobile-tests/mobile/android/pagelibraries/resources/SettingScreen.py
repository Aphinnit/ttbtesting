from PageObjectLibrary import PageObject
from utils.generic_keywords import *


class settingScreen(PageObject):
    """
    Elements and keywords for the Setting screen.
    """
    _locators = {
        # Mention locators here
        "setting_screen":'//android.view.View[@resource-id="setting_screen"]',
        "logout_button":'//android.view.View[@resource-id="button_common_log_out"]',
        "logout_confirm":'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]',
        "logout_cancel":'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]',
    }
    def _is_current_screen(self):
        """ Validate the user is on the setting screen """

        try:
            # Check if the element is present on the page
            self.aplib.wait_until_page_contains_element(self.locator.setting_screen, 5)
            print("User is on Setting Screen")
            return True
        except:
            # Element not found, handle the case
            print("User is not on Setting Screen")
            return False
        
    def user_clicks_on_log_out_button(self):
        """
        click log out button
        """
        self.aplib.wait_until_page_contains_element(self.locator.logout_button, 5)
        self.aplib.click_element(self.locator.logout_button)

    def user_clicks_on_log_out_confirm_button(self):
        """
        click logout confirm button
        """
        self.aplib.wait_until_page_contains_element(self.locator.logout_confirm, 5)
        self.aplib.click_element(self.locator.logout_confirm)

    def user_clicks_on_log_out_cancel_button(self):
        """
        click on log out cancel button
        """
        self.aplib.wait_until_page_contains_element(self.locator.logout_cancel, 5)
        self.aplib.click_element(self.locator.logout_cancel)

    