from datetime import time
import pytest
import sys
import os
from dotenv import load_dotenv
from digri.src.pages.dashboard_page import dashboard_Page
from digri.src.pages.student_login_page import LoginPage
from digri.tests.confest import set_up_tear_down_login

# Load environment variables from the .env file
load_dotenv()

# Access the variables
Email = os.getenv("EMAIL")
Password = os.getenv("PASSWORD")

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def test_digristats_button(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = dashboard_Page(page)

    # Click on the "digri's Stats" button
    dashboard.progess_digristats_button()

    # Assert that the expected element is visible after clicking "digri's Stats"
    assert page.locator("xpath_or_css_selector_for_digristats_page_or_element").is_visible(), "digri's Stats page is not visible"


def test_lobalplatforms_button(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = dashboard_Page(page)
    # Click on the "Global Platforms" button
    dashboard.progess_globalplatforms_button()

    # Assert that the expected element is visible after clicking "Global Platforms"
    assert page.locator(
        "xpath_or_css_selector_for_globalplatforms_page_or_element").is_visible(), "Global Platforms page is not visible"


def test_refresh_button(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = dashboard_Page(page)

    dashboard.refresh_button()


def test_pratice_details(set_up_tear_down_login):
    page = set_up_tear_down_login

    # Initialize login
    login = LoginPage(page)
    credentials = {'Email': Email, 'Password': Password}
    login.do_login(credentials)

    page.wait_for_timeout(10000)

    # dashboard Page
    dashboard = dashboard_Page(page)

    # Retrieve and print the 'yet to start details' text
    no_of_practice = dashboard.pratice_details()
    yet_to_start = dashboard.yet_to_start_details()
    in_progress = dashboard.in_progess_details()
    completed = dashboard.completed_details()
    not_attended = dashboard.not_attended_details()

    print("no of practice", no_of_practice)
    print("yet_to_start details:", yet_to_start)
    print("in_progress:", in_progress)
    print("completed:", completed)
    print("not_attended:", not_attended)


