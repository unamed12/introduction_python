# -*- coding: utf-8 -*-
# string_middle은 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 만들어 보세요. 
# 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
# 예를 들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.

def string_middle(str):
    # 함수를 완성하세요
    temp = int(len(str)/2)
    if len(str) % 2 == 0:
        return str[temp-1] + str[temp]
    else:
        return str[temp]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("pow32er"))

# 다른 풀이 

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))





#####