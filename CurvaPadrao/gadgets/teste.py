from flet import *

class AppTour:
    def __init__(self, apps):
        self.apps = apps
        self.current_index = 0
        self.create_tour()

    def create_tour(self):
        for app in self.apps:
            app.bgcolor = "red"
            app.on_click = self.handle_click

    def handle_click(self, event):
        if self.current_index < len(self.apps):
            current_app = self.apps[self.current_index]
            current_app.bgcolor = "blue"
            self.show_info(current_app)
            self.current_index += 1
            if self.current_index < len(self.apps):
                next_app = self.apps[self.current_index]
                next_app.bgcolor = "red"
        else:
            print("Tour finished")

    def show_info(self, app):
        print(f"App: {app.name}, Info: {app.info}")

# Define your app boxes
app1 = Container(content=Column(controls=[Text("App1")]))
app2 = Container(content=Column(controls=[Text("App2")]))
app3 = Container(content=Column(controls=[Text("App3")]))
app4 = Container(content=Column(controls=[Text("App4")]))

# Create a list of app boxes
apps = [app1, app2, app3, app4]

# Create an instance of the AppTour class with the list of apps
tour = AppTour(apps)

# Display the tour
for app in apps:
    app.show()


# import flet as ft

# def main(page: ft.Page):
#     page.fonts = {
#         "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
#         "Open Sans": "/fonts/OpenSans-Regular.ttf"
#     }

#     page.add(
#       ft.Text("This is rendered with Kanit font",font_family="Kanit"),
#       ft.Text("This is Open Sans font example", font_family="Open Sans")
#     )

# ft.app(target=main, assets_dir="assets")