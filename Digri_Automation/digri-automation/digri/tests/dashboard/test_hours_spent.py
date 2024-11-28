from digri.src.pages.dashboard_page import DashboardPage
from digri.tests.confest import set_up_tear_down_login
from digri.src.pages.student_login_page import LoginPage
import sys
import os
from dotenv import load_dotenv
import  pytest
# Load environment variables from the .env file
load_dotenv()

# Access the variables
Email = os.getenv("EMAIL")
Password = os.getenv("PASSWORD")

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def test_month_selection(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    # List of months to iterate over
    months = ["3 months", "6 months", "9 months", "12 months"]

    for month in months:
        # Select the month from the dropdown
        dashboard.hourspent_dropdown_options(month)

        # Optional: Log or verify the selected month if you have a method for that
        print(f"Selected month: {month}")


def test_hours_spent_mins(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)
    mins = dashboard.timespent_mins()
    print(mins)


def test_assessement_checkbox_graph(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.assessement_checkbox_hoursspent()


def test_practice_checkbox_graph(set_up_tear_down_login):
    # Get the page instance from the fixture
    page = set_up_tear_down_login

    # Initialize the login page
    login = LoginPage(page)

    # Define credentials for login
    credentials = {'Email': Email, 'Password': Password}

    # Perform login and get the dashboard page instance
    login.do_login(credentials)

    dashboard = DashboardPage(page)

    dashboard.practice_checkbox_hoursspent()

