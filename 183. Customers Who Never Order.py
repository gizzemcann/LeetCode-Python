customers = [
    {"id": 1, "name": "Joe"},
    {"id": 2, "name": "Henry"},
    {"id": 3, "name": "Sam"},
    {"id": 4, "name": "Max"}
]

orders = [
    {"id": 1, "customerId": 3},
    {"id": 2, "customerId": 1}
]

# Önce sipariş veren müşteri ID'lerini set olarak al
ordered_customer_ids = set(order["customerId"] for order in orders)

# Sipariş vermemiş olanları filtrele
no_orders = [customer["name"] for customer in customers if customer["id"] not in ordered_customer_ids]

print(no_orders)
