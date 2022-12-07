# 根据url下载相应的网页
# 打包的两种方式
# import 包名.包名.模块 as 别名
# from 包名.包名.模块 import 元素 (变量,函数,类)

from urllib3.poolmanager import PoolManager
from urllib3.response import HTTPResponse
from urllib.parse import urljoin

def down_page(url,method="get",encoding="utf-8"):
    pm = PoolManager()  # 打开浏览器
    # 发送了服务器请求
    res: HTTPResponse = pm.request(method=method, url=url)
    # 200  404  500
    if res.status == 200:
        return res.data.decode(encoding=encoding)
    else:
        return None

if __name__ == "__main__":
    res = down_page("http://www.163.com")
    print(res)
    print(urljoin("http://www.baidu.com","http://www.baidu.com/img/abc.png"))
    print(urljoin("http://www.baidu.com","/img/abc.png"))
    print(urljoin("http://www.baidu.com","http://www.163.com/img/abc.png"))
