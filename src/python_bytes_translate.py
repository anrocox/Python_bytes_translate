#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

How to define a mapping table characters for use with a bytes object in Python?

¿Cómo definir una tabla de mapeo de caracteres para usar en un objeto bytes
de Python?
'''

#create a str
b = b'in addition to case folding'
print(b)

#generates a bytes object of length 256 with translation table. The two
#arguments must be bytes objects of equal length. Each character in first
#arg will be mapped to the character at the same position in the second arg.
b_table = bytes.maketrans(b'abcdef', b'uvwxyz')
print(type(b_table))
print(b_table)

#generates a copy of the bytes or bytearray object where all characters have
#been mapped through the map of 'b_table', which must be a bytes object of
#length 256.
b_new = b.translate(b_table)
print(b_new)

#The second parameter allows to define the characters that should be removed
#in the bytes or bytearray object
b_new = b.translate(b_table, b'o i')
print(b_new)
