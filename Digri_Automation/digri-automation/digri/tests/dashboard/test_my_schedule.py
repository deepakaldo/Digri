from digri.src.pages.dashboard_page import DashboardPage
from digri.tests.confest import set_up_tear_down_login
from digri.src.pages.student_login_page import LoginPage
from digri.tests.confest import set_up_tear_down_login
import sys
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
Email = os.getenv("EMAIL")
Password = os.getenv("PASSWORD")

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


# Filter Selection
def test_select_filter_option(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    # Initialize the dashboard page
    dropdown = DashboardPage(page)
    dropdown.select_all_filter_option()


# Date and Month text Button
def test_date_and_month_text(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.date_and_month_text()


# Month Button
def test_next_month_button(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.month_change_button()


# Day Button
def test_next_day_button(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.pratice_details()

def test_month_and_day(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.month_and_day_data()