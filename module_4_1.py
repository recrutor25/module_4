#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# импортирую модули
from fake_math import divide as fk
from true_math import divide as tr
#вызываю функции с параметрами
result1 = fk(69, 3)
result2 = fk(3, 0)
result3 = tr(49, 7)
result4 = tr(15, 0)
# вывожу резильтат
print(result1)
print(result2)
print(result3)
print(result4)
