from flet import *
from tools.aesthetic.colors import *
from tools.Validator.Validator import Validation


# def Sendmail(self,envemail,recemail,Message):
    
    

class ForgotPassword(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = BG
        self.validator = Validation()

        self.error_border = border.all(width=4, color='red')

        self.alignment = alignment.center
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color=GRAY,
                ),
                hint_text='Adicione Email para recuperação de senha',
                cursor_color=GRAY,
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,
        )
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(width=500,
                          border_radius=30,
                          padding=40,
                          bgcolor='white',
                          content=Column(
                              alignment='center',
                              horizontal_alignment='center',
                              controls=[
                                  Text(
                                      value='Você esqueceu sua senha?',
                                      size=24,
                                      color='black',
                                      text_align='center'
                                  ),
                                  Text(
                                      value='Acontece com todos nós! Coloque seu email para que possamos enviar um link para resetar sua senha!',
                                      size=16,
                                      color='black',
                                      text_align='center'
                                  ),
                                  Container(height=1),
                                  self.email_box,

                                  # Container Click Reset

                                  Container(
                                      alignment=alignment.center,
                                      bgcolor=FG,
                                      height=40,
                                      border_radius=30,
                                      content=Text(
                                          value='Reset Senha',
                                          color='white'
                                      ),
                                      on_click=self.reset_password
                                  ),
                                  Container(height=1),

                                  # Container Click ForgotPassword

                                  Container(
                                      content=Text(
                                          value='Criar nova conta',
                                          color=BG,
                                          size=12,
                                      ),
                                      on_click=lambda _:self.page.go('/signup')
                                  ),
                                  # Container Click Create New Account
                                  Container(
                                      content=Text(
                                          value='Já possui uma conta? Então entre!',
                                          color=BG,
                                          size=12,
                                      ),
                                      on_click=lambda _:self.page.go('/login')
                                  ),


                              ]

                          )
                          ),
            ]
        )

    def reset_password(self, e):
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
        pass
