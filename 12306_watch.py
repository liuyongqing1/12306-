#-*- coding:utf8 -*-

from pyquery import PyQuery as pq
import requests,time


class fuck12306(object):
    def __init__(self):
        self.url='http://www.12306.cn/mormhweb/1/4/index_fl.html'
        self.r=requests.session()
        self.r.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                        'Referer':'http://www.12306.cn/mormhweb/1/4/index_fl.html'}
        self.one=[]
        self.count=0

    def req_html(self):
        html=self.r.get(self.url)
        html.encoding='utf-8'
        return html.text

    def res_html_one(self):
        html=self.req_html()
        doc=pq(html)
        ulli=doc.find('#newList ul li')
        for i in ulli.items():
            item=i.text()
            self.one.append(item)
        return self.one

    def xh(self):
        html=self.req_html()
        doc=pq(html)
        ulli=doc.find('#newList ul li')
        for i in ulli.items():
            item=i.text()
            if item not in self.one:
                self.count += 1
                if self.count == 5:
                    self.one.append(item)
                    self.count=0
        return self.one

if __name__ == '__main__':
    fuck=fuck12306()
    print(fuck.res_html_one())
    while True:
        time.sleep(30)
        b=fuck.xh()
        print(b)