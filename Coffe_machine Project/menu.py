class Menu:
    def items(self):
        print("items availlable : \n1.Americano.(4$) \n2.Cappuccino.(3$)\n3.Espresso.(2$)\n4.Exit the machine.")
    def select(self, select):
        if select == 1:
            return "americano"
        elif select == 2:
            return "cappuccino"
        elif select == 3:
            return "espresso"
        elif select == 4:
            return "exit"
        else:
            return None
a = Menu()