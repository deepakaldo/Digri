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


def test_github_projects(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)
    digitalprofile.digital_profile_icon_click2()

    digitalprofile.project_experience_button()
    page.wait_for_timeout(5000)

    # Locator for the elements
    projects_locator = page.locator("//a[contains(@class,'flex items-center gap-4 w-full font-text font-xs')]")

    # Get all elements and iterate through them
    project_elements = projects_locator.element_handles()

    for i, project_element in enumerate(project_elements):
        text = project_element.text_content()  # Fetch the inner text of the element
        print(f"Project {i + 1}: {text}")


def test_github_projects_button(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)
    digitalprofile.digital_profile_icon_click2()

    digitalprofile.project_experience_button()
    page.wait_for_timeout(5000)

    # Locator for the project elements (GitHub projects)
    projects_locator = page.locator("//a[contains(@class,'flex items-center gap-4 w-full font-text font-xs')]")

    # Get all project elements
    project_elements = projects_locator.element_handles()

    # Iterate through each project element
    for i, project_element in enumerate(project_elements):
        text = project_element.text_content()  # Fetch the inner text of the element
        print(f"Project {i + 1}: {text}")

        # Click on the project element and expect a new page/tab to open
        with page.context.expect_page() as new_tab_info:
            project_element.click()  # This should open a new tab

        # Get the new tab page object
        new_tab = new_tab_info.value

        # Wait for the new tab to load
        new_tab.wait_for_load_state()

        # Get the current URL of the new tab
        current_url = new_tab.url

        # Assert that the URL contains the expected GitHub link
        assert "https://github.com/sreejithvm849" in current_url

        page.bring_to_front()
