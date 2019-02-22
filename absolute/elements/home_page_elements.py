class HomePageElements:
    def __init__(self, drive):
        self.driver = drive

    def device_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-10"]')

    def device_mgn_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-20"]')

    def device_protection_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-30"]')

    def device_policy_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-40"]')

    def device_app_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-50"]')

    def device_admin_btn(self):
        return self.driver.find_element_by_xpath('//li[@id="nav-list-item-70"]')
