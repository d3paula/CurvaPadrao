import flet
from flet import *
from tools.aesthetic.colors import *

def all_app():
    return Row()
def card_gadget(text: str, imagesrc: str, route: str):
    return Card(
        elevation=30,
        content=Container(
            width = 160,
            height = 160,
            padding = 5,
            bgcolor=BLACK,
            border_radius = border.symmetric(vertical=border.BorderSide(5,"blue")),
            on_click=route
            content=Column([
                Image(
                    src = imagesrc,
                    width = 120,
                    height = 120,
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

def open_app(self,e,route):
    if e.data == True:
        self.page.go(route)
 
def box_app_icon():
    return Container(
        width = 900,
        padding = 10,
        bgcolor=WHITE,
        border_radius = border.radius.all(30),
        border_width = 3,
        content=Column(
            alignment = 'center',
            horizontal_alignment = 'center',
            controls=[
            ]
        )
    )

def alert_app_icon(self,e):   ### Tour pelo App
    if e.data==True:
        self.card_gadget.border_radius = border_radius.symmetric(vertical=border.BorderSide(5,"red"))
  #tour border will be used 

def return_to_main():
    pass

class tour:
    def __init__(self,e):
        super.__init__(self)
        self.apps=len(apps)
        self.step=number
        self.current_step=0
    def show_info(self,count):
        self.message={
            {"0": "No gerar curva você poderá gerar o gráfico da curva padrão e obter o fitting e caso escolha a análise de P1 e P5 você poderá obter uma curva mostrando se seu valor de P1 e P5 está dentro dos limites"},
            {"2":"No Valores de P1 e P5 você poderá cadastrar os valores de P1 e P5 para um determinado átomo. Aqui é possível cadastrar dois parâmetros para o mesmo átomo (Exemplo: Ca_low e Ca_high)de modo que você possa acessá-los novamente em outras análises"},
            {"3": "Em Gráficos e Tabelas você poderá visualizar os últimos 10 relatórios contendo os gráficos e trabelas das suas últimas análises. Caso necessite dos gráficos e tabelas que não foram mostrados é só fazer uma busca na aba procurar"
            },
            {"4": "O Cálculo de Diluição permite que você insira sua concentração inicial e cálcule qual seria a diluição a ser realizada"
            },
            {"5": "No botão Perguntas Frequentes você poderá encontrar um arquivo mostrando quais são as respostas para a maioria das perguntas que você poderá encontrar utilizando o aplicativo"
            },
            {"6": "No Logout você poder sair do aplicativo e voltar para a tela de login. Obs: Caso saia sem salvar seus arquivos você poderá perdê-los!"
            }
        }
        
        def Touring(self,e):
            count=0
            for count in range(len(self.apps)):
                if e.data==True:
                    show_info(count) ### Chart explaining the functionalities
                    self.page.splash=ProgressRing()
                    time.sleep(10)
                    self.page.splash=None
                    self.apps[count].border_radius=border.symmetric(vertical=border.BorderSide(5,"blue"))

                    self.page.update()
 
              

class Gadgets(Container):
    def __init__(self,page: Page) -> None:
        super().__init__()
        self.expand=True
        self.bgcolor=BLACK,
        self.page=page 
        self.content=Column(
            expand=True,
            controls=[
                Row(alignment='center',controls=[card_gadget("Gerar Curva",imagesrc='/images/GerarCurva.jpg',route="/ptable"),card_gadget("Arquivos salvos")",imagesrc='/images/Arquivos.jpg',route="/login")]),
                Row(alignment='center',controls=[card_gadget("Gerar Curva",imagesrc='/images/GerarCurva.jpg',route="/mainpage"),card_gadget("Arquivos salvos")",imagesrc='/images/Arquivos.jpg',route="/logout")]),
            ]
        )
            
##### Four gadgets with adjustable size of icon since should be add more icons later
### Gerar Curva (Tela com botao adicionar ponto, mostra gráfico e tabela caso o usuário click numa checkbox)
### Valores P1-P5 (PTable)
### Gráficos e Tabelas (Mostra os últimas 10 pastas com nome CP_data_codigoanalise_nomeusuario)
### Calcular Diluição (Faz o cálculo das diluições para cada metal)

### Tour pelo App aparecerá como sugestão para o usuário na barra superior pulsando
### durante os primeiros 10 s caso não clicado para de pulsar

