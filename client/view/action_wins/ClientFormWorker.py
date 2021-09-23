# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from client.view.action_wins.card_word_WGT import WordWidget

from client.view.view_ui.mainUI import Ui_Form


class ClientFormWorker(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.allPageBtn.clicked.connect(
            self.allPageBtn_actions)
        self.searchPageBtn.clicked.connect(
            self.searchPageBtn_actions)
        self.aboutPageBtn.clicked.connect(
            self.aboutPageBtn_actions
        )
        self.lineEdit.setPlaceholderText("Введите термин для поиска")

    def allPageBtn_actions(self):
        self.pagesWGT.setCurrentIndex(0)
        self.searchPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.allPageBtn.setStyleSheet("background-color: rgb(202, 212, 255);")
        self.aboutPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")

    def searchPageBtn_actions(self):
        self.pagesWGT.setCurrentIndex(1)
        self.allPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchPageBtn.setStyleSheet("background-color: rgb(202, 212, 255);")
        self.aboutPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")

    def aboutPageBtn_actions(self):
        self.pagesWGT.setCurrentIndex(2)
        self.allPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchPageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aboutPageBtn.setStyleSheet("background-color: rgb(202, 212, 255);")

    def create_word_card(self, word, client):
        word_card = WordWidget(client)
        word_card.lineEdit.setText(word.get_key())
        word_card.textEdit.setText(word.get_value())

        return word_card



    def add_cards(self, layout, dictionary, client):
        for item in dictionary:
            word_card = self.create_word_card(item, client)
            layout.addWidget(word_card)
            word_card.show()

    def clear_cards(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
