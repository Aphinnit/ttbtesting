from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from time import sleep


class taskmanagementScreen(PageObject):
    """
    Elements and keywords for the task management screen.
    """
    _locators = {
        # Mention locators here
        "add_new_task":'//android.view.View[@resource-id="add_task"]',
        "delete_task":'//android.view.View[@resource-id="tab_delete_task"]',

    }
        
    def _is_current_screen(self):
        """ Validate the user is on the taskmanagement screen """

        try:
            # Check if the element is present on the page
            self.aplib.wait_until_page_contains_element(self.locator.add_new_task, 5)
            print("User is on Task management Screen")
            return True
        except:
            # Element not found, handle the case
            print("User is not on Task management Screen")
            return False
    
    def user_clicks_on_add_new_task(self):
        """
        click on add new task
        """
        self.aplib.wait_until_page_contains_element(self.locator.add_new_task, 5)
        self.aplib.click_element(self.locator.add_new_task)

    def user_clicks_on_delete_task(self):
        """
        click on delete task
        """
        self.aplib.wait_until_page_contains_element(self.locator.delete_task, 5)
        self.aplib.click_element(self.locator.delete_task)

    
    
    