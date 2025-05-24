from dependency_sdk import SDKBuilder, SDKVersion, Product



def get_data(self, product_name: str) -> Product:
        api = self.sdk_builder.build(SDK_VERSION)
        product_id = self._get_product_id(product_name)
        product = api.product.get(product_id)
        str_product = self.str_product(str())

        fiber = product.fiber
        if fiber != '-':
            fiber = float(fiber)*1000
        else:
            fiber = None

        protein = float(product.protein)*1000
        fat = float(product.fat)*1000

        product = Product(product.name, product.energy, str_product.protein, str_product.fiber, str_product.fat, product.nutriscore)
        return product

