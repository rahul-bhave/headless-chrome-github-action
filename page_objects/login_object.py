"""
This class handles all methods for Login Object
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Login_object:

    username_field = locators.username_field
    password_field = locators.password_field
    submit_button = locators.submit_button
    bank_main_page_redirect_title = locators.bank_main_page_redirect_title
    transfer_link = locators.transfer_link
    
    result_flag = False

    @Wrapit._exceptionHandler
    def set_username(self, username):
        "user this method to enter username"
        result_flag = self.set_text(self.username_field,username)
        self.conditional_write(result_flag,
            positive='Set the Username to: %s'%username,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_password(self, password):
        "user this method to enter username"
        result_flag = self.set_text(self.password_field,password)
        self.conditional_write(result_flag,
            positive='Password set succeefully',
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    def click_submit(self):
        "use this method to click submit"
        result_flag=self.click_element(self.submit_button, wait_time=3)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login(self, username, password):
        "submit the form"
        result_flag = self.set_username(username)
        result_flag &= self.set_password(password)
        result_flag &= self.click_submit()

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_bank_page(self):
        result_flag = False
        if self.check_element_present(self.bank_main_page_redirect_title) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Bank page',
               negative='Failed to go on Bank page',
               level='debug')
           self.switch_page("bank_main_redirect_page")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def verify_bank_main_page(self):
        "check you are bank main page"
        result_flag = self.check_redirect_bank_page()

        return result_flag