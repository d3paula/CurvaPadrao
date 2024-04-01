import flet
import json
from flet import *
from tools.aesthetic.colors import *

##
##  DataTable Construction dummy_test
##
column_names=["Elemento","P1","P2","P3","P4","P5"]
column_widths = [80, 80, 80, 80, 80, 80]  # Adjust the width values as needed
dummy_data: dict = {
                        0: {
                            "Elemento": "P",
                            "P1": 0.5,
                            "P2": 0.0,
                            "P3": 0.0,
                            "P4": 0.0,
                            "P5": 1.5
                        },
                        1: {
                            "Elemento": "Al",
                            "P1": 0.2,
                            "P2": 0.0,
                            "P3": 0.0,
                            "P4": 0.0,
                            "P5": 2.3
                        },
                        2: {
                            "Elemento": "Si",
                            "P1": 0.25,
                            "P2": 0.0,
                            "P3": 0.0,
                            "P4": 0.0,
                            "P5": 1.32
                        },
                        3: {
                            "Elemento": "Ge",
                            "P1": 0.5,
                            "P2": 0.0,
                            "P3": 0.0,
                            "P4": 0.0,
                            "P5": 1.5
                            }
                    }    

################################################################
######################## FUNCTIONS #############################
################################################################

def table_box(control: DataTable):
    return Container(width=900,
                     padding =0,
                     bgcolor = colors.with_opacity(0.65,PAGE_MAIN),
                     border = border.all(2,'transparent'),
                     border_radius = border_radius.only(top_left=10,top_right=10),
                     shadow = BoxShadow(
                                        spread_radius = 8,
                                        blur_radius = 5,
                                        color=colors.with_opacity(0.2,SEARCH),
                                        offset=Offset(0,0)
                                        ),
                                    
                     content=Column(
                                    expand=True,
                                    controls=[
                                                control
                                     ]
                         )
     )
           
def text_box():
    return TextField(
                height=40,
                border=InputBorder.OUTLINE,
                content_padding=padding.only(bottom=0,top=0,right=15,left=15),
                cursor_color=GRAY,
                cursor_width=1,
                cursor_height=18,
                text_size=13,
                color=BLACK,
                value=""
                )
    
def inside_box(expand: bool | int, name: str, control: TextField) -> Container:
    return Container(height=60,
                     width=150,
                     bgcolor=SEARCH,
                     padding=padding.only(top=10, bottom=10),
                     content=Column(
                                    expand=expand,
                                    spacing=1,
                                    controls=[
                                                Text(
                                                    value=name,
                                                    size=12,
                                                    color=BLACK,
                                                    weight="bold",
                                                ),
                                                control                                    
                                                ]
                                )
                        )
    
def save_json(data: dict, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file)
        
def read_json(filename: str)->dict:
  with open(filename,'r') as file:
    dummy_data: dict=json.load(file)
  return dummy_data
    
def read_save_data(filename : str|dict)->dict:
        
        if isinstance(filename,dict):
            my_data =  filename 
            save_json(my_data,'./data/pdata_json.txt')
            return my_data
        else:
            my_data =  read_json(filename) 
            return my_data      

class control_items:
        
        items = read_save_data(dummy_data) 
        count : int = len(items)         
        @staticmethod
        def get_items ():
            return control_items.items
    
        @staticmethod
        def add_items (data: dict)-> None:
            control_items.items[control_items.count]=data
            control_items.count+=1
    
class Header(Container):
    def __init__(self,dt: DataTable):
        super().__init__(on_hover=self.toggler_search)
        
        self.search_value: TextField = self.element_search_field(self.filter_rows)
        self.search: Container = self.element_search_bar(self.search_value)
        self.title: Any = Text("Curva Padrao",color='white')
        self.Userava=IconButton("person")
        self.dt: DataTable=dt
        self.content= Container(
                                    height=60,            
                                    width=900,
                                    bgcolor=TABLE_HEADER,
                                    border_radius=border_radius.only(top_left=10, top_right=10),
                                    padding=padding.only(left=20, right=20),
                                    content=Row(
                                                alignment="SpaceBetween",
                                                controls=[self.title, self.search, self.Userava]
                                            )
                                )
        
    def toggler_search(self, e: HoverEvent):
        self.search.opacity=1 if e.data=="true" else 0.5
        self.search.update()
        
    def element_search_field(self,function:callable) -> TextField:
        return TextField(
            border_color='transparent',
            height=20,
            text_size=14,
            content_padding=0,
            cursor_color=WHITE,
            cursor_width=1,
            color=WHITE,
            hint_text='Buscar Elemento',
            hint_style= TextStyle(size=12,color=WHITE),
            on_change=function,           
        )
    def element_search_bar(self,control:TextField):
        return Container(
            width=350,
            bgcolor='white10',
            border_radius=6,
            opacity=0,
            animate_opacity=300,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment="center",
                controls=[
                    Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85
                    ),
                    control,
                ]
            )       
        )
     
    def filter_rows(self, e) -> None:
        for data_rows in self.dt.rows:
            data_cell = data_rows.cells[0]
            data_rows.visible = (True if e.control.value.lower() in data_cell.content.value.lower() else False)
            data_rows.update()
                              
