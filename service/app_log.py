# from datetime import datetime


# def log_file(func):
#     now = datetime.now()
#     now_str = now.strftime("%d/%m/%Y %H:%M:%S")
#     func_str = now_str + ' ' + str(func.__name__) + '\n'
#     stars = '\n' + '*' * 50 + '\n'

#     def inner():
#         with open("my_log.txt", 'a', encoding='utf-8') as f:
#             f.write(stars)
#             f.write(func_str)
#             f.write(str(func.__doc__))
#             f.write(stars)
#             func()
#     return inner

import os
import logging


def log_file(func):
    try:
        os.mkdir('log')
    except FileExistsError:
        pass

    def inner(**kwargs):
        logging.basicConfig(
            filename='log\\app.log',
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            encoding='utf-8',
            level=logging.INFO)
        logging.info(f'{func.__name__} | {func.__doc__}')
        try:
            func()
        except TypeError:
            func(**kwargs)
    return inner
