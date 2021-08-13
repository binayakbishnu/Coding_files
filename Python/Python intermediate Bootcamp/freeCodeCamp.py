# t1 = ()
# t2 = tuple()
# t3 = ("ABC")    # shown as string
# t4 = ("ABC",)
# print(type(t1),type(t2),type(t3),type(t4))

# t = ('a','b','c','d','e')
# i1, *i2, i3 = t
# print(i1)
# print(i2)
# print(i3)

# d = {
#     "name": "Max",
#     "age": 20,
# }

# d2 = dict(name = "Mary", age = 27)

# print(d,d2)
# print(d.get("city", "City not entered"))

# d = {
#     "name": "Max",
#     "age": 20,
#     "city": "IND",
#     "job": "coder",
# }
# print(d.keys())
# print(d.values())
# print(d.items())

# for i in d.items():
#     print(i)
# for i in d.items():
#     m,n = i
#     print(m,n)
# for m,n in d.items():
#     print(m,n)

# print(d.pop("name"))

# s = set("Hello")
# print(s)
# print(len(s))

# s1 = {1,6,32,8}
# s2 = {4,2,8,0}
# print(s1)
# print(s2)
# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.issubset(s2))
# print(s1.symmetric_difference(s2))
# print(s1.intersection(s2))

# s = """Hello \
# World"""
# print(s)

# s = "ABABABBABA"
# print(s.count("ABA"))
# c = 0
# for i in range(len(s)):
#     if s[i:].startswith("ABA"):
#         c+=1
# print(c)

# s = "Hello how are you?"
# l = s.split()
# print(l)
# m = [i for i in s]
# print(m)
# for i in m:
#     if ' ' in m:
#         m.remove(' ')
# print(m)

# l = ["a"] * 6
# print(l)

####! from timeit import default_timer as timer
# start = timer()
# stop = timer()
# print(stop-start)

# a = "ABC"
# b = f"DEF {a*2}"
# print(b)

####! Counter ####
# from collections import Counter
# a = "ABCBABCBABCBAB"
# c = Counter(a)
# print(c)
# print(sorted(c))
# print(sorted(c.keys()))
# print(sorted(c.values()))
# print(sorted(c.items()))
# print(c.most_common(2))
# print(c.most_common(2)[0][0])
# print(list(c.elements()))

####! Namedtuple ####
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(2,3)
# print(pt)

# Student = namedtuple('Student', 'name,year,roll')
# st = Student('Binayak', 1, 155)
# print(st)
# print(st.name)
# print(st.roll)

####! OrderedDict ####
# from collections import OrderedDict
# d = OrderedDict()
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# d['a'] = 1
# print(d)
# d2 = {}
# d2['b'] = 2
# d2['c'] = 3
# d2['d'] = 4
# d2['a'] = 1
# print(d2)
# no difference but earlier versions had difference

####! from collections import defaultdict
# # default value if not set
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d)
# print(d['c']) # gives 0, not error
# # default value if not set
# d = defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d)
# print(d['c']) # empty list, not error

####! from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.append(3)

# d.appendleft(4)
# print(d)

# d.pop()
# print(d)
# d.popleft()
# print(d)

# d.extend([8,9,10])
# print(d)
# d.extendleft([11,12,13])
# print(d)

# d.rotate(1)
# print(d)
# d.rotate(-1)
# print(d)


####! Itertools ####
# iterables like lists
# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# print(list(prod))

# prod2 = product(a,b)
# print(prod2)
# l=[]
# for i in prod2:
#     print(i)
#     l.append(i[0]*i[1])
# print(l)

# a = [1,2]
# b = [3]
# prod3 = product(a,b,repeat=2)
# print(list(prod3))

# from itertools import permutations
# a = [1,2,3,4]
# perm = permutations(a)
# print(list(perm))

# perm2 = permutations(a,2)
# print("Perm with 2 at a time\n",list(perm2))

# from itertools import combinations
# a = [1,2,3,4]
# comb = combinations(a,2)
# print("Comb with 2 at a time\n",list(comb))

# from itertools import combinations, combinations_with_replacement
# a = [1,2,3,4]
# comb = combinations_with_replacement(a,2)
# print("Comb with 2 at a time + replacement\n",list(comb))

# from math import comb
# print(comb(10,10))

# from itertools import accumulate
# a = [1,2,3,4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

#! import operator
# acc2 = accumulate(a,func=operator.mul)
# print(a)
# print(list(acc2))

# a2 = [1,2,5,3,4]
# acc3 = accumulate(a2,func=max)
# print(a2)
# print(list(acc3))

# from itertools import groupby
# a = [1,2,3,4]
# def smaller_than_3(x):
#     return (x<3)
# g = groupby(a, key=smaller_than_3)
# print(g)
# for key, value in g:
#     print(key,list(value))

# with lambda function
# g = groupby(a, key = lambda x: x<3)
# for key, value in g:
#     print(key,list(value))

# from itertools import count, cycle, repeat
# for i in count(10):
#     print(i)
#     if i==15:
#         break

# a = [1,2,3]
# c = 0
# for i in cycle(a):
#     print(i)
#     c += 1
#     if c==10:
#         break

# for i in repeat(9,4):
#     print(i)

####! lambda functions ####
# add10 = lambda x: x+10
# print(add10(10))

# mult = lambda x,y: print(x*y)
# mult(2,7)

# points2d = [(1,2),(15,1),(5,-1),(10,4)]
# points2d_sorted = sorted(points2d)
# points2d_sorted2 = sorted(points2d,key=lambda x: x[1])
# def sort_by_y(x):
#     return x[1]
# points2d_sorted3 = sorted(points2d,key = sort_by_y)
# points2d_sorted4 = sorted(points2d, key = lambda x: x[0] + x[1])

# print(points2d)
# print(points2d_sorted)
# print(points2d_sorted2)
# print(points2d_sorted3) # same
# print(points2d_sorted4)

####! map ####
# a = [1,2,3,4]
# b = map(lambda x:2*x, a)
# print(list(b))

# c = [2*i for i in a]
# print(c) # same

####! filter ####
# a = [1,2,3,4,5,6]
# b = filter(lambda x:x%2==0, a)
# print(list(b))

# c = [i%2==0 for i in a]
# print(c)

# d = [i for i in a if i%2==0]
# print(d)

####! reduce ####
# from functools import reduce
# a = [1,2,3,4,5,6]
# prod_a = reduce(lambda x,y:x*y, a)
# print(prod_a)

####! Exception handling ####
# x =-7
# if x<0:
#     raise Exception("Should be positive")
# assert(x>=0), 'x not positive'
# try:
#     a = 5/0
#     s = 5 + 'H'
###//###
# except:
#     print('Division by zero')
# better to use except Exception and not only exception
###//###
# except Exception as e:
#     print(e)
####//###
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as f:
#     print(f)
# else:
#     print('Everything is fine')
# finally:
#     print('Moving on...')

####! user-defined exception
# class toohigh(Exception):
#     pass

# def checking(x):
#     if x>100:
#         # raise Exception('Value too high')
#         raise toohigh("Value too high")

# try:
#     checking(980)
# except toohigh as t:
#     print(t)

# x=980
# if x>100:
#     raise toohigh("Value too high")

####! Logging ####
import logging




