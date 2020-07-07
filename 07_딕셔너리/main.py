# 딕셔너리 : 이름과 값의 형태로 데이터를 관리한다.
# {}를 사용한다.

dic1 = {
    'a1' : 100,
    'a2' : 11.11,
    'a3' : True,
    'a4' : '문자열'
}

print('dic1 :', dic1)



#값을 가지고 온다.
print('dic1 - a1:', dic1['a1'])
print('dic1 - a1:', dic1.get('a3'))

# 없는 이름 - 오류
# print('dic1 - b1 :', dic1['b1']
# 없는 이름 - 오류가 발생하지 않고 None값이 나온다.
print('dic1 - b2:', dic1.get('b2'))

chk2 = 'b1' in dic1
print('ch3 :', chk2)

print('--------------------')
dic2 = {}
print('dic2 :', dic2)

#값 추가하기
dic2['v1'] = 100
dic2['v2'] = 11.11
dic2['v3'] = '안녕하세요'
print('dic2', dic2)

# 값 수정하기
dic2['v1'] = 1000
print('dic2', dic2)

# 제거
del dic2['v1']
print('dic2',dic2)

# 값을 반환하고 제거한다.
k2 = dic2.pop('v2')
print('k2 :', k2)
print('dic2', dic2)


dic3 = {'a1' : 100 , 'a2' : 200, 'a3' : 300}

# 이름 목록 추출
keys_list = dic3.keys()
print('이름 :', keys_list)

#값 목록 추출
values_list = dic3.values()
print('값 :', values_list)

#이름-값 목록 추출
items_list = dic3.items()
print('이름 :', items_list)


