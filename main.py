from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from managers import DatabaseAdmin
from models import Order, OrderItem

from interface.bookshop import Ui_MainWindow
from interface.userForm import Ui_MainWindow as userForm_Ui_MainWindow
from interface.bookForm import Ui_MainWindow as bookForm_Ui_MainWindow
from interface.orderForm import Ui_MainWindow as orderForm_Ui_MainWindow
from interface.orderItemForm import Ui_MainWindow as orderItemForm_Ui_MainWindow
import os

PRODUCT_NOT_ADDED_LABEL = "Product already exists. Product was not added!"
PRODUCT_SUCCESSFULLY_ADDED_LABEL = "Product was added successfully!"


class MainWindow(QMainWindow):

    cart_books = []
    cart_order_items = []

    def __init__(self, customer='Default'):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DatabaseAdmin()
        self.books = self.db.list_books()
        self.Ui_components()
        self.customer = customer
        self.show()

    def Ui_components(self):
        # UI Changes
        self.ui.stackedWidget.setCurrentIndex(0)
        self.UiComponentLoginPage()
        self.UiComponentAdminPage()
        self.UiComponentSignupPage()
        self.UiComponentsHomePage()

    def UiComponentAdminPage(self):
        self.ui.adminStackedWidget.setCurrentWidget(self.ui.users)

        book_header = self.ui.bookTableWidget.horizontalHeader()
        order_header = self.ui.orderTableWidget.horizontalHeader()
        order_item_header = self.ui.orderItemTableWidget.horizontalHeader()
        user_header = self.ui.userTableWidget.horizontalHeader()

        for idx, header in enumerate([book_header, order_header, user_header, order_item_header]):
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(2, QHeaderView.Stretch)
            header.setSectionResizeMode(3, QHeaderView.Stretch)
            if idx in [0, 3]:
                header.setSectionResizeMode(4, QHeaderView.Stretch)
            if idx == 0:
                header.setSectionResizeMode(5, QHeaderView.Stretch)
        # Button click events
        self.ui.btn_books.clicked.connect(
            lambda: self.ui.adminStackedWidget.setCurrentWidget(self.ui.books))
        self.ui.btn_orders.clicked.connect(
            lambda: self.ui.adminStackedWidget.setCurrentWidget(self.ui.orders))
        self.ui.btn_users.clicked.connect(
            lambda: self.ui.adminStackedWidget.setCurrentWidget(self.ui.users))
        self.ui.btn_orderItems.clicked.connect(
            lambda: self.ui.adminStackedWidget.setCurrentWidget(self.ui.orderItems))
        self.ui.adminLogoutBtn.clicked.connect(self.logout)

        self.ui.book_add_button.clicked.connect(self.add_book)
        self.ui.user_add_button.clicked.connect(self.add_user)
        self.ui.order_add_button.clicked.connect(self.add_order)
        self.ui.order_item_add_button.clicked.connect(self.add_order_item)

        self.ui.book_update_button.clicked.connect(self.update_book)
        self.ui.user_update_button.clicked.connect(self.update_user)
        self.ui.order_update_button.clicked.connect(self.update_order)
        self.ui.order_item_update_button.clicked.connect(
            self.update_order_item)

        self.ui.book_delete_button.clicked.connect(self.delete_book)
        self.ui.user_delete_button.clicked.connect(self.delete_user)
        self.ui.order_delete_button.clicked.connect(self.delete_order)
        self.ui.order_item_delete_button.clicked.connect(self.delete_order_item)

        self.populate_book_table()
        self.populate_user_table()
        self.populate_order_table()
        self.populate_order_item_table()

    def populate_book_table(self):
        self.books = self.db.list_books()
        rows_num = len(self.books)
        self.ui.bookTableWidget.setRowCount(rows_num)
        for row, book in enumerate(self.books):
            self.ui.bookTableWidget.setItem(
                row, 0, QTableWidgetItem(book.book_id))
            self.ui.bookTableWidget.setItem(
                row, 1, QTableWidgetItem(book.name))
            self.ui.bookTableWidget.setItem(
                row, 2, QTableWidgetItem(book.author))
            self.ui.bookTableWidget.setItem(
                row, 3, QTableWidgetItem(book.quantity))
            self.ui.bookTableWidget.setItem(
                row, 4, QTableWidgetItem(book.price))
            image_with_extension = os.path.basename(book.image)
            image = '.'.join(image_with_extension.split('.')[:-1])
            self.ui.bookTableWidget.setItem(
                row, 5, QTableWidgetItem(image))

    def populate_order_table(self):
        orders = self.db.list_orders_return_object()
        rows_num = len(orders)
        self.ui.orderTableWidget.setRowCount(rows_num)
        for row, order in enumerate(orders):
            self.ui.orderTableWidget.setItem(
                row, 0, QTableWidgetItem(order.order_id))
            self.ui.orderTableWidget.setItem(
                row, 1, QTableWidgetItem(order.customer))
            self.ui.orderTableWidget.setItem(
                row, 2, QTableWidgetItem(order.total_price))
            self.ui.orderTableWidget.setItem(
                row, 3, QTableWidgetItem(order.dateadded))

    def populate_order_item_table(self):
        order_items = self.db.list_order_items()
        rows_num = len(order_items)
        table = self.ui.orderItemTableWidget
        table.setRowCount(rows_num)
        for row, orderItem in enumerate(order_items):
            table.setItem(row, 0, QTableWidgetItem(orderItem.orderitem_id))
            table.setItem(row, 1, QTableWidgetItem(orderItem.order_id))
            table.setItem(row, 2, QTableWidgetItem(orderItem.book.book_id))
            table.setItem(row, 3, QTableWidgetItem(orderItem.quantity))
            table.setItem(row, 4, QTableWidgetItem(orderItem.price))

    def populate_user_table(self):
        users = self.db.list_users()
        rows_num = len(users)
        self.ui.userTableWidget.setRowCount(rows_num)
        for row, user in enumerate(users):
            self.ui.userTableWidget.setItem(
                row, 0, QTableWidgetItem(user.userid))
            self.ui.userTableWidget.setItem(
                row, 1, QTableWidgetItem(user.username))
            self.ui.userTableWidget.setItem(
                row, 2, QTableWidgetItem(user.password))
            self.ui.userTableWidget.setItem(
                row, 3, QTableWidgetItem(user.is_admin))

    def UiComponentLoginPage(self):
        self.ui.loginBtn.clicked.connect(self.login)
        self.ui.signupCommandBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signupPage))

    def UiComponentSignupPage(self):
        self.ui.signupBtn.clicked.connect(self.signup)
        self.ui.loginCommandBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage))

    def UiComponentsHomePage(self):

        self.ui.scrollArea.close()

        self.scrollArea = QScrollArea(self.ui.books_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 540, 328))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(15, 15, 10, 10)
        self.gridLayout.setSpacing(15)

        for idx, book in enumerate(self.books):
            self.book = QFrame(self.scrollAreaWidgetContents)
            sizePolicy = QSizePolicy(
                QSizePolicy.Ignored, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.book.sizePolicy().hasHeightForWidth())
            self.book.setSizePolicy(sizePolicy)
            self.book.setMinimumSize(QSize(250, 0))

            self.verticalLayout = QVBoxLayout(self.book)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.frame = QFrame(self.book)
            self.frame.setMinimumSize(QSize(0, 0))
            self.frame.setStyleSheet("QFrame {\n"
                                     "border: none;\n"
                                     "background: white;\n"
                                     "}")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.verticalLayout2 = QVBoxLayout(self.frame)
            self.verticalLayout2.setContentsMargins(9, -1, -1, -1)
            self.book_image = QLabel(self.frame)
            self.book_image.setMaximumSize(QSize(16777215, 250))

            self.book_image.setPixmap(QPixmap(book.image))
            self.book_image.setScaledContents(True)
            self.verticalLayout2.addWidget(
                self.book_image, 0, Qt.AlignHCenter)
            self.verticalLayout.addWidget(self.frame)
            self.frame2 = QFrame(self.book)
            self.frame2.setStyleSheet("QFrame {\n"
                                      "border: none;\n"
                                      "}")
            self.frame2.setFrameShape(QFrame.StyledPanel)
            self.frame2.setFrameShadow(QFrame.Raised)

            self.verticalLayout3 = QVBoxLayout(self.frame2)
            self.book_name = QLabel(self.frame2)
            self.book_name.setText(
                f'Name: {book.name} \n Author: {book.author}')
            self.book_name.setStyleSheet("color: rgb(221, 221, 221);\n"
                                         "font: 10pt \"Segoe UI\";\n"
                                         "")
            self.book_name.setAlignment(Qt.AlignCenter)
            self.book_name.setWordWrap(True)
            self.verticalLayout3.addWidget(self.book_name)
            self.frame3 = QFrame(self.frame2)
            self.frame3.setFrameShape(QFrame.StyledPanel)
            self.frame3.setFrameShadow(QFrame.Raised)

            self.horizontalLayout_16 = QHBoxLayout(self.frame3)
            self.book_price = QLabel(self.frame3)
            self.book_price.setText(f'Price: ${book.price}')

            self.quantity_label = QLabel(self.frame3)
            self.quantity_label.setText(f"Quantity: {book.quantity}")
            self.quantity_label.setObjectName(f"quantity_label_{book.book_id}")
            self.horizontalLayout_16.addWidget(self.quantity_label)

            self.horizontalLayout_16.addWidget(self.book_price)
            self.verticalLayout3.addWidget(self.frame3)
            self.book_button = QPushButton(self.frame2)
            self.book_button.setText("Add to Cart")
            self.book_button.setMaximumSize(QSize(100, 16777215))
            self.verticalLayout3.addWidget(
                self.book_button, 0, Qt.AlignHCenter)
            self.verticalLayout.addWidget(self.frame2)
            self.gridLayout.addWidget(self.book, idx//2, idx % 2, 1, 1)

            # On click event
            self.book_button.clicked.connect(
                lambda x, _id=book.book_id: self.add_to_cart(_id))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ui.verticalLayout_33.addWidget(self.scrollArea)
        self.ui.horizontalLayout_13.insertWidget(0, self.ui.books_frame)
        self.ui.horizontalLayout_13.setStretch(0, 5)
        self.ui.horizontalLayout_13.setStretch(1, 2)

        self.ui.place_order_button.clicked.connect(self.place_order)
        self.ui.remove_from_cart_button.clicked.connect(self.remove_from_cart)
        self.ui.booksLogoutBtn.clicked.connect(self.logout)

    # Helper function

    def place_order(self):
        if self.ui.cart_tableWidget.rowCount() < 1:
            self.ui.status_label.setText(
                "Atleast 1 product is required to place an order")
            return

        successful = True
        order = Order.create(self.customer)
        order.total_price = 0
        for order_item in self.cart_order_items:
            order_item.order_id = order.order_id
            added = self.db.add_order_item(order_item)
            if not added:
                successful = False
                self.ui.status_label.setText(
                    "Order couldn't be placed. The book quantity must be less than the database.")
            order.total_price += int(order_item.price)
        self.db.add_order(order)

        # Update status
        book_ids = [book.book_id for book in self.cart_books]
        book_quantities = [book.quantity for book in self.cart_order_items]
        if successful:
            for book in self.books:
                book_id = book.book_id
                if book_id in book_ids:
                    idx = book_ids.index(book_id)
                    book.quantity = int(book.quantity) - \
                        int(book_quantities[idx])
                    label = self.findChild(QLabel, f'quantity_label_{book_id}')
                    label.setText(f"Quantity: {book.quantity}")

            self.ui.status_label.setText("Order is placed successfully!")
        # Remove items from table
        self.ui.cart_tableWidget.setRowCount(0)
        self.cart_order_items = []
        self.cart_books = []

    def add_to_cart(self, book_id):
        book = self.db.view_book(book_id)

        table = self.ui.cart_tableWidget
        product_already_exists = False

        for idx, item in enumerate(self.cart_books):
            # Product already exists in table. Increaase quantity
            if book.book_id == item.book_id:
                quantity = int(table.cellWidget(idx, 3).text()) + 1
                table.cellWidget(idx, 3).setValue(quantity)
                table.item(idx, 2).setText(f"{int(quantity)*int(book.price)}")
                # Update Order Item
                orderItem = self.cart_order_items[idx]
                orderItem.quantity = quantity
                orderItem.price = int(quantity)*int(book.price)
                product_already_exists = True

        # product doesn't exist already in the table. Add the product in the table
        if not product_already_exists:
            # Add book to cart list
            self.cart_books.append(book)
            orderItem = OrderItem.create(None, book, 1)
            self.cart_order_items.append(orderItem)

            spin_box = QSpinBox()
            spin_box.setStyleSheet('background: transparent;')
            spin_box.setValue(1)

            table.setRowCount(table.rowCount() + 1)
            table.setItem(table.rowCount()-1, 0, QTableWidgetItem(book.name))
            table.setItem(table.rowCount()-1, 1, QTableWidgetItem(book.author))
            table.setItem(table.rowCount()-1, 2,
                          QTableWidgetItem(book.price.strip()))
            table.setCellWidget(table.rowCount()-1, 3, spin_box)

            spin_box.valueChanged.connect(
                lambda x, book=book: self.change_product_price(book))

    def remove_from_cart(self):
        currentRow = self.ui.cart_tableWidget.currentRow()
        if currentRow != -1:
            del self.cart_books[currentRow]
            self.ui.cart_tableWidget.removeRow(currentRow)

    def change_product_price(self, book):
        row = self.cart_books.index(book)
        spinbox = self.ui.cart_tableWidget.cellWidget(row, 3)
        quantity = spinbox.value()
        total_price = int(quantity) * int(book.price)
        self.ui.cart_tableWidget.item(row, 2).setText(str(total_price))
        # Update order Item
        orderItem = self.cart_order_items[row]
        orderItem.quantity = quantity

    def logout(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def login(self):
        exists, isAdmin = self.db.login(
            self.ui.inputUsername.text(), self.ui.inputPassword.text())
        if not exists:
            self.ui.username_message_label.setText(
                "Username or password not found")
            return False
        # Set customer value for later use
        self.customer = self.ui.inputUsername.text()
        self.ui.inputUsername.setText('')
        self.ui.inputPassword.setText('')
        if isAdmin:
            self.ui.stackedWidget.setCurrentWidget(self.ui.adminPage)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)

    def signup(self):
        username_status = self.ui.username_message_label_signupPage
        password_status = self.ui.password_message_label_signupPage
        confirm_password_status = self.ui.confirm_password_message_label_signupPage

        username_status.setText('')
        password_status.setText('')
        confirm_password_status.setText('')

        username = self.ui.inputUsername_signupPage.text()
        password = self.ui.inputPassword_signupPage.text()
        confirm_password = self.ui.inputConfirmPassword.text()
        # Password strength validation
        if password.isdigit():
            password_status.setText(
                "Password can't be only numbers! Please provide a stronger password\n")
            return

        if password == confirm_password:
            signed_up = self.db.signup(username, password, False)
            if signed_up:
                # SUCCESSFUL
                self.ui.inputUsername_signupPage.setText('')
                self.ui.inputPassword_signupPage.setText('')
                self.ui.inputConfirmPassword.setText('')
                self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)

            else:
                # Some error or User already exist may be
                username_status.setText("Username already exists!")
            return

        password_status.setText(
            password_status.text() + "Passwords dont match!")
        confirm_password_status.setText("Passwords dont match!")

    def add_book(self):
        global w
        w = BookFormWindow(self)

    def add_user(self):
        global w
        w = UserFormWindow(self)

    def add_order(self):
        global w
        w = OrderFormWindow(self)

    def update_book(self):
        global w
        try:
            selected_row = self.ui.bookTableWidget.currentRow()
            id = self.ui.bookTableWidget.item(selected_row, 0).text()
            book = self.db.view_book(id)
            w = BookFormWindow(self, update=True, book=book, row_num=selected_row)
        except:
            pass

    def update_user(self):
        global w
        try:
            selected_row = self.ui.userTableWidget.currentRow()
            id = self.ui.userTableWidget.item(selected_row, 0).text()
            user = self.db.view_user(id)
            print(user, type(user))
            w = UserFormWindow(self, update=True, user=user, row_num=selected_row)
        except: pass

    def update_order(self):
        global w
        try:
            selected_row = self.ui.orderTableWidget.currentRow()
            id = self.ui.orderTableWidget.item(selected_row, 0).text()
            order = self.db.view_order_return_object(id)
            w = OrderFormWindow(self, update=True, order=order,
                                row_num=selected_row)
        except: pass

    def add_order_item(self):
        global w
        w = OrderFormWindow(self)

    def update_order_item(self):
        global w
        try:
            selected_row = self.ui.orderItemTableWidget.currentRow()
            id = self.ui.orderItemTableWidget.item(selected_row, 0).text()
            order = self.db.view_order_return_object(id)
            w = OrderItemFormWindow(self, update=True, order=order,
                                    row_num=selected_row)
        except: pass


    def delete_book(self):
        try:
            selected_row = self.ui.bookTableWidget.currentRow()
            id = self.ui.bookTableWidget.item(selected_row, 0).text()
            self.db.delete_book(id)
            self.populate_book_table()
        except: pass


    def delete_user(self):
        try:
            selected_row = self.ui.userTableWidget.currentRow()
            id = self.ui.userTableWidget.item(selected_row, 0).text()
            self.db.delete_user(id)
            self.populate_user_table()
        except: pass


    def delete_order(self):
        try:
            selected_row = self.ui.orderTableWidget.currentRow()
            id = self.ui.orderTableWidget.item(selected_row, 0).text()
            self.db.delete_order(id)
            self.populate_order_table()
        except: pass


    def delete_order_item(self):
        try:
            selected_row = self.ui.orderItemTableWidget.currentRow()
            id = self.ui.orderItemTableWidget.item(selected_row, 0).text()
            self.db.delete_order_item(id)
            self.populate_order_item_table()
        except: pass



