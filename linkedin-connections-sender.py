import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

USERNAME = "USERNAME@GMAIL.COM" # Replace with your LinkedIn username
PASSWORD = "PASSWORD" # Replace with your LinkedIn password

def login(driver):
    # Getting the login element
    username = driver.find_element(by=By.ID, value="session_key")

    # Sending the keys for username
    username.send_keys(USERNAME)

    # Getting the password element
    password = driver.find_element(by=By.ID, value="session_password")

    # Sending the keys for the password
    password.send_keys(PASSWORD)

    # Getting the tag for the submit button
    driver.find_element(by=By.CSS_SELECTOR, value='[data-id="sign-in-form__submit-btn"]').click()

def goto_network(driver):
    driver.get("https://www.linkedin.com/mynetwork/")

def send_requests(driver):
    # Wait for 3 seconds to ensure the page loads
    time.sleep(3)

    # Find and click buttons with class names like "emberNN"
    invite_buttons = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Invite")]')

	# Print number of buttons found	
    print(f"Total number of invite buttons found: {len(invite_buttons)}")

    for i, button in enumerate(invite_buttons, start=1):
        try:
            # Get the aria-label attribute
            aria_label = button.get_attribute('aria-label')
        
            # Scroll to the button to make it clickable
            ActionChains(driver).move_to_element(button).perform()
            button.click()
            print(f"Invitation {i}: {aria_label} successful!")
            time.sleep(2)  # Add a delay after clicking each button
        except Exception as e:
            print(f"OOPS! Invitation {i}: {button.get_attribute('aria-label')} unsuccessful! -_-")
            
    print("Clicked all invitation buttons!")


def main():
    # URL of LinkedIn
    url = "https://www.linkedin.com/"

    # Path to the Chrome web driver using macOS
    chromedriver_path = '/usr/local/bin/chromedriver'

    # Path to the Chrome web driver using Windows
    # chromedriver_path = 'C:/path/to/chromedriver.exe' # Replace with your path

    # Create a Service object for the ChromeDriver
    service = Service(chromedriver_path)

    # Set the options for the ChromeDriver (you can add more options as needed)
    chrome_options = webdriver.ChromeOptions()

    # Create the ChromeDriver with the Service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    login(driver)
    goto_network(driver)
    send_requests(driver)

    # Close the browser when done
    driver.quit()

# Driver's code
if __name__ == "__main__":
    main()
