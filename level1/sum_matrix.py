# -*- coding: utf-8 -*-
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
# 2개의 행렬을 입력받는 sumMatrix 함수를 완성하여 행렬 덧셈의 결과를 반환해 주세요.
# 예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 
# 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.(어떠한 행렬에도 대응하는 함수를 완성해주세요.)

def sumMatrix(A,B):
    answer = []
    for i in range(len(A)):
        temp = list()
        for j in range(len(A[i])):
            temp.append(A[i][j] + B[i][j])
        answer.append(temp)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

# 다른 풀이

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2,5], [2,3,2]], [[3,4,4],[5,6,5]]))

#다시 풀이 

def sumMatrix(A,B):
    answer = []
    for a, b in zip(A, B):
        temp = list()
        answer.append(temp)
        for c, d in zip(a, b):
            temp.append(c + d)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2,6], [2,3,7]], [[3,4,9],[5,6,8]]))

# 다른 풀이

def sumMatrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))



###