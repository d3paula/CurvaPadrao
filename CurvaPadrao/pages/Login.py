import pyrebase
import os
import firebase_admin
import pickle
import requests
from firebase_admin import auth as fire_auth
from firebase_admin import credentials,db
from flet import *
from tools.aesthetic.colors import *
from tools.Validator.Validator import Validation

class FirebaseManager:
    def __init__(self):
        #
        # Authorization Login and Signup
        #
        self.firebaseConfig= {
                "apiKey": "AIzaSyBpv1Lbp89ldWGjrulwK9p2mxYIBsMcMQc",
                "authDomain": "curvapadrao.firebaseapp.com",
                "databaseURL": "https://curvapadrao-default-rtdb.firebaseio.com",
                "projectId": "curvapadrao",
                "storageBucket": "curvapadrao.appspot.com",
                "messagingSenderId": "35872367520",
                "appId": "1:35872367520:web:55cff38319c7a7fff0bac5",
                "measurementId": "G-5H7BJW8SYT"
            }
        self.firebase_apiKey ="AIzaSyBpv1Lbp89ldWGjrulwK9p2mxYIBsMcMQc"
        self.firebase_app=pyrebase.initialize_app(self.firebaseConfig)
        self.auth=self.firebase_app.auth()

class Login(Container):

    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = BG
        self.validator = Validation()
        self.error_border = border.all(width=4, color='red')
        self.firebase_manager = FirebaseManager()  # Initialize FirebaseManager instance
    
        # Email Box
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(size=12, color=GRAY),
                hint_text='Adicione email example@gmail.com ...',
                cursor_color=GRAY,
                text_style=TextStyle(size=14, color='black'),
            ),
            border=border.all(width=1, color=GRAY),
            border_radius=10,
        )
        # Password Box
        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(bottom=0, top=0, right=20, left=20),
                hint_style=TextStyle(size=12, color=GRAY),
                hint_text='Adicione sua senha ...',
                cursor_color=GRAY,
                text_style=TextStyle(size=14, color='black'),
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
            controls=[
                Container(
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
                            self.email_box,
                            self.password_box,
                            # Container Space Between boxes and buttons
                            Container(height=1),
                            # Container Click Login
                            Container(
                                alignment=alignment.center,
                                bgcolor=FG,
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Login',
                                    color='white'
                                ),
                                on_click=self.login_me
                            ),
                            # Container Click ForgotPassword
                            Container(
                                content=Text(
                                    value='Esqueceu a senha',
                                    color=BG,
                                    size=12,
                                ),
                                on_click=lambda _: self.page.go('/forgotpassword')
                            ),
                            # Container Click Create New Account
                            Container(
                                content=Text(
                                    value='Criar nova conta',
                                    color=BG,
                                    size=12,
                                ),
                                on_click=lambda _: self.page.go('/signup')
                            ),
                        ]
                    )
                ),
            ]
        )

    def login_me(self, e):
            if not self.validator.is_valid_email(self.email_box.content.value):
                self.email_box.border = self.error_border
                self.email_box.update()
            if not self.validator.is_valid_password(self.password_box.content.value):
                self.password_box.border = self.error_border
                self.password_box.update()
            else:
                email=self.email_box.content.value
                password=self.password_box.content.value
                self.page.splash=ProgressBar()
                self.page.update()
                
            token= self.login_user(email,password)      
            
            self.page.splash=None
            self.page.update()
                     
            if token:
                self.store_token(token)
                self.page.go('/mainpage')
            else:
                self.page.snack_bar=SnackBar(
                    Text(
                        "Credenciais Invalidas"
                    )
                )
                self.page.snack_bar.open=True
                self.page.update()

    def login_user(self,email,password):
        try:
            user= self.firebase_manager.auth.sign_in_with_email_and_password(email, password)
            print("User signed in successfully.")
            print("User ID:", user['localId'])
            print("ID Token:", user['idToken'])
            return user['idToken']       
        except Exception as e:
            print(e)
            return None

    def store_token(self,token):
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
        with open('token.pickle', 'wb') as fb:
            pickle.dump(token,fb)
                            
    def remove_token(self,token):
        self.fire_auth.revoke_refresh_token(token)
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
                    
            