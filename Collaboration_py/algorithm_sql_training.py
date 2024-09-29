# training
# BJ1316
# import sys
# number = int(sys.stdin.readline())
# text = [str(sys.stdin.readline().strip()) for i in range(number)]
# group_word = 0
# # 입력받은 알파벳을 순서대로 조사한다.
# for i in text:
#     check = 0
#     for _ in i:
#         # 알파벳 순서대로 카운트 세기
#         count_num = i.count(_)
#         # 카운트센 알파벳 첫인덱스 찾기
#         find_num = i.find(_)
#         # [첫인덱스:첫인덱스+카운트] 가 동일알파벳이 아니면 그룹단어가 아니다
#         if i[find_num:find_num + count_num] != _ * count_num:
#             check += 1
#             break
#
#     if check == 0:
#         group_word += 1
#
# print(group_word)

# BJ25206
# 졸업조건 전공평점 3.3 이상 (학점 * 과목평점)합 / 학점의 총합
# import sys
# grade_dc = {
#     "A+" : 4.5,
#     "A0" : 4.0,
#     "B+" : 3.5,
#     "B0" : 3.0,
#     "C+" : 2.5,
#     "C0" : 2.0,
#     "D+" : 1.5,
#     "D0" : 1.0,
#     "F" : 0.0
# }
# grade_subject_sum = 0
# grade_sum = 0
#
# for i in range(20):
#     grade_list = sys.stdin.readline().strip().split()
#     if grade_list[-1] == "P":
#         continue
#     grade_sum += float(grade_list[-2]) # 학점의 총합
#     grade_subject_sum += (float(grade_list[-2]) * grade_dc[grade_list[-1]]) # 학점 * 과목평점의 합
#
# grade_avg = grade_subject_sum / grade_sum
# print(grade_avg)

# BJ2738 두 행렬의 덧셈
# import sys
# n, m = map(int, sys.stdin.readline().split())
#
# matrix_a = []
# matrix_b = []
# matrix_sum = []
#
# for i in range(n):
#     matrix_a.append(list(sys.stdin.readline().split()))
#
# for j in range(n):
#     matrix_b.append(list(sys.stdin.readline().split()))
#     matrix_sum.append(('a '* m).split())
#     for k in range(m):
#         matrix_sum[j][k] = int(matrix_a[j][k]) + int(matrix_b[j][k])
#
# for i in range(n):
#     print(*matrix_sum[i])

# BJ2566 최댓값
# import sys
# max_num = 0
# matrix_list = []
# where_col_row = "1 1"
#
# for i in range(9):
#     matrix_list.append(list(sys.stdin.readline().split()))
#     for j in range(9):
#         if int(matrix_list[i][j]) > max_num:
#             max_num = int(matrix_list[i][j])
#             where_col_row = f"{i+1} {j+1}"
#
# print(max_num)
# print(where_col_row)

# BJ10798 세로읽기
# import sys
# matrix_list = []
# for i in range(5):
#     matrix_list.append(list(sys.stdin.readline().split()))
#
# text = ""
# for i in range(15):
#     for j in range(5):
#         if len(matrix_list[j][0]) > i:
#             text += matrix_list[j][0][i]
#
# print(text)

# BJ2563 색종이
# import sys
# count = int(input())
# matrix_list = []
# area = 0
# for i in range(count):
#     x, y = map(int, sys.stdin.readline().split())
#     matrix_list.append((x, y))  # 좌표 저장
#
# paper = [[0] * 100 for _ in range(100)]  # 도화지는 100x100으로 가정
#
# for x, y in matrix_list:
#     for i in range(x, x + 10):
#         for j in range(y, y + 10):
#             paper[i][j] = 1  # 색종이가 붙은 부분 표시
#
# for row in paper:
#     area += sum(row)
#
# print(area)

# BJ 2745 진법 변환 (N진법 → 10진법)
# number, b = input().split()  # b진법 수 n
# b = int(b)
#
# numbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# answer = 0
#
# for i in range(len(number)):
#     if number[-(i+1)] in numbers:  # 첫째 자리부터
#         answer += (b ** i) * (numbers.find(number[-(i+1)]) + 10)
#     else:
#         answer += (b ** i) * int(number[-(i+1)])
#
# print(answer)

# BJ 11005 진법 변환2 (10진법 → N진법)
# number, b = input().split() # 10진법 number를 b진법으로 변환
# b = int(b)
# number = int(number)
# numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# answer = ""
# namugy = 0
# while number > 0:
#     namugy = number % b
#     number = number // b
#     answer = (numbers[namugy] + answer)
#
# print(answer)

# BJ 2720
# import sys
# quarter = 25
# dime = 10
# nickel = 5
# penny = 1
# temp = ""
# case_list = []
# test = int(input())
# for i in range(test):
#     test_case = int(sys.stdin.readline())
#     temp += str(test_case // quarter) + " "
#     temp += str((test_case % quarter) // dime) + " "
#     temp += str((test_case % quarter % dime) // nickel) + " "
#     temp += str((test_case % nickel) // penny)
#     case_list.append(temp)
#     temp = ""
#
# print("\n".join(case_list))

# BJ 2903 중앙 이동 알고리즘
# 초기상태 - 정사각형을 이루는 점 4개
# 1. 정사각형의 각 변의 중앙에 점을 하나 추가
# 2. 정사각형의 중심에 점을 하나 추가
# 위 과정을 n번했을때 저장되는 점의 갯수 (중복제외)

