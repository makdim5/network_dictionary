# -*- coding: utf-8 -*-
import socket
import threading

from util.word_class import Word
from util.FileDictWorker import FileDictWorker
from util.TimeTask import Time

from util.modes import *
from server.DictionaryWorker import DictionaryWorker

THREADS_AMOUNT = 5

DEFAULT_GATEWAY = "0.0.0.0"
PORT = 11000
LENGTH_QUEUE = 10
BYTES_PER_PACKAGE = 4000


def serve_client(server):
    while True:
        user_socket, address = server.accept()

        print('\nIp address and port of the client are ' + str(address) +
              "\nClient descriptor: " + str(user_socket.fileno()) +
              "\nTime of connection: " + str(Time.get_data_and_time()) +
              "\nThread: " + threading.current_thread().name)

        # получение сообщения клиенту в виде пакета в байтах
        mode = user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8")

        while mode != EXIT_MODE:
            dictionary = FileDictWorker.get_dictionary_from_file()
            if mode == INSERT_MODE:
                word = user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8")
                word = FileDictWorker.parse_str_for_word_parts(word)
                DictionaryWorker.insert_word(Word(word[0], word[1]), dictionary)
                info = FileDictWorker.convert_dictionary_to_str(dictionary)
                user_socket.send(info.encode("utf-8"))


            elif mode == FIND_MODE:
                word_name = user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8")

                results = DictionaryWorker.find_word_in_dict(word_name, dictionary)
                if results:
                    info = FileDictWorker.convert_dictionary_to_str(results)
                else:
                    info = EMPTY_RESULT
                user_socket.send(info.encode("utf-8"))

            elif mode == REMOVE_MODE:
                word_parts = FileDictWorker.parse_str_for_word_parts(
                    user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8"))
                word = Word(word_parts[0], word_parts[1])

                DictionaryWorker.remove_word(word, dictionary)

            elif mode == EDIT_MODE:
                word_parts = FileDictWorker.parse_str_for_word_parts(
                    user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8"))
                edit_word_parts = FileDictWorker.parse_str_for_word_parts(
                    user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8"))

                DictionaryWorker.edit_word(word_parts, edit_word_parts, dictionary)

            elif mode == SORT_MODE:
                DictionaryWorker.sort_dictionary(dictionary)
                info = FileDictWorker.convert_dictionary_to_str(dictionary)
                user_socket.send(info.encode("utf-8"))
            elif mode == ALL_MODE:
                info = FileDictWorker.convert_dictionary_to_str(dictionary)
                user_socket.send(info.encode("utf-8"))

            FileDictWorker.put_dictionary_to_file(dictionary)

            mode = user_socket.recv(BYTES_PER_PACKAGE).decode("utf-8")

        print(f"\nClient {str(user_socket.fileno())} is out!!!")

        user_socket.shutdown(socket.SHUT_RDWR)
        user_socket.close()


def server_start_point():
    server = socket.socket(

        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(
        (DEFAULT_GATEWAY, PORT)  # localhost
    )

    threads = []

    for i in range(THREADS_AMOUNT):
        threads.append(threading.Thread(target=serve_client, args=(server,)))

    server.listen(LENGTH_QUEUE)
    print("Server is listening...\n",
          'Ip address and port of the server are ', server.getsockname(),
          " or ", socket.gethostname(),
          "\nServer descriptor: ", server.fileno())

    for item in threads:
        item.start()

    for item in threads:
        item.join()


if __name__ == "__main__":
    try:
        server_start_point()
    except Exception as ex:
        print(ex)
