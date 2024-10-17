#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf

def divide (first, second):
    if second == 0:
        return inf # возвращаем бесконечность импортирована из math
    else:
        return first/second # возвращаем результат деления

