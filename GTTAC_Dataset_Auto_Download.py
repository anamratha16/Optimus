import os
import time
import shutil

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from zipfile import ZipFile 


#Note 1: Replace "C:/Terrorism Dashboard/Data/" with your zip folder path (from Step 1).
file_path = 'C:/Terrorism Dashboard/Data/GRID_as_csv_tables.zip'

#Note 2: Replace "C:/Terrorism Dashboard/Data/Extracted Data" with your extracted data folder path(From Step 2).
EData_path = 'C:/Terrorism Dashboard/Data/Extracted Data'

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://data.gttac.com/comparative-research-tool?_gl=1*1r61w8o*_ga*MjA2NjI1NDY5OC4xNzA2MDQxMjQ3*_ga_MQJV79VF3Q*MTcwODk5MTUwNS4xOS4xLjE3MDg5OTE1MDguMC4wLjA.')


try:
    # Wait for the "Agree" button to be clickable
    agree_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled"))
    )
    # Click the "Agree" button
    agree_button.click()
except Exception as e:
    print(f"An error occurred: {e}")


download_bt=driver.find_element(By.ID,'DownloadDropdown')
download_bt.click()
driver.find_element(By.NAME,"first_name").send_keys("Sanisha")
driver.find_element(By.NAME,"last_name").send_keys("Kolanu")
driver.find_element(By.ID,"email_address").send_keys("skolanu@gmu.edu")
driver.find_element(By.NAME,"organization").send_keys("George Mason University")


try:
    # Wait for the "codebook" checkbox to be clickable
    codebook_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "codebook"))
    )
    # Click the "codebook" checkbox
    codebook_checkbox.click()
except Exception as e:
    print(f"An error occurred while clicking on codebook checkbox: {e}")
    
try:
    # Wait for the "unfiltered" checkbox to be clickable
    unfiltered_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "unfiltered"))
    )
    # Click the "unfiltered" checkbox
    unfiltered_checkbox.click()
except Exception as e:
    print(f"An error occurred while clicking on unfiltered checkbox: {e}")



try:
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, 'download_button'))
    )
    submit_button.click()
except Exception as e:
    print(f"An error occurred while clicking the submit button: {e}")
    
    
    
timeout = 30  # Timeout in seconds
elapsed_time = 0
check_interval = 5  # Check every 5 seconds

while  elapsed_time < timeout:
    time.sleep(check_interval)
    elapsed_time += check_interval

if elapsed_time >= timeout:
    print("Download timed out.")
else:
    print("Download completed.")
    
  

# Checking if the zip file exists and delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")    
 
    
# Checking if the extracted data exists and delete it
def delete_directory_safely(EData_path):
    try:
        shutil.rmtree(EData_path)
    except FileNotFoundError:
        print("The directory does not exist.")
    except PermissionError:
        print("Permission denied. Cannot delete the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Moving file from default to the desired folder 
 
#Note 3: Replace "C:/Users/aakas/Downloads/" with your default download path.
os.rename('C:/Users/aakas/Downloads/GRID_as_csv_tables.zip',file_path)

# Extract the zip file and place the extracted data in the desired folder      
with ZipFile(file_path, 'r') as zObject:
    zObject.extractall( 
        path = EData_path) 
