import json
from store.models import Bag

with open('productsTemp.json') as f:
  product_json = json.load(f)

for i, product in enumerate(product_json):
  product = Bag(name=product['name']+str(i), brand=product['brand'], price=product['price'], discount_price=product['discount_price'], featured=product['featured'], thumbnail=product['thumbnail'], quantity=product['quantity'], in_stock=product['in_stock'], description=product['description'])
  product.save()