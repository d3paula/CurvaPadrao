from flet import *
from tools.aesthetic.colors import *
from gadgets.PTable import PTable
from pages.ForgotPassword import ForgotPassword
from gadgets.Element_Submit import MainPage
from pages.Gadgets import Gadgets 
from pages.Login import Login
from pages.Signup import Signup


class main(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.init_helper()        
        

    # def main_page_main(page: Page):
    # app(target=ptable, assets_dir='assets', view=WEB_BROWSER, web_renderer=WebRenderer.HTML)


    def init_helper(self,):
        
        self.page.on_route_change = self.on_route_change
        self.page.go('/gadgets')

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/forgotpassword": ForgotPassword,
            "/signup": Signup,
            "/mainpage": MainPage,
            "/ptable": PTable,
            "/gadgets": Gadgets
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page])
        )


app(target=main, assets_dir='assets', view=WEB_BROWSER, web_renderer=WebRenderer.HTML)
