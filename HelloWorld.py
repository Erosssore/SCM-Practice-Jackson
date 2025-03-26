class Name:
    def __init__(self, name):
        self.name = name
    def world(self):
        print("\nHello World, my name is", self.name, "\n"
              "this is the SCM project!")

n = input("What is your name: ")
user = Name(n)
user.world()