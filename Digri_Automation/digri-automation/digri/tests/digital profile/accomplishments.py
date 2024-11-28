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

    # Wait for 2 seconds before the next step
    page.wait_for_timeout(2000)

    digitalprofile.digital_profile_icon_click2()

    # Wait for 3 seconds before the next step
    page.wait_for_timeout(3000)

    digitalprofile.accomplishments_tab_section()

    name_certificate = "Certificate of Excellence"
    certificate_url = "http://certificate-url.com"
    issued_data = "2024-10-10"

    # Wait for 5 seconds before adding the accomplishment
    page.wait_for_timeout(5000)

    digitalprofile.add_learning_accomplishments(name_certificate, certificate_url, issued_data)

def test_certificate_url_click(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    # Wait for 2 seconds before the next step
    page.wait_for_timeout(2000)

    digitalprofile.digital_profile_icon_click2()

    # Wait for 3 seconds before the next step
    page.wait_for_timeout(3000)

    digitalprofile.accomplishments_tab_section()

    digitalprofile.click_link_if_text_matches('Certificate of Excellence')
