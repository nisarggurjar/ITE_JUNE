class Player:

    def __init__(self, name):
        self.name = name
        self.life = 5
        self.points = 1000

    def Attack(self):
        if self.life == 0:
            print("Game over")
        else:
            self.life-=1
            self.points -= 20

    def Defence(self):
        if self.life >= 5:
            print("Your life is already full")
        elif self.life <= 0:
            print("Game Over")
        else:
            self.life+=1
            self.points +=15

    def CheckLife(self):
        print(self.life)

class Store(Player):

    def BuyLife(self):
        # 1 life = 20 points
        # Life can never be more than 5
        # Points should be checked here
        pass

    def SellLife(self):
        # 1 life = 15 points
        # You can not sell all of your lifes (you should always have minimum 1 life)
        # Points should be checked here
        pass