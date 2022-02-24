# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication
#from interface import Window

class beautycontest:
    #Constructeur
    def __init__(self,values=[50,100,75]):
        #self.round_duration = 10
        self.values = values
        ##self.init_contest()
        
    def mean(self):
        total_value = 0
        nb_values = 0
        i=0
        while i < len(self.values):
            total_value += self.values[i]
            nb_values += 1
            i+=1
        #print("Moyenne : ", total_value/nb_values)
        return total_value/nb_values
    
    def winner(self, p):
        j=1
        while j <= len(self.values):
            print("J",j," chose :", self.values[j-1])
            j += 1
        
        mean_value_p = self.mean() * p
        print("Mean is :", mean_value_p)
        gap = abs(self.values[0] - mean_value_p)
        #print("gap :", gap)
        winner_nb = 0
        i=0
        while i < len(self.values):
            if (gap > abs(self.values[i] - mean_value_p)) & (i!=0):
                gap = abs(self.values[i] - mean_value_p)
                #print("gap :", gap)
                winner_nb = i
                
            i+=1
            #print("winner_nb : ", winner_nb)
        #print("Place du gagnant dans le tableau : ", winner_nb)
        return winner_nb
    
    def init_contest(self):
      #How many players ? boucle for + vérif entre 0 et 100
      #pour les input, faire un if (type != int) then "ftg connard"
      print("How many players ?")
      nb_players = int(input())
      i=1
      tabtmp=[None for _ in range(nb_players)]
      while i <= nb_players:
          print("J",i,", votre réponse :")
          tabtmp[i-1] = int(input())
          i += 1
      #tab = beautycontest([50,100,62])
      tab = beautycontest(tabtmp)
      print("So, the winner is J",tab.winner(0.8) +1)
        
if __name__ == "__main__":
    
    print("\nThis is not the main program !!\n")
   
        
    
        
        
        