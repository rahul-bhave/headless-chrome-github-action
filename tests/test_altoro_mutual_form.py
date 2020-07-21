"""
This is an example automated test to help you learn Qxf2's framework
Automated test will do the following:
    #Open altoromutual form.
    #Click on Sign In link
    #Fill the Login form
    #Transfer the amount from one account to other
    #View the transfered amount
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from page_objects.main_object import Main_object
from page_objects.login_object import Login_object
from utils.Option_Parser import Option_Parser
import conf.bank_form_conf as account
import conf.login_form_conf as credentials
import conf.testrail_caseid_conf as testrail_file

def test_altoro_mutual_form(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Main_Page")

        #2. Setup and register a driver
        start_time = int(time.time())

        #3. Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #4. Access Login page
        result_flag = test_obj.access_login_page()
        test_obj.log_result(result_flag,positive="Login Page accessed\n",negative="Login Page not accessible")
        
        #5. Login into application
        username=credentials.username
        password=credentials.password
        result_flag = test_obj.login(username, password)
        test_obj.log_result(result_flag,positive="Login successful\n",negative="\nLogin not successful\n")

        #6. Verify you are on the Bank Main Page
        result_flag = test_obj.verify_bank_main_page()
        test_obj.log_result(result_flag,positive="You are on Bank page\n",negative="\nBank page not accessible\n")

        #7. Access Transfer Fund link
        result_flag = test_obj.access_transfer_fund()
        test_obj.log_result(result_flag,positive="Transfer fund accessible\n",negative="\n Transfer fund not accessible")
        
        #8. Transfer funds
        amount = account.amount
        result_flag = test_obj.transfer_fund(amount)
        test_obj.log_result(result_flag, positive="Amount transfered successfully\n", negative="\n Amount not transfered successfully\n")

        #9. View Account summary
        result_flag = test_obj.view_account_summary()
        test_obj.log_result(result_flag, positive="Account view summary shown\n", negative="\n Account view summary not shown\n")

        #10. waiting for pass counters
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

            
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':

  
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'   
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_altoro_mutual_form(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())