import pyrebase 
import os
import firebase_admin
import pickle
import requests
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials,db
from flet import *
from tools.aesthetic.colors import *
from tools.Validator.Validator import Validation

class FirebaseDBManager:
    def __init__(self):
        #
        # Authorization Login and Signup
        #
        self.cred = credentials.Certificate('serviceaccount.json')
        self.firebase_admin=firebase_admin.initialize_app(self.cred,{"databaseURL":"https://curvapadrao-default-rtdb.firebaseio.com/"})
        self.firebase_apiKey ="AIzaSyBpv1Lbp89ldWGjrulwK9p2mxYIBsMcMQc"

class Signup(Container):
    def __init__(self, page: Page):

        super().__init__()
        self.expand = True
        self.bgcolor = BG
        self.validator = Validation()
        self.firebaseDB = FirebaseDBManager()
        self.error_border = border.all(width=4, color='red')
        self.firebase_auth=firebase_auth
        
        # Name Box
        self.name = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color=GRAY,
                ),
                hint_text='Nome Completo...',
                cursor_color=GRAY,
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,

        )

        # Email Box
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color=GRAY,
                ),
                hint_text='Endereço de email example@gmail.com ...',
                cursor_color=GRAY,
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,
        )
        # Password Box
        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color=GRAY,
                ),
                hint_text='Senha ...',
                cursor_color=GRAY,
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
                password=True,

            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,

        )

        # Aligning the Components

        self.alignment = alignment.center

        # Declaring Components

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[Container(
                width=500,
                padding=40,
                bgcolor=WHITE,
                content=Column(
                    horizontal_alignment='center',
                    controls=[
                        Text(
                            value='Bem-Vindo ao Curva Padrão',
                            size=16,
                            color='black',
                            text_align='center'
                        ),
                        Container(height=10),
                        self.name,
                        self.email_box,
                        self.password_box,
                        Container(height=10),

                        # Container Space Between boxes and buttons

                        Container(height=1),

                        # Container Click Login

                        Container(
                            alignment=alignment.center,
                            bgcolor=FG,
                            height=40,
                            border_radius=30,
                            content=Text(
                                value='Signup',
                                color='white'
                            ),
                            on_click=self.signup
                        ),
                        # Container Click ForgotPassword

                        Container(
                            content=Text(
                                value='Esqueceu a senha?',
                                color=BG,
                                size=12,
                            ),
                            on_click=lambda _:self.page.go('/forgotpassword')
                        ),
                        # Container Click Create New Account
                        Container(
                            content=Text(
                                value='Já possui uma conta? Então entre',
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

    def signup(self, e):
        if not self.validator.is_correct_name(self.name.content.value):
            self.name.border = self.error_border
            self.name.update()
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()
        else:
            email=self.email_box.content.value
            name=self.name.content.value
            password=self.password_box.content.value
            self.page.splash=ProgressBar()
            self.page.update()
            userUID=self.create_user(name,email,password) #creating user
            securecheck=self.response_secure_token(email,password) #checking user POST
            self.page.splash=None
            self.page.update()
    
            #Checking the correct creation and connection of the new account                   
            if securecheck==200 and userUID is not None :
                
                self.page.snack_bar=SnackBar(
                    Text(
                        "Conta criada com sucesso!"
                    )
                )
                self.page.snack_bar.open=True
                self.page.update()

                self.page.go('/login')


            else:
                self.page.snack_bar=SnackBar(
                    Text(
                        "Credenciais Invalidas"
                    )
                )
                self.page.snack_bar.open=True
                self.page.update()

        
    
    def create_user(self,name, email, password):
        try:
            user = self.firebase_auth.create_user(
                email=email,
                password=password,
                display_name=name
            ) 
            print("Conta criada com Sucesso")
            return user.uid
        except:
            return None
        
    def response_secure_token(self,email, password):
        url=f"https://identitytoolkit.googleapis.com//v1/accounts:signInWithPassword?key= {self.firebaseDB.firebase_apiKey}"
        data={
            "email":email,
            "password":password,
            "returnSecureToken":True
            }
        response=requests.post(url,json=data)
        print(response)
        if response.status_code == 200:
            print("POST request was successful.")
            json_response=response.json()
            token=json_response['idToken']
            print(f'IDToken:{token}')
            verify=self.firebase_auth.verify_id_token(token)
            print(verify)
        else:
            raise Exception(f'Error:{response.status_code}')
        return response.status_code

                    
   
