import sys
import os
from dotenv import load_dotenv
from digri.src.pages.student_login_page import LoginPage
from digri.tests.confest import set_up_tear_down_login

# Load environment variables from the .env file
load_dotenv()

# Access the variables
Email = os.getenv("EMAIL")
Password = os.getenv("PASSWORD")

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def test_login_with_standard_user(set_up_tear_down_login) -> None:
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    dashboard = login_p.do_login(credentials)
    assert dashboard.dashboard_text == "Dashboard"

