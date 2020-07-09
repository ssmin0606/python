# 바이너리 데이터를 읽고 쓰기 위한 모듈
import pickle

class TestClass :

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

def save_pickle() :
    data1 = 100
    data2 = 11.11
    data3 = True
    data4 = '안녕하세요'
    data5 = 10, 20, 30, 40, 50
    data6 = [10, 20, 30, 40, 50]
    data7 = {'k1' : 100, 'k2' : 200}
    data8 = {10, 20, 30, 40, 50}
    data9 = TestClass(100, 200)


    with open('test3.txt','wb') as f5 :

        pickle.dump(data1.f5)
        pickle.dump(data2.f5)
        pickle.dump(data3.f5)
        pickle.dump(data4.f5)
        pickle.dump(data5.f5)
        pickle.dump(data6.f5)
        pickle.dump(data7.f5)
        pickle.dump(data8.f5)
        pickle.dump(data9.f5)


# 문자열 데이터쓰기
def save_text() :

    # #파일을 쓰기 위해 열어준다.
    # #파일이 없으면 생성된다.
    # f1 = open('test1.txt', 'wt', encoding='UTF-8')
    # #파일에 쓴다.
    # f1.write('문자열1')
    # f1.write('문자열2')
    # f1.write('문자열3')
    # #파일을 닫아준다.
    # f1.close()

    with open('test2.txt', 'wt', encoding='UTF-8') as f2 :
        # f2.write('문자열1\n')
        # f2.write('문자열2\n')
        # f2.write('문자열3\n')
        str_list = ['문자열1\n', '문자열2\n', '문자열3\n']
        f2.writelines(str_list)

    print('저장완료')

def append_text() :
    with open('test2.txt', 'at', encoding='UTF-8') as f3 :
        # f3.write('문자열4\n')
        # f3.write('문자열5\n')
        # f3.write('문자열6\n')
        str_list = ['문자열7\n', '문자열8\n', '문자열9\n']
        f3.writelines(str_list)


    print('추가 완료')

def read_text() :
    with open('test2.txt', 'rt', encoding='UTF-8') as f4 :
        # str1 = f4.readline()
        # str2 = f4.readline()
        # str3 = f4.readline()


        # print(str1)

        print('---------------------------------------')
        #한 꺼번에 다 읽어오고 LIST로 반환해준다.
        str_lines = f4.readlines()
        print(str_lines)




if __name__ == '__main__' :
    # save_text()
    # append_text()
    # read_text()
    save_pickle()