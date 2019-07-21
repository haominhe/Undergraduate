Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # Problem 0
temp = 100
>>> ftemp = temp * 9/5 +32
>>> ftemp
212.0
>>> ctemp = (ftemp - 32) * 5/9
>>> ctemp
100.0
>>> 
>>> # Problem 1
>>> MP3 = 5
>>> CD = 15
>>> 4 * CD + 6 * MP3
90
>>> 
>>> # Problem 2
>>> x = 100
>>> x = x * 10
>>> x = x + x
>>> x
2000
>>> 
>>> # Problem 3
>>> x = 100
>>> x *= 10
>>> x += x
>>> x
2000
>>> 
>>> # Problem 4
>>> initial = 0.01
>>> doubling = 2
>>> days = 30
>>> total = initial * doubling **(days - 1)
>>> total
5368709.12
>>> # Yes, I see the pattern. The Python code tells me that 1 cent doubling for a month is much greater than $1 million dollars. 5368709.12 > 1000000. So I choose doubling 1 cent for a month.
>>> 
>>> # Problem xc
>>> # I choose the immediate $10 million because 10000000 > 5368709.12.
>>> 
>>> # Problem xc
>>> Teams = 64
>>> Ways = 2**(Teams - 1)
>>> Ways
9223372036854775808
>>> # There are more stars in the universe than ways of filing out an NCAA "March Madness" bracket form. From google, there are 10**22 to 10**24 stars in the Universe which is greater than the number above 9223372036854775808. Roughly comparison: 10**22 > 9**19.

>>> 
