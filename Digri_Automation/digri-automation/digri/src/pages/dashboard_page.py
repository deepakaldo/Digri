class DashboardPage:
    def __init__(self, page):
        self.page = page

        self._dashboard = page.locator("//div[contains(text(),'Dashboard')]")

        # Logout
        self._logout_dropdown = page.locator("//div[@class='absolute bottom-0 right-0 p-0 bg-white rounded-md "
                                            "cursor-pointer shadow-md']//*[name()='svg']")
        # Locator for the Logout button inside the popup
        self._logout_popup_button = page.locator(
            "//button[@class='px-4 py-2 text-white bg-[#45A8A3] rounded-md hover:bg-[#2d7875] cursor-pointer "
            "inline-flex items-center']")
        # Locator for the Cancel button inside the popup
        self._cancel_button = page.locator(
            "//button[@class='pr-4 py-2 text-black underline hover:bg-gray-100 hover:rounded-md']")

        # My Schedule
        self._myschedule_day = page.locator("//p[normalize-space()='Day']")
        self._myschedule_month = page.locator("//p[normalize-space()='Month']")
        self._myschedule_days_chance_button = page.locator("//body/main/div/section/div/div/div/div/div/div/div["
                                                          "1]/div[1]/div[2]/div[1]/div[2]/div[2]")
        self._myschedule_months_chance_button = page.locator("//body/main/div/section/div/div/div/div/div/div/div["
                                                            "1]/div[1]/div[2]/div[1]/div[2]/div[2]")
        self._date_and_month_element = page.locator("//span[contains(@class, 'lg:text-[20px]') and contains(@class, 'font-medium') "
                                    "and contains(@class, 'text-[#222]')]")

        # Progess
        self._progress_digristats = page.locator("//p[contains(text(),'digri’s Stats')]")
        self._progress_globalPlatform = page.locator("//p[normalize-space()='Global Platforms']")
        self._refresh_button_locator = page.locator("svg.inline-block.mr-1.items-center.cursor-pointer")
        # progess - Practices
        self._practice_practice_details = page.locator("//p[contains(normalize-space(),'Practices')]")
        self._practice_yet_to_start_details = page.locator("[class*='text-[#FF9053]'][class*='text-[17px]'][class*='font-bold']").first
        self._practice_in_progress_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[1]")
        self._practice_completed_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[1]")
        self._practice_not_attended_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[1]")
        # progess - assessment
        self._assessment_practice_details = page.locator("//p[contains(normalize-space(),'Assessments')]")
        self._assessment_yet_to_start_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[2]")
        self._assessment_in_progress_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[2]")
        self._assessment_completed_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[2]")
        self._assessment_not_attended_details = page.locator("(//div[contains(@class,'text-[#F6D14A] text-[17px] font-bold')])[2]")



        # Hours Spent
        self._dashboard_hoursspent_dropdown_button = page.locator("//button[@class='ant-dropdown-trigger border-[2px] "
                                                                 "rounded-md p-3 text-xs flex items-center']")
        self._filters_button = page.locator("//div[contains(@class, 'flex lg:w-[105px] md:w-[70px] sm:w-["
                                           "90px] lg:h-[50px] md:h-[35px] sm:h-[30px] relative border-["
                                           "1px] border-[#D6DDE6] rounded-xl items-center justify-center "
                                           "gap-2 cursor-pointer')]")
        self._time_spent_mins = page.locator("//span[text()='Today Time Spent : ']/following-sibling::span[contains("
                                            "@class, 'text-xs')]")
        self._assessment_checkbox = page.locator("//button[@id='ag-charts-legend-item-0' and contains(@role,'switch')]")
        self._practice_checkbox = page.locator("//button[@id='ag-charts-legend-item-1' and contains(@role,'switch')]")


    @property
    def dashboard_text(self):
        return self._dashboard.text_content()

    # dashboard visible check
    def is_dashboard_visible(self):
        # Check if the dashboard is visible after canceling logout
        return self._dashboard.is_visible()

    # MySchedule Day and month button
    def my_schedule_day_button(self):
        return self._myschedule_day.click()

    def my_schedule_month_button(self):
        return self._myschedule_month.click()

    def month_change_button(self):
        return self._myschedule_months_chance_button.click()

    def day_change_button(self):
        return self._myschedule_days_chance_button.click()

    def date_and_month_text(self):
        self._date_and_month_element.text_content()


    # DigriStats & GlobalPlatform Button
    def progess_digristats_button(self):
        return self._progress_digristats.click()

    def progess_globalplatforms_button(self):
        return self._progress_globalPlatform.click()

    def refresh_button(self):
        self._refresh_button_locator.wait_for(state='visible')
        return self._refresh_button_locator.click()

    def pratice_details(self):
        return self._practice_practice_details.text_content()

    def yet_to_start_details(self):
        yet_to_start=self._practice_yet_to_start_details
        return yet_to_start.text_content()

    def in_progess_details(self):
        return self._practice_in_progress_details.text_content()

    def completed_details(self):
        yet_to_start=self._practice_completed_details
        return yet_to_start.text_content()

    def not_attended_details(self):
        not_attended=self._practice_not_attended_details
        return not_attended.text_content()



    # Hours spent
    def hourspent_dropdown_button(self):
        return self._dashboard_hoursspent_dropdown_button.click()

    def hourspent_dropdown_options(self, month):
        self._dashboard_hoursspent_dropdown_button.click()
        option_loctor = self.page.locator(f"//span[normalize-space()='{month}']")
        option_loctor.wait_for(state="visible")
        option_loctor.click()

    def timespent_mins(self):
        return self._time_spent_mins.text_content()

    def assessement_checkbox_hoursspent(self):
        return  self._assessment_checkbox.click()

    def practice_checkbox_hoursspent(self):
        return  self._practice_checkbox.click()



    # Calender Filter
    def calender_filters_button(self):
        self._filters_button.wait_for(state='visible')
        return self._filters_button.click()

    def select_all_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        # Define the XPath for the specific input element
        input_selector = ("//body[1]/main[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                          "1]/div[2]/div[2]/div[1]/div[2]/div[2]/input[1]")

        # Wait for the input element to be visible
        self.page.wait_for_selector(input_selector, state='visible')

        # Click the input element
        self.page.click(input_selector)

    def select_contest_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        # Define the XPath for the specific input element
        input_selector = ("// body / main / div / section / div / div / div / div / div / div / div / div / div / div "
                          "/ div / div / div[3] / input[1]")
        # Wait for the input element to be visible
        self.page.wait_for_selector(input_selector, state='visible')

        # Click the input element
        self.page.click(input_selector)

    def select_practice_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        # Define the XPath for the specific input element
        input_selector = ("// body / main / div / section / div / div / div / div / div / div / div / div / div / div "
                          "/ div / div / div[ 3] / input[1]")

        # Wait for the input element to be visible
        self.page.wait_for_selector(input_selector, state='visible')

        # Click the input element
        self.page.click(input_selector)

    def select_academiclabs_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        # Define the XPath for the specific input element
        input_selector = "//body/main/div/section/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/input[1]"
        # Wait for the input element to be visible
        self.page.wait_for_selector(input_selector, state='visible')

        # Click the input element
        self.page.click(input_selector)

    def select_assessment_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        # Define the XPath for the specific input element
        input_selector = "//body/main/div/section/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/input[1]"
        # Wait for the input element to be visible
        self.page.wait_for_selector(input_selector, state='visible')

        # Click the input element
        self.page.click(input_selector)

    def select_announcements_filter_option(self):
        # Click to open the dropdown
        self.calender_filters_button()

        input_selector = "//body/main/div/section/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/input[1]"

        self.page.wait_for_selector(input_selector, state='visible')

        self.page.click(input_selector)

    # progess refers button
    def click_refresh_button(self):
        self._refresh_button_locator.wait_for(state='visible')
        self._refresh_button_locator.click()

    # month and day
    def month_and_day_data(self):
        return self._date_and_month_element().text_content()
