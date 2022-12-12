from datetime import datetime


def get_id(filename):
    file = open(filename)
    try:
        x = file.readlines()[-1]
        id = int(x.split(',')[0])
    except:
        id = 0
    finally:
        file.close()
    return id


class User:
    filename = 'data/users.csv'
    count = get_id(filename)

    def __init__(self, username, password, is_admin, _id=None):
        if _id:
            self.__userid = _id
        else:
            self.__userid = User.count

        self.__username = username
        self.__password = password
        self.__is_admin = is_admin

    # Factory Design Pattern
    def create(username, password, is_admin):
        User.count += 1
        return User(username, password, is_admin)

    @property
    def userid(self):
        return str(self.__userid)

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def is_admin(self):
        return self.__is_admin

    @userid.setter
    def userid(self, _id):
        self.__userid = _id

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    @is_admin.setter
    def is_admin(self, is_admin):
        self._is_admin = is_admin


class Book:
    filename = 'data/books.csv'
    count = get_id(filename)

    def __init__(self, name, author, quantity, image, price, _id=None):
        if _id:
            self.__book_id = _id
        else:
            self.__book_id = Book.count

        self.__name = name
        self.__author = author
        self.__price = price
        self.__quantity = quantity
        self.__image = image

        # Factory Design Pattern

    def create(name, author, quantity, image, price):
        Book.count += 1
        return Book(name, author, quantity, image, price)

    def __str__(self) -> str:
        return self.__name

    @property
    def book_id(self): return str(self.__book_id)
    @property
    def name(self): return self.__name
    @property
    def price(self): return self.__price
    @property
    def author(self): return self.__author
    @property
    def image(self): return self.__image
    @property
    def quantity(self): return self.__quantity
    @quantity.setter
    def quantity(self, quantity): self.__quantity = quantity
    @image.setter
    def image(self, image): self.__image = image
    @author.setter
    def author(self, author): self.__author = author
    @book_id.setter
    def book_id(self, _id): self.__book_id = _id
    @name.setter
    def name(self, name): self.__name = name
    @price.setter
    def price(self, price): self.__price = price


class Order:
    filename = 'data/orders.csv'
    count = get_id(filename)

    def __init__(self, customer_name, _id=None):
        if _id:
            self.__order_id = _id
        else:
            self.__order_id = Order.count
        self.__customer = customer_name
        self.__dateadded = datetime.now().date()

    # Factory Design Pattern
    def create(customer_name):
        Order.count += 1
        return Order(customer_name)

    @property
    def order_id(self): return str(self.__order_id)
    @property
    def total_price(self): return self.__total_price
    @property
    def customer(self): return self.__customer
    @customer.setter
    def customer(self, customer): self.__customer = customer
    @order_id.setter
    def order_id(self, order_id): self.__order_id = order_id
    @total_price.setter
    def total_price(self, total_price): self.__total_price = total_price
    @property
    def dateadded(self): return self.__dateadded
    @dateadded.setter
    def dateadded(self, date): self.__dateadded = date


class OrderItem:
    filename = 'data/orderItems.csv'
    count = get_id(filename)

    def __init__(self, order_id, book, quantity, _id=None):
        if _id:
            self.__orderitem_id = _id
        else:
            self.__orderitem_id = OrderItem.count
        self.__order_id = order_id
        self.__book = book
        self.__quantity = quantity
        self.__price = int(book.price) * int(quantity)

    # Factory Design Pattern
    def create(order_id, book, quantity):
        OrderItem.count += 1
        return OrderItem(order_id, book, quantity)

    @property
    def orderitem_id(self): return str(self.__orderitem_id)
    @property
    def book(self): return self.__book
    @property
    def order_id(self): return str(self.__order_id)
    @property
    def quantity(self): return str(self.__quantity)
    @book.setter
    def book(self, book): self.__book = book
    @orderitem_id.setter
    def orderitem_id(self, orderitem_id): self.__orderitem_id = orderitem_id
    @quantity.setter
    def quantity(self, quantity): self.__quantity = quantity
    @order_id.setter
    def order_id(self, order_id): self.__order_id = order_id
    @property
    def price(self): return str(self.__price)
    @price.setter
    def price(self, price): self.__price = price
