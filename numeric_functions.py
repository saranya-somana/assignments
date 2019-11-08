Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> abs(5)
5
>>> import math
>>> math.ceil(56.12)
57
>>> math.ceil(-10.89)
-10
>>> math.e
2.718281828459045
>>> math.exp(7)
1096.6331584284585
>>> math.e**7
1096.6331584284583
>>> math.floor(89.24)
89
>>> math.floor(-19.90)
-20
>>> math.sqrt(16)
4.0
>>> math.sqrt(-25)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    math.sqrt(-25)
ValueError: math domain error
>>> math.sqrt(25)
5.0
>>> math.log(5)
1.6094379124341003
>>> math.log(math.e)
1.0
>>> math.log10(10)
1.0
>>> max(1,3,5,10,2,6)
10
>>> min()-1,-10,67
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    min()-1,-10,67
TypeError: min expected 1 arguments, got 0
>>> min(-10,-1,78)
-10
>>> round(10.563832027, 3)
10.564
>>> modf(15.986)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    modf(15.986)
NameError: name 'modf' is not defined
>>> math.modf(198.473837)
(0.4738370000000032, 198.0)
>>> math.pow(2,3)
8.0
>>> math.hypot(12, 13)
17.69180601295413
>>> math.hypot(1,2)
2.23606797749979
>>> math.degrees(2)
114.59155902616465
>>> math.radians(2)
0.03490658503988659
>>> 
