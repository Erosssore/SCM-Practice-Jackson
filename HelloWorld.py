# Name class takes inputs from n which is then converted to a Name object and passed into the world() function
class Name:
    # OOP Initialization and Function
    def __init__(self, name):
        self.name = name
    def world(self):
        print("\nHello World, my name is", self.name, "\n"
              "this is the SCM project!")

# Input segment and function call
n = input("What is your name: ")
user = Name(n)
user.world()