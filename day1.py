# (100°F − 32) × 5/9 = 37.778°C
# 실험용1
fahrenheit = float(input('화씨 온도:'))
celsius = (fahrenheit - 32.0 ) * 5/9
print(f'화씨 {fahrenheit}온도 도는 섭씨 온도는 {celsius}온도 입니다')

#for countdown in 5,4,3,2,1, "hey":
#    print(countdown)
#print('프로그램 종료')
# 실험2
# 스네이크 표기법이란 단어 사이에 _를 집어 넣는 표기법을 말한다 파이썬에서는 이와 같은 방식을 사용한다.
countdown_list = [5,4,3,2,1, "hey"]
for countdown in countdown_list:
    print(countdown)
print(countdown_list[3])
print('프로그램 종료')

# (100°F − 32) × 5/9 = 37.778°C
# 실험용1
fahrenheit = float(input('화씨 온도:'))
celsius = (fahrenheit - 32.0 ) * 5/9
print(f'화씨 {fahrenheit}온도 도는 섭씨 온도는 {celsius}온도 입니다')

#for countdown in 5,4,3,2,1, "hey":
#    print(countdown)
#print('프로그램 종료')
# 실험2
# 스네이크 표기법이란 단어 사이에 _를 집어 넣는 표기법을 말한다 파이썬에서는 이와 같은 방식을 사용한다.
countdown_list = [5,4,3,2,1, "hey"]
for countdown in countdown_list:
    print(countdown)
print(countdown_list[3])
print('프로그램 종료')

# 실험 4

import tkinter as tk

win = tk.Tk()
win.geometry('400x300')
win.title('파이썬 1일차 priview')
win.mainloop()