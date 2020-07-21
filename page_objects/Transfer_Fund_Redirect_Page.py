"""
This class models the altoro mutual transfer fund page
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.fund_object import Fund_object

class Transfer_Fund_Redirect_Page(Base_Page,Fund_object):
    "Page Object for the Transfer Fund"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/bank/transfer.jsp'
        self.open(url)