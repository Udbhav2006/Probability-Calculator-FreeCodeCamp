import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []

        for ball in balls.keys():
            for i in range(0, balls[ball]):
                self.contents.append(ball)

        self.contents_copy = copy.copy(self.contents)
 

    def draw(self, num):

        if num > len(self.contents):
            self.contents = copy.copy(self.contents_copy)
        else:
            l = []
            for i in range(0, num):
                l.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
            return l
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_outcomes = 0
    total_outcomes = num_experiments

    for i in range(0, num_experiments):
        if num_balls_drawn > len(hat.contents):
            num_balls_drawn = len(hat.contents)
        balls = hat.draw(num_balls_drawn)
        hat.contents = copy.copy(hat.contents_copy)

        balls_dict = {}
        for ball in balls:
            if ball in balls_dict.keys():
                balls_dict[ball] += 1
            else:
                balls_dict[ball] = 1
    
        okays = 0
        for key in expected_balls.keys():
            try:
                if expected_balls[key] <= balls_dict[key]:
                    okays += 1
                else:
                    x = 1/0
                
            except:
                break
        
        if okays == len(expected_balls.keys()):
            expected_outcomes += 1

    return expected_outcomes / total_outcomes


