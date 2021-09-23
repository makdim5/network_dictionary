# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget

from client.view.view_ui.wordWGT_UI import Ui_Form


class WordWidget(QWidget, Ui_Form):
    def __init__(self, par):
        super().__init__()
        self.setupUi(self)

        self.__parent = par

        self.deleteBtn.clicked.connect(lambda: self.__parent.remove_word(self))
        self.changeBtn.clicked.connect(lambda: self.__parent.open_editing_word(self))
