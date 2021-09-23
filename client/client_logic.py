# -*- coding: utf-8 -*-
import socket
from client.view.action_wins.ClientFormWorker import ClientFormWorker
from util.FileDictWorker import FileDictWorker
from util.word_class import Word
from client.view.action_wins.welcomeWin import WelcomeWin
from client.view.action_wins.card_word_WGT import WordWidget

from util.modes import *

SERVER_ADDRESS = "127.0.0.1"  # в курсовой обращение по доменному имени
PORT = 11000
BYTES_PER_PACKAGE = 4000


class Client:
    def __init__(self):
        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.app = ClientFormWorker()
        self.server_dns_name = ""  # HP-PYMAK
        self.welcome_win = WelcomeWin()
        self.welcome_win.show()
        self.welcome_win.pushButton.clicked.connect(self.welcome_commands)
        self.welcome_win.lineEdit.returnPressed.connect(self.welcome_commands)

        self.app.searchBtn.clicked.connect(self.find_mode_actions)
        self.app.lineEdit.returnPressed.connect(self.find_mode_actions)

        self.app.sortBtn.clicked.connect(self.sort_mode_actions)

        self.app.addWordBtn.clicked.connect(self.insert_mode_actions)

    def welcome_commands(self):
        try:
            self.server_dns_name = self.welcome_win.lineEdit.text()
            self.connect()
            self.welcome_win.close()
            self.app.show()
            self.all_mode_actions()
        except socket.gaierror:
            self.welcome_win.warningMsg.show()
            self.welcome_win.lineEdit.clear()
# сетевые функции
    def connect(self):
        self.client.connect(
            (self.server_dns_name, PORT)
        )

    def send(self, msg):
        self.client.send(msg.encode("utf-8"))

    def receive(self):
        return self.client.recv(BYTES_PER_PACKAGE).decode("utf-8")

# Функции для отправки запросов и обработки ответов в главном окне
    def all_mode_actions(self):
        self.send(ALL_MODE)
        info = self.receive()
        dictionary = FileDictWorker.convert_dict_str_real_dict(info)
        self.app.clear_cards(self.app.allWordsLay)
        self.app.add_cards(self.app.allWordsLay, dictionary, self)

    def find_mode_actions(self):
        if not self.app.lineEdit.text():
            return
        self.send(FIND_MODE)
        self.send(self.app.lineEdit.text())
        self.app.clear_cards(self.app.searchWLay)
        answers = self.receive()
        if answers != EMPTY_RESULT:
            self.app.add_cards(self.app.searchWLay,
                               FileDictWorker.convert_dict_str_real_dict(answers),
                               self)
        else:
            self.app.add_cards(self.app.searchWLay, [Word(
                self.app.lineEdit.text() + " не найдено.", ""
            )], self)

        for i in range(self.app.searchWLay.count()):
            self.app.searchWLay.itemAt(i).widget().changeBtn.hide()
            self.app.searchWLay.itemAt(i).widget().deleteBtn.hide()

    def sort_mode_actions(self):
        self.send(SORT_MODE)
        dictionary = FileDictWorker.convert_dict_str_real_dict(self.receive())
        self.app.clear_cards(self.app.allWordsLay)
        self.app.add_cards(self.app.allWordsLay, dictionary, self)

    def insert_mode_actions(self):
        adder = WordWidget(self)
        adder.changeBtn.hide()
        adder.deleteBtn.hide()
        adder.setWindowTitle("Добавление слова")
        adder.lineEdit.setReadOnly(False)
        adder.textEdit.setReadOnly(False)
        adder.show()
        adder.lineEdit.returnPressed.connect(
            lambda: self.add_word(adder))

    def add_word(self, adder):
        self.send(INSERT_MODE)
        msg = adder.lineEdit.text() + "^" + adder.textEdit.toPlainText()
        adder.close()
        self.send(msg)
        info = self.receive()
        dictionary = FileDictWorker.convert_dict_str_real_dict(info)
        self.app.clear_cards(self.app.allWordsLay)
        self.app.add_cards(self.app.allWordsLay, dictionary, self)

    def open_editing_word(self, wordCard):
        self.send(EDIT_MODE)
        adder = WordWidget(self)
        adder.changeBtn.hide()
        adder.deleteBtn.hide()
        adder.setWindowTitle("Редактирование слова")
        adder.show()

        adder.lineEdit.setText(wordCard.lineEdit.text())
        adder.lineEdit.setReadOnly(False)
        adder.textEdit.setReadOnly(False)
        adder.textEdit.setText(wordCard.textEdit.toPlainText())
        adder.lineEdit.returnPressed.connect(
            lambda: self.edit_word(wordCard, adder)
        )

    def edit_word(self, wordCard, adder):
        self.send(wordCard.lineEdit.text() +
                  "^" + wordCard.textEdit.toPlainText())
        wordCard.lineEdit.setText(adder.lineEdit.text())
        wordCard.textEdit.setText(adder.textEdit.toPlainText())

        msg = adder.lineEdit.text() + "^" + adder.textEdit.toPlainText()
        adder.close()
        self.send(msg)

    def remove_word(self, wordCard):
        self.send(REMOVE_MODE)
        self.send(wordCard.lineEdit.text() +
                  "^" + wordCard.textEdit.toPlainText())

        wordCard.hide()
