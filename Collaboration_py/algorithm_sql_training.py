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
import sys
grade_dc = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
grade_subject_sum = 0
grade_sum = 0

for i in range(20):
    grade_list = sys.stdin.readline().strip().split()
    if grade_list[-1] == "P":
        continue
    grade_sum += float(grade_list[-2]) # 학점의 총합
    grade_subject_sum += (float(grade_list[-2]) * grade_dc[grade_list[-1]]) # 학점 * 과목평점의 합

grade_avg = grade_subject_sum / grade_sum
print(grade_avg)
