# 실험 3

subjects = {
    "의사소통영어": "A0",
    "데이터베이스": "A+",
    "회귀분석": "B+",
    }
student = '박화랑'
subject = '데이터베이스'
print(student, '학생의', subject, '성적은', subjects[subject])

# f 스트링 기법
print(f'{student}학생의 {subject}과목 성적은 {subjects[subject]}입니다')
# modern style
#print("{0}학생의 {1}과목 성적은 {2}입니다.". format(student, subject, subjects[subject]))

# old style
print("%s학생의 %s과목 성적은 %s입니다" % (student, subject, subjects[subject]))