# 创建一个解析器,用来解析有价值的数据 (image)
from lxml import etree
from lxml.etree import _Element
from urllib.parse import urljoin
class HtmlParse():

    # 解析 image url
    def __init__(self):
        # 用来存储解析url地址
        self.url_set = set()
        self.img_set = set()

    def __img_parse(self,base:str,html:_Element):
        img_list = html.xpath("//img/@src")
        for img_src in img_list:
            img_src = urljoin(base,img_src)
            self.img_set.add(img_src)

    def __url_parse(self,base:str,html:_Element):
        url_list = html.xpath("//a/@href")
        for href in url_list:
            href = urljoin(base, href)
            self.url_set.add(href)

    def html_parse(self,base:str,html:str):
        html = etree.HTML(html)
        self.__img_parse(base,html)
        self.__url_parse(base,html)
        return self.url_set,self.img_set

if __name__ == "__main__":
    wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="http://www.abc.com/link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html" id='kw'>fifth item</a>
                 <img src="a.png">我是相对路径图片</a>
                 <img src="http://www.163.com/img/b.png">我是相对路径图片</a>
             </ul>
             <a href="http://www.163.com/">网易</a>
        </div>
    """
    hp = HtmlParse()
    hp.html_parse("http://www.163.com",wb_data)
    for url in hp.url_set:
        print(url)

    for img in hp.img_set:
        print(img)