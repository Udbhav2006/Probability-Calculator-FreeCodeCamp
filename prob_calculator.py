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
    pass

h =  Hat(yellow = 1, blue = 2, striped = 2, red = 3)