class BookFormWindow(QMainWindow):
    def __init__(self, admin_window, update=False, book=None, row_num=None):
        super().__init__()
        self.book = book
        self.row_num = row_num
        self.admin_window = admin_window
        self.db = DatabaseAdmin()
        self.ui = bookForm_Ui_MainWindow()
        self.ui.setupUi(self)

        # USER INTERFACE

        self.ui.chooseFile_button.clicked.connect(self.openFileNamesDialog)
        if update:
            self.ui.add_buttton.setText("Update")
            self.populate_input_boxes()
            self.ui.add_buttton.clicked.connect(self.update_book)
        else:
            self.ui.add_buttton.clicked.connect(self.add_book)

        self.show()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(
            self, "Product Image", "", "JPEG (*.jpg *.jpeg);; PNG (*.png)", options=options)
        self.file = file
        if file:
            # A file was selected
            image_with_extension = os.path.basename(file)
            self.image = '.'.join(image_with_extension.split('.')[:-1])
            self.ui.chooseFile_button.setText(image_with_extension)
            self.ui.chooseFile_button.setIconSize(QSize(0, 0))

    def add_book(self):
        name = self.ui.input_name.text()
        author = self.ui.input_author.text()
        quantity = self.ui.input_quantity.text()
        price = self.ui.input_price.text()

        book = self.db.add_book(
            name, author, quantity, price, self.file)
        self.ui.status_label.setText(PRODUCT_SUCCESSFULLY_ADDED_LABEL)

        # Insert added product in the admin table as well
        if self.admin_window:
            table = self.admin_window.ui.bookTableWidget
            row_count = table.rowCount()
            table.setRowCount(row_count+1)
            table.setItem(row_count, 0, QTableWidgetItem(book.book_id))
            table.setItem(row_count, 1, QTableWidgetItem(name))
            table.setItem(row_count, 2, QTableWidgetItem(author))
            table.setItem(row_count, 3, QTableWidgetItem(quantity))
            table.setItem(row_count, 4, QTableWidgetItem(price))
            table.setItem(row_count, 5, QTableWidgetItem(self.image))

    def update_book(self):
        name = self.ui.input_name.text()
        author = self.ui.input_author.text()
        quantity = self.ui.input_quantity.text()
        price = self.ui.input_price.text()

        image_with_extension = os.path.basename(self.book.image)
        self.image = '.'.join(image_with_extension.split('.')[:-1])

        self.db.update_book(self.book.book_id, name, author,
                            quantity, price, self.book.image)

        # Insert update book in the admin table as well
        if self.admin_window:
            table = self.admin_window.ui.bookTableWidget
            table.setItem(self.row_num, 0, QTableWidgetItem(self.book.book_id))
            table.setItem(self.row_num, 1, QTableWidgetItem(name))
            table.setItem(self.row_num, 2, QTableWidgetItem(author))
            table.setItem(self.row_num, 3, QTableWidgetItem(quantity))
            table.setItem(self.row_num, 4, QTableWidgetItem(price))
            table.setItem(self.row_num, 5, QTableWidgetItem(self.image))

        self.ui.status_label.setText(PRODUCT_SUCCESSFULLY_ADDED_LABEL)

    def populate_input_boxes(self):
        self.ui.input_name.setText(self.book.name)
        self.ui.input_author.setText(self.book.author)
        self.ui.input_quantity.setText(self.book.quantity)
        self.ui.input_price.setText(self.book.price)
        self.ui.chooseFile_button.setText(self.book.image)


