# -*- codeing: utf-8 -*-

import sys, os, unittest
from time import sleep
from appium import webdriver

'''
测试机型: 红米1s android 4.4.2 
'''






desire_caps = {}
desire_caps['platformName'] = 'iOS'
desire_caps['platformVersion'] =  '4.4.2'
desire_caps['appPackage'] ='com.android.contacts'
desire_caps['appActivity'] = '.activities.PeopleActivity'
# 手机名称,这个可以通过命令行adb devices即可获取,我发现在连接多台手机时会有影响
desire_caps['deviceName'] = '9de1f8c7'
# 以下两项主要是在点击输入框的时候,会触发系统输入法,导致可能我们发送的是字符 `234`,但是九宫格中文输入法有可能给出的是 `bei` ,这两个属性就是屏蔽系统输入法,使用appium自己的,但是测试完成后,得自己去系统设置中将输入法切换过来
desire_caps['unicodeKeyboard'] = True
desire_caps['resetKeyboard'] =  True

# ip地址在pc上的 appium客户端-设置 中可以看到 `server address` 和 `port`,保持一致即可
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)

# 通过id查找控件
# 具体的控件id可以通过 `AndroidSDK\tools\uiautomatorviewer.bat` 来直接获取
createContactBtn = driver.find_element_by_id('com.android.contacts:id/fab')
# 模拟点击操作
createContactBtn.click()
# 也可以通过文本查找控件,并输入姓名
name = driver.find_element_by_name(u"姓名") # "姓名" 是输入框的hint值
name.click()
name.send_keys("阿冏Lynxz") # 输入指定的文本,注意这里需要上面desire_caps屏蔽系统输入法才行
# 也可以查找多个控件
# 比如通讯录可能有多个电话号码输入框 `elements` 多了个s
phone = driver.find_elements_by_name(u"电话")
phone[0].click()
phone[0].send_keys("189***0620")
# 判断结果是否符合预期,不通过的话会在这里中断并打印日志
# self.assertEqual(phone[0].text,"15390")
# 截屏,会在当前目录保存指定文件名的图片
driver.save_screenshot("after_input.png")
# 等待,单位:秒
sleep(5)
# 测试完成,退出
driver.quit()









