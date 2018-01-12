from splinter import Browser
b = Browser('chrome')
url = 'https://kyfw.12306.cn/otn/leftTicket/init'  
b.visit(url)  #访问网址  
first_found = b.find_by_id('login_user').click()  
b.fill('loginUserDTO.user_name', '12306账号')  
b.fill('userDTO.password', '12306密码')   
input()  
sec_found = b.find_by_id('selectYuding').click()  
b.cookies.add({'_jc_save_fromStation': '%u4E0A%u6D77%2CSHH'})  
b.cookies.add({'_jc_save_toStation': '%u6D1B%u9633%2CLYF'})  
b.cookies.add({'_jc_save_fromDate': '2017-02-17'})  
b.cookies.add({'_jc_save_toDate': '2017-02-19'})  
b.reload()  
third_found = b.find_by_text(u'查询').click()  
b.find_by_text(u'预订')[4].click()  