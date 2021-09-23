#!/usr/bin/python3
# -*- coding: utf-8 -*-
from util.word_class import Word


class DictionaryWorker:
    @classmethod
    def add_word(cls, word, dictionary):
        if cls.__check_parameters(word, dictionary):
            dictionary.append(word)

    @classmethod
    def edit_word(cls, word, edit_word, dictionary):
        for i in range(len(dictionary)):
            item_key = dictionary[i].get_key()
            item_val = dictionary[i].get_value()
            if item_key == word[0] and word[1] in item_val:
                dictionary[i].set_key(edit_word[0])
                dictionary[i].set_value(edit_word[1])
                break

    @classmethod
    def insert_word(cls, word, dictionary):
        cls.add_word(word, dictionary)
        cls.sort_dictionary(dictionary)

    @classmethod
    def find_word_in_dict(cls, word_name, dictionary):
        results = []
        for item in dictionary:
            if item.get_key().lower() == word_name.lower():
                results.append(item)

        return results

    @classmethod
    def remove_word(cls, word, dictionary):
        for item in dictionary:
            if item.get_key() == word.get_key() and item.get_value() == item.get_value():
                dictionary.remove(item)
                break

    @staticmethod
    def sort_dictionary(dictionary):
        for i in range(1, len(dictionary)):
            fixed_item = dictionary[i]
            j = i - 1
            while j >= 0 and fixed_item.get_key().lower() < dictionary[j].get_key().lower():
                dictionary[j + 1] = dictionary[j]
                j -= 1
            dictionary[j + 1] = fixed_item

    @staticmethod
    def __check_parameters(word, dictionary):
        return (True if isinstance(word, Word) and isinstance(dictionary, list)
                else False)
