from web_automation.core_libs.browsers.Browser import Browser


class Chrome(Browser):
    def __init__(self):
        print(self.__class__.__name__)
    def getBrowserDriver(self):
        return "Chrome Driver"


