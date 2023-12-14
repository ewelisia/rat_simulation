
import random

class rat:
    def __init__(self, health, x, y, age=0): 
        self.age=age
        self.health=health
        self.x=x
        self.y=y
        # how to take random health

    def move(self, a,b, allowed_moves):
        los=random.randint(0,4)
        if los==0 and self.y<b:
            if (self.x, self.y+1) in allowed_moves:
                self.y = self.y+1
        if los==1 and self.y>0:
            if (self.x, self.y-1) in allowed_moves:
                self.y=self.y-1
            # to do
        if los==2 and self.x<a:
            if (self.x+1, self.y) in allowed_moves:
                self.x=self.x+1
        if los==3 and self.x>0:
            if (self.x-1, self.y) in allowed_moves:
                self.x=self.x-1 
        

    def reproduction(self):
        probability=min(0.3,1-self.age/12)
        if random.random()<probability:
            return 1
        else:
            return 0


    def die(self):
        probability=min(1,self.age/10)
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
        
    def add(self, rats):
        grid.storage.append(rats)
    
    # initialize rat
    def initialize(self):
        num=random.randint(1,5)
        self.rat_list=[]
        for i in range(num):
            ra=rat("good", random.randint(0,self.a), random.randint(0, self.b))
            self.rat_list.append(ra)
            
    def run_step(self):
        rat_to_die=[]
        for i, ra in enumerate(self.rat_list):
            ra.update_age()
            rat_positions=[]
            for ra_x_y in self.rat_list:
                rat_positions.append(ra_x_y.place())
            pos_moves = self.possible_move(ra.x, ra.y)
            pos_moves_rat = []
            for move in pos_moves:
                if move not in rat_positions:
                    pos_moves_rat.append(move)
# iterate through all rat_positions
#
            ra.move(self.a, self.b, pos_moves_rat)
            if ra.reproduction()==1:
                ra_reproducted=rat("good", ra.x, ra.y)
                self.rat_list.append(ra_reproducted)
            if ra.die()==1:
                rat_to_die.append(i)
            
        for i in sorted(rat_to_die, reverse=True):
            del self.rat_list[i]
    
    def position(self):
        for rat in self.rat_list:
            print(rat.place())

    def possible_move(self, x, y):
        possible_moves=[]
        if not x==0:
            possible_moves.append((x-1, y))
        if not x==self.a:
            possible_moves.append((x+1, y))
        if not y==0:
            possible_moves.append((x, y-1))
        if not y==self.b:
            possible_moves.append((x, y+1))
        return possible_moves

        

    
# bactery moves randomly, here to incoprporate random module

Console=grid()
Console.initialize()
print(Console.position())
for n in range(100):
    Console.run_step()
    print(len(Console.rat_list))
    

# print(Console.position())
