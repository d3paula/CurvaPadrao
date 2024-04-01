import flet
import pickle
from flet import *
from pages.Login import Login 
from tools.aesthetic.colors import *

#########################################
############## FUNCTIONS ################
#########################################
def get_signed_email(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def card_gadget(page: Page, text: str, imagesrc: str, route: str):
    return Card(
        elevation=30,
        content=Container(
            width = 200,
            height = 210,
            padding = 5,
            bgcolor=WHITE,
            border=border.all(2,"BLUE"),
            border_radius = border_radius.only(top_left=10,top_right=10,bottom_left=10,bottom_right=10),
            on_click=lambda _: page.go(route),
            content=Column([
                Image(
                    src = imagesrc,
                    width = 160,
                    height = 160,
                    border_radius=border_radius.all(30),
                    fit=ImageFit.CONTAIN
                ),
                Text(
                   value=text,
                   size=16,
                   weight="bold",
                   width=150,
                   text_align=TextAlign.CENTER,
                    
                )], alignment="center", horizontal_alignment='center',
            )
        )
    )
 
def box_app_icon():
    return Container(
        width = 900,
        padding = 10,
        bgcolor="transparent",
        border_radius = border.radius.all(30),
        border_width = 3,
        content=Column(
            alignment = 'center',
            horizontal_alignment = 'center',
            controls=[
            ]
        )
    )

# def onclick_question(self,e: TapEvent):
#     if e.data == True:
#         self.page.go("/question") #Open page of frequently questions

# def onclick_person(self,e: TapEvent):
#     if e.data == True:
#         self.page.go("/question") #Open page of frequently questions
    
def alert_app_icon(self,e):   ### Tour pelo App
    if e.data==True:
        self.card_gadget.border_radius = border_radius.symmetric(vertical=border.BorderSide(5,"red"))
  #tour border will be used 

def return_to_main():
    pass

################################################################
####################### CLASSES ################################
################################################################

class show_info:
        def __init__(self) -> None:
            self.message: dict ={
                "0": "No gerar curva você poderá gerar o gráfico da curva padrão e obter o fitting e caso escolha a análise de P1 e P5 você poderá obter uma curva mostrando se seu valor de P1 e P5 está dentro dos limites",
                "1":"No Valores de P1 e P5 você poderá cadastrar os valores de P1 e P5 para um determinado átomo. Aqui é possível cadastrar dois parâmetros para o mesmo átomo (Exemplo: Ca_low e Ca_high)de modo que você possa acessá-los novamente em outras análises",
                "2": "Em Gráficos e Tabelas você poderá visualizar os últimos 10 relatórios contendo os gráficos e trabelas das suas últimas análises. Caso necessite dos gráficos e tabelas que não foram mostrados é só fazer uma busca na aba procurar",
                "3": "O Cálculo de Diluição permite que você insira sua concentração inicial e cálcule qual seria a diluição a ser realizada",
                "4": "No botão Perguntas Frequentes você poderá encontrar um arquivo mostrando quais são as respostas para a maioria das perguntas que você poderá encontrar utilizando o aplicativo",
                "5": "No Perfil você poderá consultar qual usuário está logado e poderá sair do aplicativo e voltar para a tela de login. Obs: Caso saia sem salvar seus arquivos você poderá perdê-los!"
                
            }    
        def get_message(self,key):
            return self.message.get(key)
        def print_message(self,key):
            info = show_info()
            message = info.get_message(key)
            print(message)
            
def tour_click(event):
    pass      

def tour_hover(event):
    pass

def person_open(e):
    print(f"{e.control.content.value}.on_click")
def person_hover(event):
    pass

def question_click(event):
    pass         
                
        
class Gadgets_Area(Container):
    def __init__(self,page: Page):
        super().__init__(self)
        self.page=page

        
        ### Cards Gadgets ###
        self.diluicao=card_gadget(self.page,"Diluicao",'/images/Diluicao.jpg',"/signup")
        self.tabelap1p5=card_gadget(self.page,"Tabela P1 e P5",'/images/TabelaP1P5.jpg',"/mainpage")
        self.gerarcurva=card_gadget(self.page,"Gerar Curva",'/images/GerarCurva.jpg',"/ptable")
        self.arquivossalvos=card_gadget(self.page,"Arquivos salvos",'/images/Arquivos.jpg',"/login")
        
        ### Rows ###
        self.row1= Row(spacing=30,alignment='center',controls=[self.gerarcurva, self.arquivossalvos])
        self.row2= Row(spacing=30,alignment='center',controls=[self.tabelap1p5, self.diluicao])
        
        ### Structure for Gadgets ###
        self.content=Container(
            width=500,
            padding=0,
            shadow=BoxShadow(
                spread_radius = 2,
                blur_radius = 5,
                color=colors.with_opacity(0.2,WHITE),
                offset=Offset(0,0)),   
            bgcolor="transparent",
            content=Column(
                alignment='center',
                horizontal_alignment='center',
                controls=[
                    self.row1,
                    Container(height=5),
                    self.row2,
                ]
            )
        )
        
class Gadgets(Container):
    def __init__(self,page: Page) -> None:
        super().__init__()
        self.expand=True
        self.bgcolor=BG
        self.page=page
        self.error_border = border.all(width=4, color='red')
        self.Gadgets_Area=Gadgets_Area(self.page)
        self.Appbar=AppBar(self.page)
        self.info=show_info()
        self.signed=get_signed_email('./email.pickle')
        self.boxfrequentq=SubmenuButton(
                
                            content=Row([
                                Icon(name=icons.QUESTION_MARK),
                                Text("Perfil")]
                            ),
        )
        self.boxtour=SubmenuButton(
                
                            content=Row([
                                Icon(name=icons.TOUR),
                                Text("Perfil")]
                            ),
        )
        self.boxperson=SubmenuButton(
            content=Row([
                Icon(name=icons.PERSON),
                Text("Perfil")]
            ),
                                
            controls=[
                MenuItemButton(
                    content=Text(f'Usuário: {self.signed}',size=14,color="black"),
                    ),
                MenuItemButton(
                    content= Text(disabled=False, size=14,color="blue",spans=[TextSpan("Sair",on_click=lambda e: self.page.go("/login"))]),
                )                   
            ]
        )
        self.menu=Container(
            width=500,
            height=50,
            content=MenuBar(
                style=MenuStyle(
                    bgcolor=PAGE_MAIN,
                    padding=padding.only(left=10, right=10),
                ),
                controls=[ Row(
                    spacing=100,
                    controls=[self.boxfrequentq,
                            self.boxtour,
                            self.boxperson])
                    ]
            )
        )

        self.content=Column(
            expand=True,
            alignment='center',
            horizontal_alignment='center',
            spacing=0,
            controls=[
                self.menu,
                Divider(height=10, color="transparent"),
                self.Gadgets_Area
            ]
         )
    
    ##### If the user hovers on Tour it shows the Tooltip if the user clicks on it the buttons will show 
    