#coding=utf-8
#导入webdriver驱动程序
from selenium import webdriver
#定义需要打开的浏览器
br=webdriver.Chrome()
#定义打开的目标地址
br.get("https://www.baidu.com")
#1.name定位
# br.find_element_by_name("wd").send_keys("顶真")
#2.class定位
# br.find_element_by_class_name("s_ipt").send_keys("美国大选")
#3.id定位
# br.find_element_by_id("kw").send_keys("拜登")
#4.tag定位
# br.find_element_by_tag_name("input").send_keys("123")
#5.通过link定位
# br.find_element_by_link_text("hao123").click()
#6.partial_link定位
# br.find_element_by_partial_link_text("闻").click()
#7.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("aaa")
#8.css定位
br.find_element_by_css_selector("#kw").send_keys("思密达")

