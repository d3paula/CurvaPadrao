from tools.aesthetic.colors import *
from flet import *


class Interface(Container):
    def __init__(self, page: Page):

        super().__init__()
        self.expand = True
        self.bgcolor = BG
        # Checkbox items
        def sbm_clicked(e):
        Checkbox(label=Init_t.value)
        Init_t.value = ""
        Init_t.focus()
        Init_t.update()

    # Creating TextBox: Choosing the element to construct the Standard Curve
    Init_t = TextField(label="Símbolo do Elemento", width=250)

    # Inserting the checkboxes column into the Row within first_page_contents
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='SpaceBetween',
                    controls=[
                        Container(
                            content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.LOGIN),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                                Icon(icons.HELP_OUTLINE_ROUNDED)
                            ],
                        ),
                    ],
                    ),
                Container(height=1),
                Text(
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    spans=[ft.TextSpan(" "),
                           ft.TextSpan('CURVA PADRÃO',
                                       ft.TextStyle(
                                           weight=ft.FontWeight.BOLD,
                                           #    foreground=ft.Paint(
                                           #        gradient=ft.PaintLinearGradient(
                                           #            (0, 20), (150, 20), [
                                           #                ft.colors.BROWN, ft.colors.BROWN_200]
                                           #        )
                                           #    ),
                                       ),
                                       ),
                           ],
                ),
                Container(height=20),
                Row(
                    [Init_t,
                     ElevatedButton("Enviar", on_click=sbm_clicked, icon="Input")]
                ),
                # Container(height=20),
                # Row(controls=[plot_graph(counter, icp_points, element)],
                #     ),
            ],
        ),
    )

    # Rest of the code remains unchanged
    page_1 = Container()
    page_2 = Row(controls=[
        Container(
            width=400,
            height=750,
            bgcolor=GREEN,
            border_radius=35,
            padding=padding.only(
                top=50,
                left=20,
                right=20,
                bottom=5
            ),
            content=Column(
                controls=[
                    first_page_contents
                ]
            )
        )
    ]
    )

    container = Container(
        width=400,
        height=750,
        bgcolor=GREEN,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
