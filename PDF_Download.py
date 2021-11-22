# -*- coding: utf-8 -*-
import time
import numpy as np
from selenium.webdriver.common.by import By
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import importlib, sys

importlib.reload(sys)
url = "https://www.google.com.hk/search?q="
driver = webdriver.Chrome()
# driver.maximize_window() #屏幕最大

"""此处search 输入你想在浏览器搜索的资源标题，例如查找“车联网 PDF”可以下载车联网pdf文件内容。"""
search = '车辆网 PDF'
""" """

driver.get(url + search)

print('友好提示：请输入你想搜索的字段内容')
# time.sleep(30)  #这里睡眠30秒时间，可以帮助用户修改搜索框搜索内容进行编辑。

driver.implicitly_wait(10)
final_list = []
for a in range(1):
    elemss = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/a[@href]")
    for i in elemss:
        print('第', a + 1, '页：', i.get_attribute("href"))
        final_list.append(i.get_attribute("href"))
    """  下一页   """
    driver.find_element(By.XPATH, "//*[@id='pnnext']/span[2]").click()
    time.sleep(5)
file = open('new_file_txt.txt', 'w')
file.write(str(final_list))
file.close()
f = open(r'new_file_txt.txt', encoding='UTF-8')
print('打印pdf', f.read())

"""打开新的窗口进行文件下载"""
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_experimental_option('prefs', {
    "download.default_directory": "D:\\edesk\\outtask\\AIopt\\AIOPTjiaofu\\lunwen",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # 这句配置很重要
})
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(5)
for i in range(len(final_list)):
    time.sleep(2)
    driver.get(final_list[i])
    print('资源下载中......', final_list[i])
    time.sleep(0.1)
print('资源下载完毕，您可以去文件保存路径查看详细信息。')
time.sleep(10)
driver.set_window_size(width=1000, height=800, windowHandle="current")
