from selenium import webdriver#核心
import requests#核心
import time#用来显示打卡日期
import yagmail#用来发送登录码、打卡信息，不用也可以
import os#用来在脚本里运行另一个脚本
import json#打卡脚本里用的，这里好像没用

print(time.strftime("========= %Y年%m月%d日 =========== refresh",time.gmtime()))

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('no-sandbox')
option.add_argument('disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=option)

driver.get('https://jielong.co/')
print(driver.title)

#设置位置之后的所有元素定位操作都有最大等待时间十秒，在10秒内会定期进行元素定位，超过设置时间之后将会报错
driver.implicitly_wait(10)

#__RequestVerificationToken
RequestVerificationToken = driver.find_element_by_name('__RequestVerificationToken').get_attribute('value')
print('RequestVerificationToken: ',RequestVerificationToken)

#点击
#//*[@id="section1"]/div/div[2]/a
#/html/body/div/div[1]/div/div[2]/a
driver.find_element_by_xpath('//a[@class="code-btn code-login"]').click()
time.sleep(1)

#url https://jielong.co/Portal/GetWXQRCode?key=gnxqlx0fr542tpfg31iudaxu&returnUrl=
#//*[@id="QRContent"]/img
url = driver.find_element_by_xpath('//*[@id="QRContent"]/img').get_attribute('src')
print('url: ',url)
#key
key = url[ url.find( '=' )+1 : url.find( '&' ) ]
print('key: ',key)

#获取登录小程序码
session = requests.session()
#用requests.session()创建session对象，相当于创建了一个空的会话框，准备保持cookies。
headers = {
    'Host': 'jielong.co',
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'sec-ch-ua-platform': "Windows",
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://jielong.co/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__RequestVerificationToken=' + RequestVerificationToken
}

img = session.get(url,headers=headers).content

#保存图片到本地
with open('login.jpg', 'wb') as file:
    file.write(img)
    
#发送图片
yag=yagmail.SMTP(user='...@qq.com',password='...',host='smtp.qq.com',encoding='GBK')
yag.send(to='...@qq.com',subject='快来扫登录码',contents=[yagmail.inline("./login.jpg")])
print('邮件发送成功')   
yag.close()
    
#等待扫码

    #读取token
with open("/token.txt", "r") as f:
    old_token = f.read()
    print('old_token: ', old_token)
token = old_token
for i in range(100):
    print('等待扫码 ',i)
    # print('driver.get_cookies(): ', driver.get_cookies())
    for item in driver.get_cookies():
        if item['name'] == 'token':
            token = item['value']
            print(token)
            break
    if token != old_token: #当token未过期的时候，兑换的token没有变，但是这里的token有Bearer%20，所以不等
        break
    time.sleep(6)

#扫码失败
if token == old_token:
    print('获取token失败！')
    yag=yagmail.SMTP(user='...@qq.com',password='...',host='smtp.qq.com',encoding='GBK')
    yag.send(to='...@qq.com',subject='获取token失败',contents='获取token失败')
    print('获取token失败-邮件发送成功')
    yag.close()
    driver.quit()
    os._exit(0)
    
#获取token
token = token.replace('Bearer%20','')
print('token: ', token)
#设置token
with open("/token.txt","w") as f:
    f.write(token)  # 自带文件关闭功能，不需要再写f.close()
print('重写token成功！')
time.sleep(1)

driver.quit()

#重新运行打卡脚本--打卡脚本里也可以在判断需要登录时，自动运行获取token的脚本
# res = os.popen("python3 /home/jielongguanjia/day.py")    #运行命令 
# print('运行打卡脚本！')
# print(res.read())
# res.close()

#print('----------------------------------------------------------------------')
