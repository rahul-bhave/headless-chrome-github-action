#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main Page
signin_link = "xpath,//a[@id='LoginLink']"
login_redirect_heading = "xpath//h1[contains(text(),'Online Banking Login')]"

#Locators for login page
username_field = "xpath,//input[@id='uid']"
password_field = "xpath,//input[@id='passw']"
submit_button="xpath,//input[@value='Login']"
transfer_link = "xpath,//a[@id='MenuHyperLink3']"
transfer_fund_redirect_heading = "xpath//h1[contains(text(),'Transfer Funds')]"

#Locators for Transfer Fund Page
from_account_dropdown = "xpath,//select[@id='fromAccount']"
from_account_option = "xpath,//option[@value='800002']"
to_account_dropdown = "xpath,//select[@id='toAccount']"
to_account_option = "xpath,//option[@value='800003']"
transfer_ammount_text = "xpath,//input[@id='transferAmount']"
transfer_amount_button = "xpath,//input[@id='transfer']"
transfer_amount_check = "xpath,//span[@id='_ctl0__ctl0_Content_Main_postResp']"

#Locators for Bank Main Page
view_account_summary_link = "xpath,//a[@id='MenuHyperLink1']"
bank_main_page_redirect_title = "xpath,//p[contains(text(),'Welcome to Altoro Mutual Online.')]"

#Locators for View Account Summary
go_button = "xpath,//input[@value='   GO   ']"
view_account_summary_check_heading = "xpath,//h1[contains(text(),'Account History')]"