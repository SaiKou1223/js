import requests
import hashlib
import time
import random
import json

class Youdaofanyi(object):
    def __init__(self,word):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1954411926@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=176291494.1898419; JSESSIONID=aaaLK9Cp7Am2W-8hJH7rx; ___rl__test__cookies=1599800313178',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        self.formdata = None
        self.word = word

    def get_formdata(self):
        '''
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,--- "" + (new Date).getTime()
            bv: t,---n.md5(navigator.appVersion)
            salt: i,---r + parseInt(10 * Math.random(), 10);---ts + parseInt(10 * Math.random(), 10);
            sign: n.md5("fanyideskweb" + e + i + "]BjuETDhU)zqSxf-=B#7m")
        }
        '''
        ts= str(time.time()*1000)
        salt = ts + str(random.randint(0,9))
        dddd = "fanyideskweb" + self.word + salt + "]BjuETDhU)zqSxf-=B#7m"
        md5 = hashlib.md5()
        md5.update(dddd.encode())
        sign = md5.hexdigest()
        self.formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': ts,
            'bv': '02edb5d6c6ac4286cd4393133e5aab14',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
    def get_data(self):
        response = requests.post(self.url,headers=self.headers,data=self.formdata)
        return response.text
    def run(self):
        self.get_formdata()
        result = self.get_data()
        text = json.loads(result)["translateResult"][0][0]["src"]
        print(text)
if __name__ == "__main__":
    you = Youdaofanyi("english")
    you.run()