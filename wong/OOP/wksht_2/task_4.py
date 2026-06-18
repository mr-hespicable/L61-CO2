class Product:
    def __init__(self, pid, price):
        self.__product_id = pid
        self.__product_price = price
    
    def get_id(self):
        return self.__product_id
    
    def get_price(self):
        return self.__product_price


class Order:
    def __init__(self, on, od):
        self.__order_number = on
        self.__order_date = od
        self.__products_ordered = []
        self.__num_items_ordered = 0
        self.__status = OrderStatus()

    def OrderItem(self, p: Product):
        self.__products_ordered.append(p)
        self.__num_items_ordered += 1

    def getOrderStatus(self):
        return self.__status.get_status()

    def getOrderItemID(self, n):
        return self.__products_ordered[n-1].get_id()

    def getOrderItemPrice(self, n):
        return self.__products_ordered[n-1].get_price()

class OrderStatus:
    def __init__(self, hs = False):
        self.__has_shipped = hs

    def get_status(self):
        return self.__has_shipped


prod_1 = Product("beans", 0.45)
prod_2 = Product("eggs", 1.25)

myOrder = Order(1, "1/1/17")
myOrder.OrderItem(prod_1)
myOrder.OrderItem(prod_2)

print(myOrder.getOrderStatus())
print(myOrder.getOrderItemID(1))
print(myOrder.getOrderItemPrice(1))

print(myOrder.getOrderItemID(2))
print(myOrder.getOrderItemPrice(2))
