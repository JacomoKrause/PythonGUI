import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                               QMenuBar, QPushButton, QTableWidget,
                               QTableWidgetItem, QTabWidget, QVBoxLayout,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QVBoxLayout()

        # Region A: Menu Bar
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")
        self.setMenuBar(menu_bar)

        # Region C: Tabs
        self.tab_widget = QTabWidget(self)
        layout.addWidget(self.tab_widget)

        # Adding tables to tabs
        self.table1 = self.create_table()
        self.table2 = self.create_table()
        self.tab_widget.addTab(self.table1, "Table 1")
        self.tab_widget.addTab(self.table2, "Table 2")

        # Region D: Buttons
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Row")
        self.remove_button = QPushButton("Remove Row")
        self.toggle_button = QPushButton("Toggle Button")
        
        self.add_button.clicked.connect(self.add_row)
        self.remove_button.clicked.connect(self.remove_row)
        self.toggle_button.clicked.connect(self.toggle_new_button)

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.remove_button)
        self.button_layout.addWidget(self.toggle_button)

        layout.addLayout(self.button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.new_button = None  # Placeholder for a new button to be toggled

    def create_table(self):
        table = QTableWidget(10, 5)
        for row in range(10):
            self.add_table_row(table, row)
        return table

    def add_table_row(self, table, row):
        check_item = QTableWidgetItem()
        check_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        check_item.setCheckState(Qt.Unchecked)
        table.setItem(row, 0, check_item)
        for col in range(1, 5):
            item = QTableWidgetItem(f"Item {row+1}-{col+1}")
            table.setItem(row, col, item)

    def add_row(self):
        current_table = self.tab_widget.currentWidget()
        current_table.insertRow(current_table.rowCount())
        self.add_table_row(current_table, current_table.rowCount() - 1)

    def remove_row(self):
        current_table = self.tab_widget.currentWidget()
        current_row = current_table.currentRow()
        if current_row != -1:  # If a row is selected
            current_table.removeRow(current_row)

    def toggle_new_button(self):
        if not self.new_button:
            self.new_button = QPushButton("New Button")
            self.button_layout.addWidget(self.new_button)
        elif self.new_button.isVisible():
            self.new_button.hide()
        else:
            self.new_button.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
