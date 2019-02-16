class HomePageElements:
    def __init__(self, drive):
        self.driver = drive

    def find_device_btn(self):
        return self.driver.find_element_by_xpath('//li[@data-automation-id="nav-list-item-10"]')