class OrderFormWindow(QMainWindow):
    def __init__(self, update=False):
        super().__init__()
        self.db = DatabaseAdmin()
        self.ui = orderForm_Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_buttton.setText("Update")

        if update:
            self.ui.add_buttton.clicked.connect(self.update_order)
        else:
            self.ui.add_buttton.clicked.connect(self.add_order)
        self.show()

    def add_order(self):
        text = self.ui.comboBox.currentText()
        # create new order

    def update_order(self):
        text = self.ui.comboBox.currentText()
        # update existing order


class OrderItemFormWindow(QMainWindow):
    def __init__(self, adminWindow=None, update=False, orderItem=None, row_num=None):
        super().__init__()
        self.db = DatabaseAdmin()
        self.adminWindow = adminWindow
        self.ui = orderItemForm_Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_buttton.setText("Update")

        if update:
            self.ui.add_buttton.clicked.connect(self.update_order)
        else:
            self.ui.add_buttton.clicked.connect(self.add_order)
        self.show()

    def add_order(self):
        text = self.ui.comboBox.currentText()
        # create new order

    def update_order(self):
        text = self.ui.comboBox.currentText()
        # update existing order


class UserFormWindow(QMainWindow):
    def __init__(self, adminWindow=None, update=False, user=None, row_num=None):
        super().__init__()
        self.db = DatabaseAdmin()
        self.adminWindow = adminWindow
        self.ui = userForm_Ui_MainWindow()
        self.ui.setupUi(self)

        if update:
            self.row_num = row_num
            self.user = user
            self.ui.input_name.setText(user.username)
            self.ui.input_password.setText(user.password)
            self.ui.add_buttton.setText("Update")
            self.ui.add_buttton.clicked.connect(self.update_user)
        else:
            self.ui.add_buttton.clicked.connect(self.add_user)
        self.show()

    def add_user(self):
        # create new order
        self.ui.status_label.setText("")
        username = self.ui.input_name.text()
        password = self.ui.input_password.text()
        if self.validate_password(password):
            user = self.db.signup(username, password, False)
            if user:
                self.ui.status_label.setText("User Successfully Added!")
                table = self.adminWindow.ui.userTableWidget
                rows = table.rowCount()
                table.setRowCount(rows + 1)
                table.setItem(rows, 0, QTableWidgetItem(user.userid))
                table.setItem(rows, 1, QTableWidgetItem(username))
                table.setItem(rows, 2, QTableWidgetItem(password))
                table.setItem(rows, 3, QTableWidgetItem(str(user.is_admin)))

    def update_user(self):
        # update existing order
        self.ui.status_label.setText("")
        username = self.ui.input_name.text()
        password = self.ui.input_password.text()
        if self.validate_password(password):
            self.db.update_user(self.user.userid, username, password, False)
            self.ui.status_label.setText("User Successfully Updated!")
            table = self.adminWindow.ui.userTableWidget
            table.setItem(self.row_num, 1, QTableWidgetItem(username))
            table.setItem(self.row_num, 2, QTableWidgetItem(password))

    def validate_password(self, password):
        # Password strength validation
        if password.isdigit():
            self.ui.status_label.setText("Password cannot be digits only!")
            return False
        return True


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
