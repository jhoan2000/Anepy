# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:19:52 2023

@author: Estudiante
"""

import re

d = '1, 1, 2, 20, 30, 219498.39 '

patron = r'\b\d+.{1,3}\b'

datos = re.findall(patron, d)

print(datos)