# 가로, 세로 늘어나는 정사각형수 2 ** (n-1)
# 가로, 세로 점의 수 = (정사각형수 * 2) + 1
# 저장해야하는 점의 수 = 가로 점의 수 * 세로 점의 수 = 가로 점의 수 ** 2

# N = int(input())
# add_square = 2 ** (N-1)
# save_dot = ((add_square * 2) + 1) ** 2
# print(save_dot)

# BJ 2292 벌집

# N = int(input())
# count = 1
# size = 1
# answer = 1
# # 벌집 크기 (마지막번호) 중앙에서 오른쪽아래
# while N > size:
#     count += 1
#     size = (6 * ((count *(count-1)) // 2)) + 1
#
# print(count)

# BJ 1193 분수찾기

# 1  2  6  7  15 16
# 3  5  8  14 17
# 4  9  13 18
# 10 12 19
# 11 20
# 21
#
#  1 4 1 8 1

# n = 1
# number = 1
# X = int(input())
# answer = 0
# while True:
#     if X <= number:
#         answer = abs(number - X)
#         break
#
#     if n % 2 == 1:
#         number += 1
#     else:
#         if X <= number + n - 1:
#             answer = abs(number - X)
#             break
#         number += 2 * n
#
#     n += 1
#
# print(f"{answer+1}/{n-answer}")

# BJ 2869 달팽이
# import sys
# day = 1
# height = 0
# A, B, V = map(int, sys.stdin.readline().split())
#
# V -= A
# count = abs(V // (A-B))
# day += count
# count_ = abs(V % (A-B))
# if count_ != 0:
#     day += 1
#
# print(day)

# BJ 5086 배수와 약수
# import sys
#
# while True:
#     first, second = map(int, sys.stdin.readline().split())
#     if first == 0 and second == 0:
#         break
#
#     if first % second == 0:
#         print('multiple')
#     elif second % first == 0:
#         print('factor')
#     else:
#         print('neither')

# BJ 2501 약수 구하기
# import sys
# n, k = map(int, sys.stdin.readline().split())
# count = 0
# num = 1
#
# while True:
#     if n % num == 0:
#         count += 1
#         if count == k:
#             print(num)
#             break
#
#     if n == num:
#         print(0)
#         break
#
#     num += 1

# BJ 9506 약수들의 합
# import sys
# while True:
#     n = int(sys.stdin.readline())
#     num = 1
#     total = 0
#     numbers = []
#     if n == -1:
#         break
#     while True:
#         if n % num == 0:
#             total += num
#             numbers.append(num)
#             if total > n:
#                 print(f"{n} is NOT perfect.")
#                 break
#
#         if n - 1 == num:
#             if total != n:
#                 print(f"{n} is NOT perfect.")
#                 break
#             else:
#                 text = " + ".join(map(str, numbers))
#                 print(f"{n} = {text}")
#                 break
#         num += 1

# BJ 1978 소수 찾기
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# N = int(input())
# numbers = list(map(int, input().split()))
# prime_count = sum(1 for number in numbers if is_prime(number))
# print(prime_count)

# BJ 2581 소수
# import sys
# m = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
# numbers = []
#
# for i in range(m, n+1):
#     count = 0
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5)+1):
#         if j != i+1 and i % j == 0:
#             count += 1
#             break
#     if count == 0:
#         numbers.append(i)
#     count = 0
#
# if len(numbers) == 0:
#     print(-1)
# else:
#     print(sum(numbers))
#     print(min(numbers))

# BJ 11653 소인수분해
# import sys
#
#
# def prime_num(n):
#     if n == 1:
#         return
#
#     while n % 2 == 0:
#         print(2)
#         n //= 2
#
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         while n % i == 0:
#             print(i)
#             n //= i
#
#     if n > 2:
#         print(n)
#
#
# number = int(sys.stdin.readline().strip())
# prime_num(number)

# BJ 27323 직사각형
# a = int(input())
# b = int(input())
# print(a * b)

# BJ 1085 직사각형에서 탈출
# x, y, w, h= map(int, input().split())
# numbers = []
# numbers.append(x-0)
# numbers.append(y-0)
# numbers.append(w-x)
# numbers.append(h-y)
# print(min(numbers))

# BJ 3009 네 번째 점
# numbers = []
# for i in range(3):
#     a, b = map(int, input().split())
#     numbers.append(a)
#     numbers.append(b)
#
# answer_x = 0
# answer_y = 0
#
# if numbers[0] == numbers[2]:
#     answer_x = numbers[4]
# elif numbers[0] == numbers[4]:
#     answer_x = numbers[2]
# else:
#     answer_x = numbers[0]
#
# if numbers[1] == numbers[3]:
#     answer_y = numbers[5]
# elif numbers[1] == numbers[5]:
#     answer_y = numbers[3]
# else:
#     answer_y = numbers[1]
#
# print(answer_x, answer_y)

# BJ 15894 정사각형
# n = int(input())
# print(n*4)

# BJ 9063 대지
# import sys
# n = int(input())
# numbers_x = []
# numbers_y = []
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     numbers_x.append(a)
#     numbers_y.append(b)
#
# if min(numbers_x) == max(numbers_x) or min(numbers_y) == max(numbers_y):
#     print(0)
# else:
#     print((max(numbers_x) - min(numbers_x)) * (max(numbers_y) - min(numbers_y)))
