import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                               QMenuBar, QPushButton, QTableWidget,
                               QTableWidgetItem, QTabWidget, QVBoxLayout,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Layout
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
        table1 = self.create_table()
        table2 = self.create_table()
        self.tab_widget.addTab(table1, "Table 1")
        self.tab_widget.addTab(table2, "Table 2")

        # Region D: Buttons
        button_layout = QHBoxLayout()
        for i in range(5):  # Just as an example, you can add as many buttons as you want
            btn = QPushButton(f"Button {i+1}")
            button_layout.addWidget(btn)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_table(self):
        # Region B: Table with checkable rows
        table = QTableWidget(10, 5)  # Example: 10 rows, 5 columns
        for row in range(10):
            check_item = QTableWidgetItem()
            check_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            check_item.setCheckState(Qt.Unchecked)
            table.setItem(row, 0, check_item)
            for col in range(1, 5):
                item = QTableWidgetItem(f"Item {row+1}-{col+1}")
                table.setItem(row, col, item)
        return table

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

