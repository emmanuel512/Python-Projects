#Emmanuel Banjo
#T.A. Stephen Rhein
#Pig Game

from random import*
class PigGame():
    def __init__(self, names, scores, computer, whoseturn):
        self.names = names
        self.scores = scores
        self.computer = computer
        self.whoseturn = whoseturn

    def userplay(self):
        self.printscores()
        round_score = self.scores[self.whoseturn]
        rounds = 0
        lastroll = 0
        x = "yes"
        while  x == "yes":
            dice = randint(1,6)
            if self.scores[self.whoseturn] >= 100:
                self.won()
                return(False)
            if dice == 2:
                print(str(self.names[self.whoseturn]) + ' rolled a ' + str(dice))
                print('You lost your points this round.')
                rounds = 0
                dice = 0
                round_score = 0
                self.whoseturn += 1
                return(self.computerplay())
            if lastroll == 1:
                if dice == 1:
                    print('You got two 1s. All points Gone')
                    rounds = 0
                    dice = 0
                    self.scores[self.whoseturn] = 0
                    self.whoseturn += 1
                    return(self.computerplay())
                if dice == 6:
                    print('Total points double') 
                    self.scores[self.whoseturn] = self.scores[self.whoseturn] * 2
            else:
                round_score+=dice
                self.scores[self.whoseturn] = round_score
            print(str(self.names[self.whoseturn]) + ' rolled a ' + str(dice))
            print(' Current score is ' + str(round_score))
            print(' If ' + str(self.names[self.whoseturn]) + ' stops, total score will be ' + str(self.scores[self.whoseturn]))
            x = input(" do you want to roll again ?")
        if x == "no":
            self.whoseturn += 1
            return(self.computerplay())
      
            
                
            
    def computerplay(self):
        self.printscores()
        round_score = self.scores[self.whoseturn]
        rounds = 0
        lastroll = 0
        print(str(self.names[self.whoseturn]) + ' starting score is ' + str(round_score))
        y = 0
        while y <= 14 :
            dice = randint(1,6)
            if self.scores[self.whoseturn] >= 100:
                self.won()
                return(False)
            if dice == 2:
                print(str(self.names[self.whoseturn]) + ' rolled a ' + str(dice))
                print('Comp1 lost its points round.')
                rounds = 0
                dice = 0
                round_score = 0
                self.whoseturn -= 1
                self.scores
                return(self.userplay())
            if lastroll == 1:
                if dice == 1:
                    print('Comp1 got two 1s. All points Gone')
                    rounds = 0
                    dice = 0
                    self.scores[self.whoseturn] = 0
                    self.whoseturn -= 1
                    return(self.userplay())
                if dice == 6:
                    print('Total points double') 
                    self.scores[self.whoseturn] = self.scores[self.whoseturn] * 2
            else:
                    round_score+=dice
                    self.scores[self.whoseturn] = round_score
            print(str(self.names[self.whoseturn]) + ' rolled a ' + str(dice))
            print(' Current score is ' + str(round_score))
            print(' If ' + str(self.names[self.whoseturn]) + ' stops, total score will be ' + str(self.scores[self.whoseturn]))
            y += randint(1,6)
        if y >= 14:
            print("Comp1 stops")
            self.whoseturn -= 1
            return(self.userplay())
      
        
        
    def won(self):
        print ("\nThe winner is: "+str(self.names[self.whoseturn])+" with a score of "+str(self.scores[self.whoseturn]))
        print(self.scores)

            
    def printscores(self):
        print("\n\n____________________________________________________")
        for x in range(len(self.names)):
            print(self.names[x] + ":"+ str(self.scores[x]))
        print("____________________________________________________")

    def play(self):
        x = True
        while x == True:
            if (self.computer[self.whoseturn] == False):
                x = self.userplay()
            else:
                x = self.computerplay()
            self.whoseturn += 1;
            if self.whoseturn == len(self.names):
                self.whoseturn = 0
                

def main():
    Game = PigGame(['Emmanuel','Comp1'],[0,0],[False,True],0)
    Game.play()

main()
        




            
        
        






    
