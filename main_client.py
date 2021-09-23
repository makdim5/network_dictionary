# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from client.client_logic import Client
from util.modes import EXIT_MODE
from qt_material import apply_stylesheet

try:
        app = QApplication(sys.argv)
        client = Client()
        apply_stylesheet(app, theme='light_blue.xml')
        app.exec_()
        client.send(EXIT_MODE)

except Exception as ex:
        print(ex)
