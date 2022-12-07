# 爬虫调度器,对url管理器,下载器和解析器进行调度操作
from day01_pm.down_html import down_page  # 函数
from day01_pm.html_parse import HtmlParse  # 类
from day01_pm.url_manager import UrlManager # 类

class Scrapy():

    def __init__(self):
        self.hp = HtmlParse()  # url解析器
        self.um = UrlManager() # url管理器

    # 编写一个方法,启动爬虫(此方法完成异常捕获,但是没有控制下载数量)
    # def scrapy_html(self,start_url,encoding="utf-8"):
    #     # 把初始地址交给url管理器
    #     self.um.add_url(start_url)
    #     while self.um.has_url():
    #         url = self.um.get_url()
    #         # 把地址交给下载器
    #         try:
    #             html_str = down_page(url,encoding=encoding)
    #             # 把下载的网页(str) 交给解析器（解析 url img）
    #             url_set,img_set = self.hp.html_parse(url,html_str)
    #             # 把新获取的地址交给url管理器
    #             self.um.add_urls(url_set)
    #             # 把解析的数据保存入库、csv 此处打印到控制台
    #             for img in img_set:
    #                 print(img)
    #         except Exception as err:  # 捕获异常
    #             print('-->', err)

    def scrapy_html(self,start_url,count = 10,encoding="utf-8"):
        # 把初始地址交给url管理器
        self.um.add_url(start_url)
        current = 0   # 统计当前成功下载的次数
        while self.um.has_url():
            url = self.um.get_url()
            # 把地址交给下载器
            try:
                html_str = down_page(url,encoding=encoding)
                # 把下载的网页(str) 交给解析器（解析 url img）
                url_set,img_set = self.hp.html_parse(url,html_str)
                # 把新获取的地址交给url管理器
                self.um.add_urls(url_set)
                # 把解析的数据保存入库、csv 此处打印到控制台
                for img in img_set:
                    print(img)
                current +=1  # 当前次下载成功
                if current == count:
                    break
            except Exception as err:  # 捕获异常
                print('-->', err)
        print(f'待下载地址数:{len(self.um.new_urls)},已下载url地址数:{len(self.um.old_urls)}')

if __name__ == "__main__":
    Scrapy().scrapy_html("http://www.163.com")
