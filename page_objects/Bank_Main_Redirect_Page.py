"""
This class models the altoro bank page
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.bank_object import Bank_object

class Bank_Main_Redirect_Page(Base_Page,Bank_object):
    "Page Object for the Bank Main Page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/bank/main.jsp'
        self.open(url)