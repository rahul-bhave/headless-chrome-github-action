"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Altoro Mutual Main Page
2. Altoro Mutual Login Page
3. Altro Mutual Bank Page
4. Altoro Mutual Transfer Fund Page
"""
from page_objects.zero_page import Zero_Page
from page_objects.Main_Page import Main_Page
from page_objects.Login_Redirect_Page import Login_Redirect_Page
from page_objects.Transfer_Fund_Redirect_Page import Transfer_Fund_Redirect_Page
from page_objects.Bank_Main_Redirect_Page import Bank_Main_Redirect_Page
import conf.base_url_conf

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "main_page":
            test_obj = Main_Page(base_url=base_url)
        elif page_name == "login_redirect_page":
            test_obj = Login_Redirect_Page(base_url=base_url)
        elif page_name == "transfer_fund_redirect_page":
            test_obj = Transfer_Fund_Redirect_Page(base_url=base_url)
        elif page_name == "bank_main_redirect_page":
            test_obj = Bank_Main_Redirect_Page(base_url=base_url)
        return test_obj

    get_page_object = staticmethod(get_page_object)