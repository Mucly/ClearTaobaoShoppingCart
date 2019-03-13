#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/1/20
# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time


def login(browser):
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成淘宝扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(browser, buy_time):
    while True:
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if cur_time > buy_time:
            # 全选购物车
            while True:
                try:
                    if browser.find_element_by_id("J_SelectAll1"):
                        browser.find_element_by_id("J_SelectAll1").click()
                        print("已全选")
                        break
                except:
                    print("找不到全选按钮")
            # 结算和提交订单
            while True:
                try:  # 疯狂点击<结算>按钮
                    if browser.find_element_by_id("J_Go"):
                        browser.find_element_by_id("J_Go").click()
                        print("已结算")
                except:  # 界面跳转后，点击<提交订单>按钮
                    try:
                        if browser.find_element_by_link_text('提交订单'):
                            browser.find_element_by_link_text('提交订单').click()
                            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print("抢购成功时间：%s" % now1)
                            browser.close()
                            return 0
                    except:
                        print("再次尝试提交订单")

            time.sleep(0.001)  # 1ms循环

if __name__ == "__main__":
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    set_time = input(f"请输入抢购时间，格式如 {cur_time} :\n")
    # 时间格式："2018-09-06 11:20:00.000000"
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()

    login(chrome_browser)
    buy(chrome_browser, set_time)
