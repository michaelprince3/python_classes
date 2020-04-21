class Pizza:
    def __init__(self):
        self.size = ""
        self.crustType = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        sentence = f'I would like a {self.size}-inch, {self.crustType} pizza with {self.toppings[0]} and {self.toppings[1]}.'

        print(sentence)
        