"""
This class models the altoro mutual login page
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.login_object import Login_object

class Login_Redirect_Page(Base_Page,Login_object):
    "Page Object for the Altoro Mutual Login page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/login.jsp'
        self.open(url)