class Title(Container):
    def __init__(self,dt: DataTable):
        
        super().__init__()
        self.dt: DataTable = dt
        self.content= Column(
            expand=True,
            controls=[
                        Container(
                                    height=40,
                                    width=900,
                                    bgcolor=TABLE_HEADER,
                                    padding=padding.only(left=20,right=20),
                                    border=border.all(2, BLACK),
                                    border_radius = border_radius.only(top_left=10,top_right=10),
                                    content=Column(
                                                    spacing=0,
                                                    alignment="center",
                                                    horizontal_alignment="center",
                                                    controls=[
                                                        Text(
                                                            value="Tabela de Valores de P1 e P5 para o Elementos",
                                                            size=18,
                                                            color=WHITE,
                                                            weight="bold"
                                                        ),
                                                        Container(height=4)
                                                    ]
                                                )
                                            )
            ]
        )
                                  
class PForms(Container):
    def __init__(self,dt: DataTable):
        
        super().__init__()
        self.dt: DataTable = dt
        ### Setting p1 and p5 text areas
        self.p1_box_value: TextField = text_box()
        self.p5_box_value: TextField = text_box()
        
        ### Creating the p1 and p5 boxes
        
        self.p1_box: Container = inside_box(True, "Valor de P1", self.p1_box_value)
        self.p5_box: Container = inside_box(True, "Valor de P5", self.p5_box_value)
        
        ### Setting the Submit Button(Adicionar)
                     
        self.submit=Container(ElevatedButton(text="Adicionar",style=ButtonStyle(shape={"": RoundedRectangleBorder(radius=10)}), on_click=self.add_p1p5))
        self.save=Container(ElevatedButton(text="Salvar",icon='SAVE_AS_ROUNDED',style=ButtonStyle(shape={"": RoundedRectangleBorder(radius=10)}), on_click=self.add_p1p5))


        # Creating TextBox: Choosing the element to construct the Standard Curve
        self.element_value : TextField = text_box()
        self.element= inside_box (True, "Símbolo do Elemento", self.element_value)

        self.content = Column(
                                expand=True,
                                alignment = 'center',
                                horizontal_alignment='center',
                                controls=[
                                                    Container(
                                                        height=100,
                                                        width=900,
                                                        border_radius= 15,
                                                        border=border.all(1,BLACK),
                                                        bgcolor=SEARCH,
                                                        padding=padding.only(left=10, right=10),

                                                        content=Row(                                                
                                                                        alignment="SpaceBetween",
                                                                        controls=[self.element,self.p1_box,self.p5_box,self.submit, self.save]
                                                                    )
                                                                
                                                    )
                                            ]
                            )
                                   
                
    def add_p1p5(self,e: TapEvent):
        data: dict ={
            "Elemento" : str(self.element_value.value).strip(),
               "P1" : float(self.p1_box_value.value),    
               "P2" : 0,
               "P3" : 0,
               "P4" : 0,
               "P5" : float(self.p5_box_value.value) 
        }
        control_items.add_items(data)
        self.clear_input(e)
        self.dt.fill_table()
        self.page.update()
        
    def clear_input(self,e):
        self.element_value.value=''
        self.p1_box_value.value=''
        self.p5_box_value.value=''
        self.content.update()  
    
    
    ##### FALTA #######
    # def remove_element #### Remover elemento para cadastrar um novoe e fazer um botao pra isso 
    
    # def save_firebase #### Salvar arquivo de p1 e p5 para os elementos em pdf, excel e enviar para o firebase database    

#################################                
########### Classes #############
#################################
             
class datatable(DataTable):
    def __init__(self) -> None:
        
        super().__init__(width=900,
                         border_radius = 12,
                         border = border.all(2,BLACK),
                         column_spacing=50,
                         horizontal_lines = border.BorderSide(2,SEARCH),
                         vertical_lines = border.BorderSide(2,SEARCH),                                  
                         columns = [DataColumn(Text(index, size=12, color=BLACK, weight="bold",width=width),numeric=True if index!="Elemento" else False) for index, width in zip(column_names,column_widths) 
                                   ]
                        )
        
        self.df= control_items.get_items()
            
    def fill_table(self):
        self.rows=[]
        for values in self.df.values():
            data = DataRow()
            data.cells = [
                DataCell(Text(value,size=12,color=BLACK)) for value in values.values()
            ]
            self.rows.append(data)
            
    def is_in_table(filename : str|dict, value: str) -> bool|list:
        table: dict=read_save_data(filename)
        values=[]
        for keys, row in table.items():
            if row.get("Elemento")==value:
                v1=row.get("P1",0)
                v5=row.get("P5",0)
                if v1 is not None and v5 is not None:
                    values=[row["Elemento"],v1,v5]
                    return values
        return False
              
class PTable(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.table=datatable()
        self.expand = True
        self.bgcolor = PAGE_MAIN
        self.table=datatable()
        self.header: Container= Header(dt=self.table)
        self.forms: Container= PForms(dt=self.table)
        self.title=Title(dt=self.table)
        self.dtable=table_box(self.table)
        self.content=Column(
                        expand=True,
                        alignment='center',
                        scroll='hidden',
                        horizontal_alignment='center',
                        spacing=0,
                        controls=[  self.header,
                                    Divider(height=2, color="transparent"),
                                    self.forms,
                                    Divider(height=6, color="transparent"),
                                    self.title,
                                    self.dtable
                                ]
                    )
        self.table.fill_table()
        