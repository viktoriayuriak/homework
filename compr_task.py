from operator import ne

from timeit import Timer
from random import random, seed

def h_dist0(s1,s2):
    ''' For loop '''
    tot = 0
    for d1, d2 in zip(s1, s2):
        if d1 != d2:
            tot += 1
    return tot

def h_dist1(s1, s2):
    '''While Loop'''
    tot = 0
    d1 = {}
    d2 ={}
    while d1== True and d2 == True:
        zip(s1, s2)
        if d1 != d2:
            tot += 1
    return tot

def h_dist2(s1,s2):
    ''' List comprehension '''
    return sum([dgt1 != dgt2 for dgt1, dgt2 in zip(s1, s2)])

def h_dist3(s1,s2):
    ''' Generator expression '''
    return sum(dgt1 != dgt2 for dgt1, dgt2 in zip(s1, s2))


def h_dist4(s1,s2):
    ''' Dict comprehension '''
    return sum({dgt1 != dgt2 for dgt1, dgt2 in zip(s1, s2)})

def h_dist5(s1,s2):
    ''' Set comprehension '''
    return sum({dgt1 != dgt2 for dgt1, dgt2 in zip(s1, s2)})



funcs = [
    h_dist0,
    h_dist1,
    h_dist2,
    h_dist3,
    h_dist4,
    h_dist5
]

# ------------------------------------

def check_full():
    print ('Testing all functions with strings of length', len(s1))
    for func in funcs:
        print ('%s:%s\n%d\n' % (func.__name__, func.__doc__, func(s1, s2)))

def check():
    print ('Testing all functions with strings of length', len(s1))
    print ([func(s1, s2) for func in funcs], '\n')

def time_test(loops=10000, reps=3):
    ''' Print timing stats for all the functions '''
    slen = len(s1)
    print ('Length = %d, Loops = %d, Repetitions = %d' % (slen, loops, reps))

    for func in funcs:
        #Get function name and docstring
        fname = func.__name__
        fdoc = func.__doc__

        print ('\n%s:%s' % (fname, fdoc))
        t = Timer('%s(s1, s2)' % fname, 'from __main__ import s1, s2, %s' % fname)
        results = t.repeat(reps, loops)
        results.sort()
        print (results)
    print ('\n' + '- '*30 + '\n')

def xrange(x):

    return iter(range(x))

def make_strings(n, r=0.5):
    print ('r:', r)
    s1 = 'a' * n
    s2 = ''.join(['b' if random() < r else 'a' for _ in xrange(n)])
    return s1, s2

# ------------------------------------

seed(37)

s1, s2 = make_strings(100)
#print '%s\n%s\n' % (s1, s2)
check()
time_test(10000)

s1, s2 = make_strings(100, 0.1)
check()
time_test(10000)

s1, s2 = make_strings(100, 0.9)
check()
time_test(10000)

s1, s2 = make_strings(10)
check()
time_test(50000)

s1, s2 = make_strings(1000)
check()
time_test(1000)