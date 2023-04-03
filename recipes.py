class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish 
        self.items = items
        self.time = time


    def contents(self):
        print(f"The {self.dish} has {str(self.items)} and takes {str(self.time)} to prepare")


pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
githeri = Recipe("Githeri", ["maize", "beans", "water"], 89)
pizza.contents()
githeri.contents()
