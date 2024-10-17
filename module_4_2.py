#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# создаю функцию
def my_test_function():
    # создаю вложенную функцию
    def inner_function():
        print('я в области видимости функции my_test_function')
    # вызов вложенной функции
    inner_function()
# вызов основной функции
my_test_function()

