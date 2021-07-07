import datetime
import time
import os

def horario():
        while True:
             now = datetime.datetime.now()
             horas = now.strftime("%H:%M")
             os.system('cls' if os.name == 'nt' else 'clear')
             print(horas)
             time.sleep(60)   

             
        
      
