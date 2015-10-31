# 5.1

bool_one = True

bool_two = True

bool_three = False

bool_four = False

bool_five = False

# 5.2
bool_one = False

bool_two = True

bool_three = False

bool_four = True

bool_five = False

# 5.3
# 변수의 값이 참이 되도록 만드세요!
bool_one = 5 != 2+2

# 변수의 값이 거짓이 되도록 만드세요!
bool_two = 2>3

# 변수의 값이 참이 되도록 만드세요!
bool_three = 3<4

# 변수의 값이 거짓이 되도록 만드세요!
bool_four = 3 == 4

# 변수의 값이 참이 되도록 만드세요!
bool_five = 3>=2

# 5.4
"""
     불린 연산자(Boolean Operators)
-----------------------------------------------
True 그리고(and) True의 결과는 True
True 그리고(and) False의 결과는 False
False 그리고(and) True의 결과는 False
False 그리고(and) False의 결과는 False

True 또는(or) True의 결과는 True
True 또는(or) False의 결과는 True
False 또는(or) True의 결과는 True
False 또는(or) False의 결과는 False

True 부정(not)의 결과는 False
False 부정(not)의 결과는 True

"""
# 5.5
bool_one = False

bool_two = False

bool_three = False

bool_four = True

bool_five = True

# 5.6
bool_one = True

bool_two = True

bool_three = False

bool_four = True

bool_five = False

# 5.7
bool_one = False

bool_two = True

bool_three = True

bool_four = True

bool_five = False

# 5.8
bool_one = False

bool_two = True

bool_three = True

bool_four = True

bool_five = False

# 5.9
# 변수의 값이 거짓이 되도록 만드세요!
bool_one = False and True

# 변수의 값이 참이 되도록 만드세요!
bool_two = not False

# 변수의 값이 거짓이 되도록 만드세요!
bool_three = False or False

# 변수의 값이 참이 되도록 만드세요!
bool_four = True and not False

# 변수의 값이 참이 되도록 만드세요!
bool_five = (True or True) or False

# 5.10
response = N

answer = "Left"
if answer == "Left":
    print "이런, 방을 잘못 들어왔습니다!"

# 위의 print 명령문이 console에 출력될까요?
# 그럴거 같다면 변수 response에 'Y'를, 그렇지 않다면 'N'을 값으로 지정하세요.

# 5.11
def using_control_once():
    if 3>2:
        return "Success #1"

def using_control_again():
    if  5>4:
        return "Success #2"

print using_control_once()
print using_control_again()

# 5.12
answer = "이 정돈 그냥 긁힌거지!"

def black_knight():
    if answer == "이 정돈 그냥 긁힌거지!":
        return True
    else:
        return  False      # False 값을 반환하도록 만드세요

def french_soldier():
    if answer == "저리 꺼져, 그렇지 않으면 또 다시 본떼를 보여주마!":
        return True
    else:
        return  Flase     # False 값을 반환하도록 만드세요

# 5.13
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

# 5.14
def the_flying_circus(answer):
    # 여기서 부터 코딩을 시작하세요!
    if answer > 4:
        return True
    elif answer <4:
        return False
    else:
        return True
print greater_less_equal_5(4)

bool_one = False and True
print bool_one
