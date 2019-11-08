class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.reserve = []

    def display(self):
        print("Customer name: {}".format(self.name))
        print("Customer age: {}".format(self.age))
        print("Customer reserved seats: ")
        for r in self.reserve:
            print(r)

    def __str__(self):
        return self.name