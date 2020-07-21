"""
This class handles all methods required for Main Page
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Main_object:

    signin_link = locators.signin_link
    login_redirect_heading = locators.login_redirect_heading
    
    result_flag = False

    @Wrapit._exceptionHandler
    def click_signin(self):
        "use this method to click on sign in"
        result_flag=self.click_element(self.signin_link,wait_time=3)
        self.conditional_write(result_flag,
            positive='click success',
            negative='click not success',
            level='debug')
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_login(self):
        result_flag = False
        if self.check_element_present(self.login_redirect_heading) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Login page',
               negative='Failed to go on Login page',
               level='debug')
           self.switch_page("login_redirect_page")
        return result_flag 

    @Wrapit._exceptionHandler
    def access_login_page(self):
        "method to access login page"
        result_flag = self.click_signin()
        result_flag &= self.check_redirect_login()

        return result_flag