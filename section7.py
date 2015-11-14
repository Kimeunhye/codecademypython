# 7.1
def spam():
    """문자열 'Eggs!'를 출력"""
    print "Eggs!"
spam()

# 7.2
def square(n):
    """숫자의 제곱 값을 반환"""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# 아홉 번째 줄에 함수 square를 호출하세요!
# 소괄호 사이에 숫자 10을 넣으셔야 합니다.
square(10)

# 7.3 (---오류남!!---)
def power(base, exponent):  # 여기에 매개변수를 추가하세요!
    result = base**exponent
    print "%d  %d  %d ." % (base, exponent, result)

power(37, 4)  # 여기에 인자를 추가하세요!

# 7.4
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

# 7.5
def by_three(m):
    if m % 3 == 0:
      cube = pow(m,3)
      return cube

    else:
     return false

# 7.6 (---모르겠음, 계속 오류남)
def cube(number):
    return number ** 4

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    return false

 # 7.7
 # sqrt(25)를 출력하도록, 파이썬에게 세 번째 줄에 물어보세요.

print sqrt(25)

# 7.8
# sqrt(25)를 출력하도록, 파이썬에게 세 번째 줄에 물어보세요.
import math
print math.sqrt(25)

# 7.9
# 세 번째 줄에 *오직* sqrt 함수만 math 모듈로부터 임포트하세요!
from math import sqrt
print sqrt(25)

# 7.10
from math import *

# 7.11
import math            # math 모듈을 불러옵니다
everything = dir(math) # math 모듈 안의 모든 것을 목록으로 만들어 변수에 저장합니다
print everything       # 변수 안에 담긴 리스트 전부를 출력합니다!

# 7.12
def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# 7.13
maximum = max(1, 2, 3)

print maximum

# 7.14
minimum = min(1, 2, 3)

print minimum

# 7.15
absolute = abs(-42)

print absolute

# 7.16
print type(30)
print type(3.5)
print type('유모차')

# 7.17
def shut_down(s):
    s = s.lower()
    if s ==  'yes':
        return "Shutting down..."
    elif s == 'no':
        return "Shutdown aborted!"

    else:
        return "Sorry, I didn't understand you."

# 7.18
from math import sqrt
print sqrt(13689)

# 7.19
def distance_from_zero(s):
    if type(s) == int or type(s) == float:
        return abs(s)

    else:
        return "Not an integer or float!"
