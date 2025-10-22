class NavigationPage:
    def __init__(self, context):
        self.context = context
        self.path = None

    def go_to(self, url):
        url = f"{self.context.BASE_URL.rstrip('/')}/{url.lstrip('/')}"
        self.context.driver.get(url)
        self.path = url

    def get_path(self):
        return self.path
