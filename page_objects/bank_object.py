"""
This class handles all methods for Bank object
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Bank_object:

    transfer_fund_redirect_heading = locators.transfer_fund_redirect_heading
    transfer_link = locators.transfer_link
    
    result_flag = False

    @Wrapit._exceptionHandler
    def clik_transfer_funds(self):
        "use this method to click transfer funds"
        result_flag=self.click_element(self.transfer_link, wait_time=3)
        self.conditional_write(result_flag,
            positive='transfer funds link clicked',
            negative='transfer funds link can not be clicked',
            level='debug')
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_transfer_fund(self):
        result_flag = False
        if self.check_element_present(self.transfer_fund_redirect_heading) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Tranasfer Fund page',
               negative='Failed to go on Transfer Fund page',
               level='debug')
           self.switch_page("transfer_fund_redirect_page")
        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def access_transfer_fund(self):
        "check access transfer fund is avialble"
        result_flag = self.clik_transfer_funds()
        result_flag &= self.check_redirect_transfer_fund()

        return result_flag