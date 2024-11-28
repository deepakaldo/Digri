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


def test_developer_skills(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digital_profile = DigitalProfile(page)

    digital_profile.digital_profile_icon_click2()

    page.wait_for_timeout(10000)

    output = digital_profile.foundation_skills_details()
    for text in output:
        cleaned_text = text.replace('\n', ' ').strip()  # Remove '\n' and leading/trailing spaces
        parts = cleaned_text.split()  # Split the cleaned string into parts
        language = " ".join(parts[:-1])  # Get the language part (everything except the last word)
        level = parts[-1]  # Get the level part (the last word)
        print(f"{language}: {level}")

def test_developer_standards(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    digitalprofile = DigitalProfile(page)

    digitalprofile.digital_profile_icon_click2()

    page.wait_for_timeout(10000)

    output = digitalprofile.projects_summary_details()
    # Iterate over each text item in the output list
    for text in output:
        # Step 1: Replace multiple \n with a single space and strip any extra spaces
        cleaned_text = text.replace('\n', ' ').strip()

        # Step 2: Split the cleaned text into meaningful parts
        parts = cleaned_text.split()

        # Step 3: Format the output in the desired format
        # Since the first part is "Projects Summary", we print it
        print(parts[0], parts[1])

        # Step 4: Reconstruct the rest of the segments and print them as per the requirement
        # Example: "Projects 2/2", "Analysed 0/2", "Quality Pass 0/2"
        print(f"Projects {parts[2]}")
        print(f"Analysed {parts[4]}")
        print(f"Quality Pass {parts[6]}")


def test_project_details(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}

    # Login process
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Navigate to the Digital Profile
    digitalprofile = DigitalProfile(page)
    digitalprofile.digital_profile_icon_click2()

    # Wait for some time to ensure the page loads (adjust if needed)
    page.wait_for_timeout(10000)

    # Fetch project details
    project_details_1 = digitalprofile.project_details_1()
    project_details_2 = digitalprofile.project_details_2()

    # Formatting `project_details_1`
    for detail in project_details_1:
        cleaned_text_1 = detail.replace('\n', ' ').strip()
        parts_1 = cleaned_text_1.split()

        # Extracting project details
        if "Project Name" in cleaned_text_1:
            print(f"Project Name: {parts_1[2]}")  # Adjust index if needed
        if "Project Size" in cleaned_text_1:
            print(f"Project Size: {parts_1[5]}")  # Adjust index if needed
        if "Lines" in cleaned_text_1:
            print(f"Lines of code: {parts_1[9]}")  # Adjust index if needed
        if "Quality Gate" in cleaned_text_1:
            print(f"Quality Gate: {' '.join(parts_1[12:])}")  # Adjust index if needed

    print()  # Print a new line for separation

    # Formatting `project_details_2`
    for detail in project_details_2:
        cleaned_text_2 = detail.replace('\n', ' ').strip()
        parts_2 = cleaned_text_2.split()

        # Extracting and formatting details properly
        if "Reliability" in cleaned_text_2:
            reliability_value = ' '.join(parts_2[3:])  # Join remaining parts
            print(f"Reliability: {parts_2[1]} ({parts_2[2]}) - {reliability_value}")
        elif "Security" in cleaned_text_2:
            security_value = ' '.join(parts_2[3:])  # Join remaining parts
            print(f"Security: {parts_2[1]} ({parts_2[2]}) - {security_value}")
        elif "Maintainability" in cleaned_text_2:
            maintainability_value = ' '.join(parts_2[3:])  # Join remaining parts
            print(f"Maintainability: {parts_2[1]} ({parts_2[2]}) - {maintainability_value}")
        elif "Duplications" in cleaned_text_2:
            duplication_value = ' '.join(parts_2[3:])  # Join remaining parts
            print(f"Duplication: {parts_2[1]} ({parts_2[2]}) - {duplication_value}")


def test_previous_project_change_button(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}

    # Login process
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Navigate to the Digital Profile
    digitalprofile = DigitalProfile(page)
    digitalprofile.digital_profile_icon_click2()

    # Wait for some time to ensure the page loads (adjust if needed)
    page.wait_for_timeout(10000)

    digitalprofile.previous_project_button_click()


def test_next_project_change_button(set_up_tear_down_login):
    page = set_up_tear_down_login
    credentials = {'Email': Email, 'Password': Password}

    # Login process
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Navigate to the Digital Profile
    digitalprofile = DigitalProfile(page)
    digitalprofile.digital_profile_icon_click2()

    # Wait for some time to ensure the page loads (adjust if needed)
    page.wait_for_timeout(10000)

    digitalprofile.next_project_button_click()