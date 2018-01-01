# -*- coding: utf-8 -*-
# 두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 반환해주는 gcdlcm 함수를 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 gcdlcm(3,12)가 입력되면, [3, 12]를 반환해주면 됩니다.


def gcdlcm(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
        return abs(m)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))



import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)
