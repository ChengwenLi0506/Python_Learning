# 构建url管理器, 需要有两个set 存储待下载url地址,和已下载的url地址
# s = {1,2,'A',3,4,1}  # 去重,因为set没有下标
# print(s,type(s))
# print(s.pop())  # 随机获取一个数据
# print(s)

# 判断某个数在序列(list,set,tuple,dict,str)中是否出现
# print(3 not in [5,6,7])
num = 100

class UrlManager:

    def __init__(self):
        self.new_urls = set()  # 存储待下载url地址
        self.old_urls = set()  # 存储已下载url地址

    # 添加待下载的url地址(一个)
    def add_url(self,url):
        # 判断是否在待下载和已下载中出现
        if (url not in self.new_urls) and (url not in self.old_urls):
            self.new_urls.add(url)

    # 添加待下载的url地址(多个),传入如果是序列,则都可以通过for遍历
    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)

    # 每次随机返回一个url
    def get_url(self):
        url = self.new_urls.pop()
        # 把当前url添加到已下载url集合中
        self.old_urls.add(url)
        return url

    # 判断是否还有待下载的url地址
    def has_url(self):
        return len(self.new_urls) > 0

# 魔法变量
if __name__ == "__main__":
    um = UrlManager()
    um.add_urls(['http://www.163.com', "http://www.162.com", "http://www.baidu.com"])
    url = um.get_url()
    print(url)
    print(um.has_url())
    um.get_url()
    um.get_url()
    print(um.has_url())
    um.add_url("http://www.163.com")
    print(f'待下载:{um.new_urls},已下载:{um.old_urls}')



