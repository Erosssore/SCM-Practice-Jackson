class Name:
    def __init__(self, name):
        self.name = name
    def world(self):
        print("Hello World, my name is", self.name, "\n"
              "this is the SCM project!")


n = Name('Jackson')
n.world()