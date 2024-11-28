from digri.src.pages.digital_profile_page import DigitalProfile
from digri.tests.confest import set_up_tear_down_login
import sys
import os
from dotenv import load_dotenv
from digri.src.pages.student_login_page import LoginPage

# Load environment variables from the .env file
load_dotenv()

# Access the variables
Email = os.getenv("EMAIL")
Password = os.getenv("PASSWORD")

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

def test_practice_status(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    digitalprofile.digital_profile_icon_click2()

    digitalprofile.problem_sloving_section()

    page.wait_for_timeout(5000)

    status = digitalprofile.digri_practice_status()

    for item in status[0].split('\n'):
        print(item)

def test_practice_details(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    digitalprofile.digital_profile_icon_click2()

    digitalprofile.problem_sloving_section()

    page.wait_for_timeout(5000)

    details = digitalprofile.digri_practice_details()

    for item in details:
        label, value = item.split('\n\n')  # Split into label and value
        print(f"{label}: {value}")


def test_digitalflatform_details(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    digitalprofile.digital_profile_icon_click2()

    digitalprofile.problem_sloving_section()

    page.wait_for_timeout(5000)

    digital_flatform = digitalprofile.digitalprofile_details()

    for entry in digital_flatform:
        # Remove '\n' and split by it, this will give us individual pieces of information
        items = entry.split('\n')

        # Filter out any empty strings that may occur due to multiple '\n' in a row
        cleaned_items = [item for item in items if item]

        # Print each cleaned item in order
        for item in cleaned_items:
            print(item)

        # Add a line break after each entry for better readability
        print("-" * 30)

def test_source_leetcode(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    # Navigate to the necessary page
    digitalprofile.digital_profile_icon_click2()
    digitalprofile.problem_sloving_section()

    page.wait_for_timeout(5000)

    # Click the source_leetcode_button and capture the new tab
    with page.context.expect_page() as new_tab_info:
        digitalprofile.source_leetcode_button()  # This opens a new tab

    new_tab = new_tab_info.value  # Get the new tab page object

    # Wait for the new tab to load
    new_tab.wait_for_load_state()

    # Get the title of the new tab (LeetCode page)
    actual_title = new_tab.title()
    expected_string = 'LeetCode Profile'  # The expected part of the title

    # Assert that the title contains the expected string (LeetCode)
    assert expected_string in actual_title, f"Expected '{expected_string}' to be in '{actual_title}'"
