import requests
import threading

threadLock = threading.Lock()

def urlsGet(url):
    timeout = 3     #超时设置为3s
    try:
        get_response = requests.get(url=url,timeout=timeout)
        print(url+" GET请求测试结果-->"+str(get_response.status_code))
        file = open("url.txt", "a", encoding='UTF-8')
        if get_response.status_code in (200,302,403,404,500,503):
            threadLock.acquire()  # 同步锁,用于异步写入，避免同时写入出现错误
            file.write(url)
            file.write('\n')
            file.close()
            threadLock.release()  # 释放同步锁

    except Exception as e:
        # threadLock.acquire()  # 同步锁,用于异步写入，避免同时写入出现错误
        value3 = url + " -->异常"
        print(value3)
        # file = open("url.txt", "a", encoding='UTF-8')
        # file.write(value3)
        # file.write('\n')
        # file.close()
        # threadLock.release()    # 释放同步锁
        pass

if __name__ == '__main__':
    with open('url.txt', 'r', encoding='utf-8') as fp:
        urls = fp.readlines()
        for url in urls:
            if url.find("http") == 0:
                url = url
            else:
                url = "http://"+url

            url = url.replace("\n", "")
            t = threading.Thread(target=urlsGet, args=(url,))  # 注意传入的参数一定是一个元组!
            t.start()


