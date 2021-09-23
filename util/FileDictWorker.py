from util.word_class import Word

WORDS_FILE = r"../in.txt"
SPECIFIC_CHAR = "^"


class FileDictWorker:
    @classmethod
    def get_dictionary_from_file(cls, file=WORDS_FILE):
        with open(file, "r", encoding="utf-8") as file_out:
            dictionary = cls.convert_to_dictionary(file_out.readlines())
        return dictionary

    @classmethod
    def put_dictionary_to_file(cls, words, file=WORDS_FILE):
        with open(file, "w", encoding="utf-8") as file_in:
            file_in.write(cls.convert_dictionary_to_str(words))

    @classmethod
    def convert_to_dictionary(cls, words):
        new_words = []
        for item in words:
            word_data = cls.parse_str_for_word_parts(item)
            new_words.append(Word(word_data[0], word_data[1]))

        return new_words

    @classmethod
    def convert_dictionary_to_str(cls, dictionary):
        string = ""
        for item in dictionary:
            string += cls.parse_word_to_str(item)

        return string

    @staticmethod
    def parse_str_for_word_parts(string):
        simple_index = 0
        for i in range(len(string)):
            if string[i] == SPECIFIC_CHAR:
                simple_index = i
                break
        return string[:simple_index], string[simple_index + 1:]

    @staticmethod
    def parse_word_to_str(word):
        word_value = word.get_value() if "\n" in word.get_value()\
                                        else word.get_value() + "\n"
        return word.get_key() + SPECIFIC_CHAR + word_value

    @classmethod
    def convert_dict_str_real_dict(cls, string):
        words = []
        i = 0
        while i < len(string):
            word = ""
            meaning = ""
            while string[i] != SPECIFIC_CHAR:
                word += string[i]
                i += 1

            i += 1

            while i < len(string) and string[i] != "\n":
                meaning += string[i]
                i += 1
            i += 1

            words.append(Word(word, meaning))

        return words
#
# with open(WORDS_FILE, "r", encoding="utf-8") as file_out:
#         print(file_out.readlines())