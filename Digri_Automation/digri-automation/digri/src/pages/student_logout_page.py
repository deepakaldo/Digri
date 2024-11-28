class StudentLogoutPage:
    def __init__(self, page):
        self.page = page
        self._dashboard = page.locator("//div[contains(text(),'dashboard')]")
        self._logoutDropDown = page.locator("//div[@class='absolute bottom-0 right-0 p-0 bg-white rounded-md "
                                            "cursor-pointer shadow-md']//*[name()='svg']")
        # Locator for the Logout button inside the popup
        self.logout_popup_button = page.locator(
            "//button[@class='px-4 py-2 text-white bg-[#45A8A3] rounded-md hover:bg-[#2d7875] cursor-pointer "
            "inline-flex items-center']")
        # Locator for the Cancel button inside the popup
        self.cancel_button = page.locator(
            "//button[@class='pr-4 py-2 text-black underline hover:bg-gray-100 hover:rounded-md']")

    @property
    def logout_dropdown1(self):
        return self._logoutDropDown.click()

    def logout_dropdown(self):
        return self._logoutDropDown.click()

    def select_dropdown_option(self, option_text):
        # Click to open the dropdown
        self.logout_dropdown()
        # Wait for the option to be visible and click the option by its text
        option_locator = self.page.locator(f"//a[normalize-space()='{option_text}']")
        option_locator.wait_for(state='visible')
        option_locator.click()

    # Confirm and Cancel Button
    def confirm_logout(self):
        # Ensure the logout button is visible before interacting
        self.logout_popup_button.wait_for(state="visible")
        # Click the 'Logout' button inside the popup
        self.logout_popup_button.click()

    def cancel_logout(self):
        # Ensure the cancel button is visible before interacting
        self.cancel_button.wait_for(state="visible")
        # Click the 'Cancel' button inside the popup
        self.cancel_button.click()
        # Optionally wait for the popup to close or verify that it has closed
        self.page.locator("//div[contains(text(),'Logout')]").wait_for(state="hidden",
                                                                       timeout=2000)  # Adjust as necessary


