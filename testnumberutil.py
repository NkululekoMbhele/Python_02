"""

>>> import numberutil

>>> numberutil.aswords(-1)
'ninety nine'
>>> numberutil.aswords(1000)
'ten hundred'
>>> numberutil.aswords(209)
'two hundred and nine'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(187)
'one hundred and eighty seven'
>>> numberutil.aswords(50)
'fifty'
>>> numberutil.aswords(11)
'eleven'
>>> numberutil.aswords(980)
'nine hundred and eighty'

"""
import doctest
doctest.testmod(verbose=True)
