# BackEndAutomation

### Weather API Automation Testing

###### MAC OS Pre-requisites:

Python 3 
Homebrew 
pip (in case pip is not available on your system)<br />
    1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`<br />
    2. Move the get-pip.py file into your Python3 folder then run the below command from your terminal<br />
    3. `python3 get-pip.py` <br />

Please follow below instructions in order to run the framework and all the test cases in it from the terminal on your local machine:

  1. Clone the repository to your local machine: `git clone https://github.com/mukirashidov/BackEndAutomation.git`       
  2. Navigate to the cloned repository through your terminal 
  3. Execute the following commands (unless those packages are already installed and available on your machine) :<br />
              `pip install behave`<br />
              `pip install allure-behave`<br />
              `pip install requests`<br />
              `brew install allure`<br />
  4. To run the whole framework and generate Allure Results folder, execute the following command in your terminal from the project repo <br />
              `behave -f allure_behave.formatter:AllureFormatter -o %AllureResultsFolderName%` <br />
  5. Run below command in order to invoke Allure server (has to be ran from the project repository/folder or the absolute path needs to be provided) <br />
              `allure serve %AllureResultsFolderPath%` <br />
              
 
 
    
