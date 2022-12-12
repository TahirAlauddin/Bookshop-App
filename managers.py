from models import *
from typing import *

INDEX_USER_ID_USER_FILE = INDEX_BOOK_ID_BOOK_FILE = 0
INDEX_USERNAME_USER_FILE = INDEX_BOOK_NAME_BOOK_FILE = 1
INDEX_PASSWORD_USER_FILE = INDEX_AUTHOR_NAME_BOOK_FILE = 2
INDEX_IS_ADMIN_USER_FILE = INDEX_BOOK_PRICE_BOOK_FILE = 3
INDEX_BOOK_IMAGE_BOOK_FILE = 4


class DatabaseAdmin:
    books = []
    users = []
    orders = []
    order_items = []
    collections = []

    # //////////////////////////////////////////////////////////////////////
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ??????????????????????????????????????????????????????????????????????
    #######################################################################
    # WORKING WITH USER FILE
    def read_user(self, id) -> User:
        with open(User.filename) as user_file:
            users_information = user_file.read()
            for user in users_information.split('\n')[:-1]:
                _id, username, password, is_admin = user.split(',')
                if id == _id:
                    return User(username, password, is_admin, _id=_id)

    def login(self, username, password) -> Tuple[bool]:
        users = self.list_users()
        for user in users:
            if user.username == username and user.password == password:
                is_admin = [True, False][user.is_admin == 'False']
                return True, is_admin
        return False, False

    def signup(self, username, password, is_admin) -> bool:
        exists, _ = self.login(username, password)
        if exists:
            return False
        user = User.create(username, password, is_admin)
        with open(User.filename, 'a') as user_file:
            user_file.write(','.join([str(user.userid), str(username),
                                      str(password), str(is_admin)]))
            user_file.write('\n')
        return user

    # //////////////////////////////////////////////////////////////////////
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ??????????????????????????????????????????????????????????????????????
    #######################################################################
    # BOOKS MANIPULATION
    def view_book(self, id) -> Book:
        with open(Book.filename) as book_file:
            for book in book_file.readlines():
                _id, name, author, quantity, price, image = book.split(',')
                if _id == id:
                    return Book(name, author, quantity, price, image, _id=_id)

    def list_books(self) -> List[Book]:
        books = []
        with open(Book.filename) as book_file:
            data = book_file.read()
            for book in data.split('\n')[:-1]:
                _id, name, author, quantity, price, image = book.split(',')
                book = Book(name, author, quantity, price, image, _id=_id)
                books.append(book)
        return books

    def delete_book(self, id) -> None:
        books = []
        with open(Book.filename) as book_file:
            data = book_file.read()
            for book in data.split('\n')[:-1]:
                _id, name, author, quantity, price, image = book.split(',')
                if _id == id:
                    continue
                books.append([_id, name, author, quantity, price, image])

        with open(Book.filename, 'w') as book_file:
            for book in books:
                book_file.write(','.join(book))
                book_file.write('\n')

    def update_book(self, id, name=None, author=None, quantity=None, price=None, image=None) -> None:
        books = []
        with open(Book.filename) as book_file:
            data = book_file.read()
            for book in data.split('\n')[:-1]:
                book = book.split(',')
                if id == book[0]:
                    books.append([book[0], name or book[1], author or book[2],
                                 quantity or book[3], image or book[5], price or book[4]])
                else:
                    books.append(book)
        with open(Book.filename, 'w') as book_file:
            for book in books:
                book_file.write(','.join(book))
                book_file.write('\n')

    def add_book(self, name, author, quantity, price, image) -> Book:
        book = Book.create(name, author, quantity, price, image)
        with open(Book.filename, 'a') as book_file:
            book_file.write(
                ','.join([book.book_id, name, author, price, image, str(quantity)]))
            book_file.write('\n')

        return book

    # ////////////////////////////////////////////////////////////////////
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ??????????????????????????????????????????????????????????????????????
    #######################################################################
    # ORDERS MANIPULATION
    def view_order(self, id) -> list:
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, customer, placed_at = order.split(',')
                if _id == id:
                    return _id, customer, placed_at

    def view_order_return_object(self, id) -> Order:
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, customer, placed_at = order.split(',')
                if _id == id:
                    return Order(customer, _id=_id)

    def list_orders(self) -> List[List]:
        orders = []
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, customer, placed_at = order.split(',')
                orders.append([_id, customer, placed_at])

        return orders

    def list_orders_return_object(self) -> List[Order]:
        orders = []
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, placed_at, customer, total_price = order.split(',')
                order = Order(customer, _id=_id)
                order.dateadded = placed_at
                order.total_price = total_price
                orders.append(order)

        return orders

    def delete_order(self, id) -> None:
        orders = []
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, customer, placed_at = order.split(',')
                if _id != id:
                    orders.append([_id,  customer, placed_at])

        with open(Order.filename, 'w') as order_file:
            for order in orders:
                order_file.write(','.join(order))
                order_file.write('\n')

    def update_order(self, id, customer) -> None:
        orders = []
        with open(Order.filename) as order_file:
            for order in order_file.readlines():
                _id, placed_at, customer, total_price = order.split(',')
                if _id == id:
                    _customer = customer
                orders.append([_id, placed_at, _customer, total_price])

        with open(Order.filename, 'w') as order_file:
            for order in orders:
                order_file.write(','.join(order))
                order_file.write('\n')

    def add_order(self, order) -> Order:
        with open(Order.filename, 'a') as order_file:
            order_file.write(
                ','.join([str(order.order_id),  str(order.dateadded), order.customer, str(order.total_price)]))
            order_file.write('\n')

        return order

    # //////////////////////////////////////////////////////////////////////
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ??????????????????????????????????????????????????????????????????????
    #######################################################################
    # ORDER ITEMS MANIPULATION
    def view_order_item(self, id) -> Tuple:
        with open(OrderItem.filename) as orderItem_file:
            data = orderItem_file.read()
            for orderItem in data.split('\n')[:-1]:
                _id,  order, book, quantity = orderItem.split(',')

                if _id == id:
                    return _id,  order, book, quantity

    def list_order_items(self) -> List[OrderItem]:
        orderItems = []
        with open(OrderItem.filename) as orderItem_file:
            data = orderItem_file.read()
            for orderItem in data.split('\n')[:-1]:
                _id, order, book, quantity = orderItem.split(',')
                book = self.view_book(book)
                orderItem = OrderItem(order, book, quantity, _id=_id)
                orderItems.append(orderItem)

        return orderItems

    def delete_order_item(self, id) -> None:
        orderItems = []
        with open(OrderItem.filename) as orderItem_file:
            data = orderItem_file.read()
            for orderItem in data.split('\n')[:-1]:
                _id,  order, book, quantity = orderItem.split(',')
                if _id == id:
                    continue
                orderItems.append([_id,  order, book, quantity])

        with open(OrderItem.filename, 'w') as orderItem_file:
            for orderItem in orderItems:
                orderItem_file.write(','.join(orderItem))
                orderItem_file.write('\n')

    def update_order_item(self, id, **kwargs) -> None:
        orderItems = []
        with open(OrderItem.filename) as orderItem_file:
            data = orderItem_file.read()
            for orderItem in data.split('\n')[:-1]:
                _id,  order, book, quantity = orderItem.split(',')
                if _id == id:
                    attribute_changed = list(kwargs.keys())
                    print(attribute_changed)
                orderItems.append([_id,  order, book, quantity])

        with open(OrderItem.filename, 'w') as orderItem_file:
            for orderItem in orderItems:
                orderItem_file.write(','.join(orderItem))
                orderItem_file.write('\n')

    def add_order_item(self, order_item) -> bool:
        item_quantity = order_item.quantity
        book_id = order_item.book.book_id
        book_quantity = self.view_book(book_id).quantity
        # Validation
        if int(item_quantity) > int(book_quantity):
            # Order book quantity is more than our database
            return False
        with open(OrderItem.filename, 'a') as orderItem_file:
            orderItem_file.write(
                ','.join([str(order_item.orderitem_id),  str(order_item.order_id), str(order_item.book.book_id), str(item_quantity)]))
            orderItem_file.write('\n')
        # Update book quantity
        self.update_book(
            book_id, quantity=f"{int(book_quantity)-int(item_quantity)}")
        return True

    # //////////////////////////////////////////////////////////////////////
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ??????????????????????????????????????????????????????????????????????
    #######################################################################
    # USER MANIPULATION

    def view_user(self, id) -> User:
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                _id,  username, password, is_admin = user.split(',')

                if _id == id:
                    return User(username, password, is_admin, _id=_id)

    def get_user_id(self, username) -> int:
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                id,  _username, *_ = user.split(',')

                if username == _username:
                    return id

    def get_book_price(self, title):
        with open(Book.filename) as book_file:
            data = book_file.read()
            for book in data.split('\n')[:-1]:
                _, _title, price, *_ = book.split(',')
                if title == _title:
                    return price

    def get_super_user_status(self, user_id):
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                id,  *_, is_admin = user.split(',')
                if user_id == id:
                    return [True, False][is_admin == 'False']

    def list_users(self) -> List[User]:
        users = []
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                _id, name, password, isAdmin = user.split(',')
                users.append(User(name, password, isAdmin, _id=_id))
        return users

    def update_user(self, id, name=None, password=None, isAdmin=None):
        users = []
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                user = user.split(',')
                if id == user[0]:
                    users.append([user[0], name or user[1], password or user[2],
                                  isAdmin or user[3]])
                else:
                    users.append(user)
        with open(User.filename, 'w') as user_file:
            for user in users:
                user_file.write(','.join(user))
                user_file.write('\n')

    def get_book_id(self, title):
        books = self.list_books()
        for book in books:
            if title == book[INDEX_BOOK_NAME_BOOK_FILE]:
                return book[INDEX_BOOK_ID_BOOK_FILE]

    def delete_user(self, id) -> None:
        users = []
        with open(User.filename) as user_file:
            data = user_file.read()
            for user in data.split('\n')[:-1]:
                _id, name, password, isAdmin = user.split(',')
                if _id == id:
                    continue
                users.append([_id, name, password, isAdmin])

        with open(User.filename, 'w') as user_file:
            for user in users:
                user_file.write(','.join(user))
                user_file.write('\n')
