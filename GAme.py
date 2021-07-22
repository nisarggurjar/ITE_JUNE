class Player:

    def __init__(self, name):
        self.name = name
        self.life = 5
    
    def Attack(self):
        self.life-=1

    def Defence(self):
        self.life+=1

    def CheckLife(self):
        print(self.life)

p1 = Player("P1")
p2 = Player("P2")

p1.Attack() #4
p1.Attack() #3
p1.Defence() #4
p1.Attack() #3
p1.Defence() #4
p1.Defence() #5
p1.Defence() #6


p2.Attack() #4
p2.Attack() #3
p2.Attack() #2
p2.Attack() #1
p2.Defence() #2
p2.Attack() #1
p2.Attack() #0
p2.Attack() #-1
p2.Defence() #0
p2.Attack() #-1
p2.Defence() #0
p2.Defence() #1


p1.CheckLife()
p2.CheckLife()