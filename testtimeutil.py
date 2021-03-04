"""
>>> import timeutil  
>>> timeutil.validate("11:5 p.m.")
False
>>> timeutil.validate("111:1 p.m.")
False
>>> timeutil.validate("12 32 a.m")
False
>>> timeutil.validate("12:61 a.m.")
False
>>> timeutil.validate("5:01 am")
False
>>> timeutil.validate("1:45")
False

"""
import doctest
doctest.testmod(verbose=True)