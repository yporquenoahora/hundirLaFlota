from utils import Jugador
from const import barcos, barcosNum
import numpy as np

class Game: 
    turno = True # Si es True el turno es del jugador, si es False es el turno de la máquina
    status = True # On/Off

    def __init__(self, maquina: Jugador, jugador: Jugador): # Tipo el argumento para que quede fijo
        self.maquina = maquina
        self.jugador = jugador  

    def salir(self,exit_word:str): # Función para salir
        if exit_word.replace(" ","").lower() == "salir" or exit_word.replace(" ","").lower() =="no":
            print("\n","Esperábamos más de ti, grumete, pero se ve que no tenías la valía necesaria.","\n")
            quit()  # TODO implementar un ¿estas seguro? si-> salir/no-> continuar
            
    # def reiniciar(self): # TODO Función para reiniciar


    def jugar (self):
        tamTablero = 10 # Ambos tienen las mismas dimensiones de tablero. ## Podriamos ponerlo en cnts para que quede mas limpio
        
        print("* Generando tableros y desplegando la flota... *","\n")

        self.jugador.initTablero()
        self.maquina.initTablero()
        for i, v in barcosNum.items():    
            self.jugador.colocarBarcos(i,v)
            self.maquina.colocarBarcos(i,v)
 
        
        while self.status: #  while True
            if self.turno:  
                # TURNO/LOGICA DEL JUGADOR: 
                # 1. coordenadas? > disparo
                # 2. feedback despues del impacto > jugador.getDisparo()
                # 3. si agua: turno = False ; si impacta: continue or fin = True
                
                print("\n", f"Es tu turno, {self.jugador.nombre}","\n", self.jugador.mostrarTablero(), self.jugador.mostrarImpactos())
                print("- Capitán Sardino: Y bien grummete, ¿hacia donde disparamos?.","\n")
                x = input("Coordenada del eje x (A a J):")
                self.salir(x)
                y = input("Coordenada del eje y (1 a 10):") 
                self.salir(y)

                print("\n","* Disparando a la flota enemiga...*","\n")

                res = self.jugador.getDisparo(x,y)    # Reemplaza coordenada y actualiza tablero_impactos
                if res == "-": # Si dispara en agua
                    self.turno = False
                    print("\n","* Fallo *","\n")
                    print("\n","-Capitán Sardino: Fallamos!, arr. Más al loro grumete!")
                
                elif res == "fin de juego": # Si todo los bascos enemigos se hunden
                    self.status = False
                    print("\n","* Impacto *","\n")
                    print("\n","Barco tocado y hundido", "\n\n", "-Capitan Sardino: HurraAaAa! Hemos vencido!", "\n")
                    print("Victoria magistral. Todos los barcos de la flota enemiga han sido derrotados.")
                    break
                else: # Si impacta a un barco
                    print("\n","* Impacto *","\n") 
                    print("\n","-Capitan Sardino: por las barbas de Neptuno. Buen disparo!")
                    continue

                
            else:
                # TURNO/LOGICA DE LA MAQUINA: 
                # 1. coordenadas aleatorias sin repetir (verifica que no haya nada en la coordenada de tablero_imapctos) > disparo
                # 2. feedback despues del impacto > jugador.getDisparo()
                # 3. si agua: turno = False ; si impacta: continue or fin = True -> Y actualiza tablero


                print("\n", f"Ahora es el turno de {self.maquina.nombre}")

                while self.turno == False: 
                    x = np.random.randint(10)
                    y = np.random.randint(10)
                    while self.maquina.tablero_impactos[x,y] != " ":
                        x = np.random.randint(10)
                        y = np.random.randint(10)
                    
                    print("\n","* Barco enemigo disparando... *","\n")

                    res = self.maquina.getDisparo(x,y)      # Reemplaza coordenada y actualizar tablero_impactos ??
                    if res == "-": # Si dispara en agua
        
                        self.turno = True
                        print("\n","* Fallo *","\n")
                        print("\n","-Capitán Sardino: Fallaron!, arr.")
                       
                    elif res == "fin de juego":  # Si impacta a un barco
                        
                        self.status = False
                        print("\n","* Impacto *","\n\n","Barco tocado y hundido.","\n")
                        print("\n","Derrota aplastante. Todos los barcos de tu flota se han ido a pique...")
                        print("\n","- Capitán Sardino: Gluglugluglu...","\n")
                        break
                    else:
                        
                        print("\n","* Impacto *","\n")
                        print("\n","- Capitán Sardino: Ouch!","\n")
                        continue
                    
                    
                    