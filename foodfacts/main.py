from foodfacts.display_facts import DisplayFacts
from foodfacts.openfoodfact_adapter import OpenfoodfactAdapter
from foodfacts.model import Product
from foodfacts.api import get_data


class FoodFact:
    def __init__(self, openfoodfact_adapter: OpenfoodfactAdapter, display_data: DisplayFacts):
        self.food_data = openfoodfact_adapter
        self.view = display_data   

    def ask_and_display_data(self):
        product_name = input("Enter a product name: ")
        product = self.food_data.get_data(product_name)


if __name__ == "__main__":
    app = FoodFact(OpenfoodfactAdapter(), DisplayFacts())
    app.ask_and_display_data()