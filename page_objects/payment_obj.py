from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
#from page_objects.payment_page import Payment_Page

class Payment_Object:
    "Page object for Payment page"
    def check_redirect_payment(self):
        result_flag = False
        payment_url = 'confirmation'
        current_url = self.get_current_url().lower()
        "Check the Payment screen is loaded on redirect"
        if payment_url in current_url:
            result_flag = True
            
        self.conditional_write(result_flag,
                positive='Landed on payment screen',
                negative='Could not land on payment screen',
                level='debug')    

        return result_flag 
