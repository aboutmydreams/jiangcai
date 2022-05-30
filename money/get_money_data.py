import requests
from bs4 import BeautifulSoup

first_url = "https://fee.icbc.com.cn/index.jsp"
second_url = "https://fee.icbc.com.cn/servlet/ICBCINBSReqServlet"

bd_session = requests.Session()

response = bd_session.get(first_url)
cookii = requests.utils.dict_from_cookiejar(response.cookies)

cookie = "".join(f"{i}=" + value + ";" for i, value in dict(cookii).items())
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '166',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookie,
    'Host': 'fee.icbc.com.cn',
    'Origin': 'https://fee.icbc.com.cn',
    'Referer': 'https://fee.icbc.com.cn/servlet/ICBCINBSReqServlet',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3833.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


datas = {
    'dse_sessionId': 'FTIMDLGAAOCICCEACIJPEXDECPAZIUIJCYJLJGEL',
    'randomIdAppendToFormForMacSafari': '1562649689360-83023251',
    'dse_applicationId': '-1',
    'dse_operationName': 'per_SelfHelpPaymentOp',
    'dse_pageId': '3',
    'pageMark': '3',
    'paymentContent': 'busiCode=2201804177',
    'maskFlag': '0',
    'IN_PAYITEMCODE': 'PJ120012021000015901',
    'paymentR': '0',
}

res = requests.post(second_url,headers=headers,data=datas)
soup = BeautifulSoup(res.text,"lxml")
name = soup.select("#item20")
money = soup.select("#item24")
user_id = soup.select("#busiCode")

print(res.text)
