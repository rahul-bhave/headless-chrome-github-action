"""
This class handles all methods for Transfer Fund object
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Fund_object:

    from_account_dropdown = locators.from_account_dropdown
    from_account_option = locators.from_account_option
    to_account_dropdown = locators.to_account_dropdown
    to_account_option = locators.to_account_option
    transfer_amount_text = locators.transfer_ammount_text
    transfer_amount_button = locators.transfer_amount_button
    transfer_amount_check = locators.transfer_amount_check
    account_summary_link = locators.view_account_summary_link
    go_button = locators.go_button
    view_account_summary_check_heading = locators.view_account_summary_check_heading
    
    result_flag = False

    @Wrapit._exceptionHandler
    def add_from_account(self, from_account_dropdown, wait_time=3):
        "Use this method to add from Account"
        result_flag = self.click_element(self.from_account_dropdown)
        self.smart_wait(wait_time, self.from_account_dropdown)
        result_flag &= self.click_element(self.from_account_option)
        self.conditional_write(result_flag,
            positive='from account set',
            negative='failed to set from Account',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def add_to_account(self, to_account_dropdown, wait_time=1):
        "Use this method to add from Account"
        result_flag = self.click_element(self.to_account_dropdown)
        self.smart_wait(wait_time, self.to_account_dropdown)
        result_flag &= self.click_element(self.to_account_option)
        self.conditional_write(result_flag,
            positive='to account set',
            negative='failed to set to Account',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_transaction_amount(self, amount, wait_time=3):
        "Set the transaction amount"
        result_flag = self.set_text(self.transfer_amount_text, amount)
        self.smart_wait(wait_time,self.transfer_amount_text)
        self.conditional_write(result_flag,
            positive='transcations amount set %s'%amount,
            negative='could not set transaction amount',
            level='debug')

        return result_flag

    def submit_transfer_fund(self):
        "use this method to click on transfer fund button"
        result_flag = self.click_element(self.transfer_amount_button)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def transfer_fund(self, amount, wait_time=3):
        "use this method to transfer amount"
        result_flag = self.add_from_account(self.from_account_option)
        result_flag &= self.smart_wait(wait_time,self.from_account_option)
        result_flag &= self.add_to_account(self.to_account_option)
        result_flag &= self.smart_wait(wait_time, self.to_account_option)
        result_flag &= self.set_transaction_amount(amount)
        result_flag &= self.submit_transfer_fund()
        result_flag &= self.check_element_displayed(self.transfer_amount_check)
        result_flag &= self.smart_wait(wait_time, self.transfer_amount_check)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def click_view_account_summary(self):
        "click on view account summary"
        result_flag = self.click_element(self.account_summary_link, wait_time=3)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag
 
    @Wrapit._exceptionHandler
    def click_go_button(self):
        "clicking on go button"
        result_flag = self.click_element(self.go_button)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def view_account_summary(self, wait_time=3):
        "View account summary"
        result_flag = self.click_view_account_summary()
        result_flag &= self.click_go_button()
        result_flag &= self.check_element_displayed(self.view_account_summary_check_heading)
        result_flag &= self.smart_wait(wait_time,self.view_account_summary_check_heading)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag  