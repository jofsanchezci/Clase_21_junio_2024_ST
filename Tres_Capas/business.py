from data import Data

class BusinessLogic:
    def __init__(self):
        self.data = Data()

    def add_item(self, item):
        self.data.add_item(item)

    def get_items(self):
        return self.data.get_items()
