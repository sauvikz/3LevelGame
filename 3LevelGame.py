from sys import exit
from random import randint

class Situation(object):
    def enter(self):
        print "This is a parent class. Everything will done in sub-classes of this parent class."
        exit(1)
        
class DoorA(Situation):
    def enter(self):
        player_name = raw_input("Enter your name: ")
        print "Welcome to the game %s" % player_name.capitalize()
        print """
        I am very sorry to announce that you have landed yourself 
        in the darkest dungeon of the world where mysterious and magical 
        creatures dwell and death awaits you every moment. There is only one 
        path to freedom. There are three doors that you have to surpass to 
        attain freedom. But alas! Every door comes with its own set of 
        puzzles. Chances of survival is low but if you are strong willed
        and luck is on your side, you might live to see another day.
        ALL THE BEST %s.
        """ % player_name.capitalize()
        print "Welcome to DoorA also known as the 'Door to Hell'"
        print "There is a vicious bloodthirsty tiger seated in front of you."
        print "What do you do to save yourself?"
        action = raw_input("Enter your choices out of 'laugh' or 'cry' else you wind up dead! >> ")            
        if action == 'laugh':
            return 'death'
        elif action == 'cry':
            return 'door_b'
        else:
            return 'death'
            
class DoorB(Situation):
    def enter(self):
        print "Whoof! Seeing you cry, the tiger magically turns into an angel and lets you access DoorB"
        print "Welcome to DoorB! You will have to solve a Mathemactics puzzle to cross this door."
        print "The makers of this dungeon were mathematicians after all *wink wink*"
        print "What is Ramanujan's number? Hint: It is the smallest number that is the sum of cubes of two different pairs!"
        print "example: a^3 + b^3 = c^3 + d^3 = Ramanujan's number where a != b != != c != d"
        r_number = int(raw_input("Enter Ramanujan's Number >> "))
        if r_number == 1729:
            return 'door_c'
        else:
            return 'death'
            
class DoorC(Situation):
    def enter(self):
        print "That was a close shave! Hope you didn't use the blasmephous tool called 'Google'"
        print "Welcome to DoorC! You get one chance to survivor here. Offer your prayers to lady luck!"
        print "We will roll a 6-sided dice and let destiny decide your fate."
        print "You make it through the door if you get any number less than or equal to three else you DIE!"
        print "Rolling your dice now."
        print "Hit enter to continue"
        raw_input("> ")
        number = randint(1,6)
        print "The number you got is %s" % number
        print "_" * 100
        if number <= 3:
            print "Congratulations it's less than 3 :D"
            return 'finish'
        else:
            return 'death'
            
class Dead(Situation):
    def enter(self):
        print """
        You are such a big loser! You end up dead in this game!
        I will prey on your soul! You are a disappointment to humanity! BYE!
        """
        exit(1)
        
class Finish(Situation):
    def enter(self):
        print "Woahh!! You are one of the lucky few who survived. Have a good day :D"
        exit(1)        


class Map(object):
    situations = {
        "door_a": DoorA(),
        "door_b": DoorB(),
        "door_c": DoorC(),
        "death": Dead(),
        "finish": Finish() 
    }
    
    def __init__(self, start_situation):
        self.start_situation = start_situation
    
    def get_val_from_dict(self, key):
        val = Map.situations.get(key)
        return val
    
    def situation_return(self):
        return self.get_val_from_dict(self.start_situation)
    

class Engine(object):
    
    def __init__(self, situation):
        self.situation = situation
        
    # self.situation = Map('door_a') initially
    def play(self):
        current_situation = self.situation.situation_return()
        last_situation = self.situation.get_val_from_dict('finish')
    
        while current_situation != last_situation:
            situation_now = current_situation.enter()
            current_situation = self.situation.get_val_from_dict(situation_now)
        current_situation.enter()
        
           
start = Map('door_a')    
y = Engine(start)
y.play()                      
