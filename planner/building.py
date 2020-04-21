import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner
    
    def print_building(self):
        sentence = f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.'

        print(sentence)

eight_hundred_eighth = Building("800 8th Street", 12)

eight_hundred_eighth.construct()
eight_hundred_eighth.print_building()

