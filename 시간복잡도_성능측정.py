import time
start_time = time.time() #측정 시작

######################### 프로그램 소스코드 #########################
from random import randint

array = []
for _ in range(1000):
    array.append(randint(1, 100)) # 1부터 100 사이의 랜덤한 정수

#선택 정렬 프로그램
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프


####################################################################

end_time = time.time() #측정 종료
print("time:", end_time - start_time) #수행시간 출력