from PageObjectLibrary import PageObject
from utils.generic_keywords import *


class taskdetailScreen(PageObject):
    """
    Elements and keywords for the task detail screen.
    """
    _locators = {
        # Mention locators here
        "task_detail_screen":'//android.view.View[@resource-id="task_detail_screen"]',
        
    }  
    def _is_current_screen(self):
        """ Validate the user is on the task detail screen """

        try:
            # Check if the element is present on the page
            self.aplib.wait_until_page_contains_element(self.locator.task_detail_screen, 5)
            print("User is on Task detail Screen")
            return True
        except:
            # Element not found, handle the case
            print("User is not on task detail Screen")
            return False
        

    def verify_validate_task_detail_display_correctly(self,csv):
        """
        verify and validate task detail display correctly 
        """
        self.aplib.wait_until_page_contains_element(self.locator.task_detail_screen, 5)
        self.aplib.element_text_should_be(self.locator.task_detail_screen,csv)
    
    