
import random

class bacterium:
    def __init__(self, health, x, y, age=0): 
        self.age=age
        self.health=health
        self.x=x
        self.y=y
        # how to take random health

    def move(self, a,b):
        los=random.randint(0,4)

        if los==0 and self.y<b:
            self.y=self.y+1
        if los==1 and self.y>0:
            self.y=self.y-1
        if los==2 and self.x<a:
            self.x=self.x+1
        if los==3 and self.x>0:
            self.x=self.x-1 

    def reproduction(self):
        probability=min(0.3,1-self.age/12)
        if random.random()<probability:
            return 1
        else:
            return 0


    def die(self):
        probability=min(1,self.age/25)
        if random.random()<probability:
            return 1
        else:
            return 0

    def place(self):
        return self.x, self.y
    
    def update_age(self):
        self.age=self.age+1
        

# grid has to have list which storages bacterias, wszystkim zarzadza grid który maw sobie bakterie i okresla jej połozenie
class grid:
    storage=[]
    # movement={"up":1, "down":-1, "right":1, "left":-1}
    def __init__(self, a=20, b=20):
        self.a=a
        self.b=b
        
    def add(self, bacteria):
        grid.storage.append(bacteria)
    
    # initialize bacterium
    def initialize(self):
        num=random.randint(1,5)
        self.bacterium_list=[]
        for i in range(num):
            bact=bacterium("good", random.randint(0,self.a), random.randint(0, self.b))
            self.bacterium_list.append(bact)
            
    def run_step(self):
        bacterium_to_die=[]
        for i, bact in enumerate(self.bacterium_list):
            bact.update_age()
            bact.move(self.a, self.b)
            if bact.reproduction()==1:
                bact_reproducted=bacterium("good", bact.x, bact.y)
                self.bacterium_list.append(bact_reproducted)
            if bact.die()==1:
                bacterium_to_die.append(i)
            
        for i in sorted(bacterium_to_die, reverse=True):
            del self.bacterium_list[i]
    
    def position(self):
        for bact in self.bacterium_list:
            print(bact.place())

    
# bactery moves randomly, here to incoprporate random module

Console=grid()
Console.initialize()
print(Console.position())
for n in range(100):
    Console.run_step()
    print(len(Console.bacterium_list))
    

# print(Console.position())
