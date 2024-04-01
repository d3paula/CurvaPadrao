import flet 
from flet import *

class menu(UserControl):
  def __init__(self):
    super().__init__()
    
  def build(self):
    return Container(
      width=0,
      bgcolor=white,
      animate=animation.Animation(400, "decelerate"),
      clip_behavior=ClipBehavior.HARD_EDGE,
      content=Column(
        expand=True,
        controls=[
          Row(
            controls=Text(
              value="Gadgets",
              color=WHITE,
              size=12,
              weight="bold"
            ),
            Column(
              expand=True,
              controls=[
                ElevatedButton(value="Elevate",shape={'':RoundedRectangle(radius=4)})
              ]
            )  
          )
        ]
      )
    )
    