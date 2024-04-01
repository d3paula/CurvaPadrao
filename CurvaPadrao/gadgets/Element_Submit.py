from flet import *
from tools.aesthetic.colors import *
from gadgets.PTable import datatable 
from tools.Validator.Validator import Validation
import time

class MainPage(Container):
    def __init__(self, page: Page):

        super().__init__()
        self.expand = True
        self.bgcolor = GREEN
        self.validator = Validation()
        page.fonts={"NEXA":"https://db.onlinewebfonts.com/t/3fe2115b5af4c997012cc8131973d9d1.eot"}

        self.error_border = border.all(width=4, color='red')
        self.menu=Icon(icons.MENU)
        self.search_icon=Icon(icons.SEARCH)
        self.notification=Icon(icons.NOTIFICATIONS_OUTLINED)
        self.help=Icon(icons.HELP_OUTLINE_ROUNDED)
        
        # Corners Elements
        self.corners = Container(
            content=Column(
                controls=[
                    Row(alignment='SpaceBetween',
                        controls=[
                            Container(
                                content=self.menu),
                            Row(
                                controls=[
                                    self.search_icon,
                                    self.notification,
                                    self.help,
                                ],
                            ),
                        ],
                        ),
                    Container(height=1),
                ],
            )
        )

        # Element Box
        self.element = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color=GRAY,
                ),
                hint_text='Símbolo do Elemento Químico...',
                cursor_color=GRAY,
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,
        )

        # Aligning the Components
        self.alignment = alignment.center

        # Declaring Components

        # Setting up the Element Box
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    padding=40,
                    bgcolor=WHITE,
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            self.corners,
                            Container(height=10),
                            Text(
                                value='Curva Padrão',
                                size=22,
                                color='black',
                                weight="bold",
                                text_align='center',
                                font_family="NEXA"
                            ),
                            Container(height=10),
                            self.element,
                            Container(height=10),
                            # Container Click Login
                            Container(
                                alignment=alignment.center,
                                bgcolor=DGREEN,
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Submeter',
                                    color='white'
                                ),
                                # Go to TableView
                                on_click=self.gadgetspage_me
                            ),
                        ]
                    )
                ),
            ]
        )
    
    def gadgetspage_me(self,e):
        
        def symbol_value():
            self.symbol=self.element.content.value
            if self.symbol is None:
                return None
            if not self.validator.is_valid_element(self.symbol):
                return None
            else:
                return self.symbol
        
        
        self.symbol= symbol_value()
        self.value=datatable.is_in_table("./data/pdata_json.txt",self.symbol)

        if self.symbol is None:
            self.page.snack_bar=SnackBar(
                    Text(
                        "Entrada do Símbolo do Elemento Incorreta"
                        )
                )
            self.page.snack_bar.open=True
            self.page.update()
        
        else: 
            if not isinstance(self.value,list):
                print(f'{self.value} valor')
            
                ### Dialog
                self.open_dlg()
                time.sleep(8)
                self.page.go('/ptable')
            else:
                self.dlg_modal= AlertDialog(modal=True, title=Text("Confirmação"),
        content=Text(f"Confirme se os valores de P1 = {self.value[1]} e P5={self.value[2]} para o elemento {self.symbol} está correto?"),
        actions=[
            TextButton("Sim", on_click=self.close_dlg),
            TextButton("Não", on_click=self.close_dlg_no),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
                self.open_dlg_ms()
                time.sleep(8)
                self.page.go('/login')           #### Goes to Features page
                      
                
    def open_dlgmodal(self):
        self.page.dialog = AlertDialog(title=Text(f'Cadastre os valores corretos de P1 e P5 do elemento!'), bgcolor='yellow', shape={"":BeveledRectangleBorder(radius=8)},
 on_dismiss=lambda e: print("Xau brigado!"))                        
        self.page.dialog.open = True
        self.page.update()
        
    def open_dlg(self):
        self.page.dialog = AlertDialog(title=Text(f'Elemento não cadastrado! Você será redirecionado em alguns segundos para adicionar e salvar o elemento e seus valores de P1 e P5 deste elemento'), bgcolor='yellow', shape={"":BeveledRectangleBorder(radius=4)},
 on_dismiss=lambda e: print("Xau brigado!"))                        
        self.page.dialog.open = True
        self.page.update()
    
    def close_dlg(self,e):
        self.dlg_modal.open = False
        self.page.update()

    def close_dlg_no(self,e):
        self.dlg_modal.open = False
        self.open_dlgmodal()
        time.sleep(2)
        self.page.update()
        self.page.go('/ptable')           #### Goes to Features page
        
    def open_dlg_ms(self):
        self.page.dialog=self.dlg_modal            
        self.page.dialog.open = True
        self.page.update()
            