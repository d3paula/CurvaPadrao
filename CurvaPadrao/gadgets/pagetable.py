import flet
import numpy as np
import matplotlib.pyplot as plt
from flet import *
from tools.aesthetic.colors import *

class Header(Container):
  
    def __init__(self):
        super().__init__(
            on_hover=self.toggler_search,
        )
        self.expand = True
        self.bgcolor=PAGE_MAIN,
        self.search_value: TextField = self.element_search_field(self.filter_rows)
        self.search: Container = self.element_search_bar(self.search_value)
        self.title: Any = Text("Curva Padrao",color='white')
        self.Userava=IconButton("person")

        content=Container(
                        height=60,
                        bgcolor=TABLE_HEADER,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=20, right=20),
                        content=Row(
                            alignment="SpaceBetween",
                            controls=[self.title, self.search, self.Userava]
                        )
                    )
        
def main(page:Page):
  page.bgcolor=PAGE_MAIN
  header=Header()
  page.add(
      Column(
          expand=True,
          controls=[
            header
          ]
      )
  )
  page.update()
app(target=main)
        