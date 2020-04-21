from classes import Pizza

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crustType = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()