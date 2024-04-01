from flet import *
import numpy as np
import matplotlib.pyplot as plt
from tools.aesthetic.colors import *

#
# Setting up the Container
#

class PlotValues():
   
   def__init__(self):
     super().__init__()
   
   def plot_rtime(self,narray: numpy.ndarray) 
   
   def getvalue_(self,number):
    
    global numbers=np.array([]) #Catching the numbers as numpy array and make them global
    inpnum=float(number)
    
    try:
      numbers=np.append(inpnum)
      plot_rtime(numbers)
      return numbers
    except Error:
      print('Você escreveu um número inválido')
      
    def save_plot(self, narray: np.ndarray, destination: str, form_as: str) -> None:
      if form_as == '.pdf':
        # Save plot as PDF
        plt.plot(narray)
        plt.savefig(destination, format='pdf')
        plt.close()  # Close the plot
      elif form_as == '.xlsx':
        # Save plot as Excel
        wb = Workbook()
        ws = wb.active
        for i, value in enumerate(narray):
                  ws.cell(row=i+1, column=1, value=value)
              wb.save(destination)
      elif form_as == '.png':
        # Save plot as Excel
        plt.plot(narray)
        plt.savefig(destination, format='png')
        plt.close()
      else:
        raise ValueError("Unsupported format. Supported formats are '.pdf' and '.xlsx'.")def save_plot(self,narray: numpy.ndarray, destination: str, form_as: str)->document.form_as:
        
        
    
      
    
    
  
  