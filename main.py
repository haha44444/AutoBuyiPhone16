# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 型号和颜色包含在url中，在官网选择后即可复制链接到此处

# iPhone 16 Pro Max 原色钛金属 256G
url = "https://www.apple.com.cn/shop/buy-iphone/iphone-16-pro/MYTQ3CH/A"

# # iPhone 15 蓝色 128G
# url = "https://www.apple.com.cn/shop/buy-iphone/iphone-15/MTLG3CH/A"

# 苹果账号邮箱
appleid_username = 'xxx@xxx.com'
# 苹果账号密码
appleid_password = 'password'

# 设置浏览器options
options = webdriver.ChromeOptions()
# 加初始化设置（运行完成不会自动关闭浏览器）
options.add_experimental_option('detach', True)

# 创建浏览器对象
driver = webdriver.Chrome(options=options)


def one():
    # 没有旧机抵扣
    while True:
        try:
            element_old = driver.find_element(By.ID, 'noTradeIn_label')
            break
        except NoSuchElementException:
            driver.refresh()

    driver.execute_script("arguments[0].click();", element_old)

    # 无Applecare

    # iPhone16
    element_care = driver.find_element(By.ID, 'applecareplus_59_noapplecare')

    # # iPhone15
    # element_care = driver.find_element(By.ID, 'applecareplus_58_noapplecare')

    driver.execute_script("arguments[0].click();", element_care)

    # 添加到购物袋
    time.sleep(1)
    element_car = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[2]/div[4]/div[2]/div[3]/div[4]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/span/form/div/span/button')
    # element_car = driver.find_element_by_name('add-to-cart')
    # element_car = driver.find_element_by_css_selector('.add-to-cart')
    if element_car is not True:
        element_car = driver.find_element(By.XPATH,
                                          '//*[@id="root"]/div[2]/div[3]/div[4]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/span/form/div/span/button')

    driver.execute_script("arguments[0].click();", element_car)


# 跳转到购买界面
driver.get(url)
# 隐式等待
driver.implicitly_wait(20)

one()
if driver.current_url == url:
    one()

# 页面跳转查看购物袋
driver.implicitly_wait(10)
element_check = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/form/button')
driver.execute_script("arguments[0].click();", element_check)

# 结账
driver.implicitly_wait(10)
element_check_out = driver.find_element(By.XPATH, '//*[@id="shoppingCart.actions.navCheckout"]')
driver.execute_script("arguments[0].click();", element_check_out)

# 结账界面跳转时间较长  隐式等待多等一会
driver.implicitly_wait(30)

# 勾选隐私条款
element_signin_consent_1 = driver.find_element(By.XPATH,
                                               '//*[@id="signIn.consentOverlay.dataHandleByApple_label"]/span')
driver.execute_script("arguments[0].click();", element_signin_consent_1)
element_signin_consent_2 = driver.find_element(By.XPATH,
                                               '//*[@id="signIn.consentOverlay.dataOutSideMyCountry_label"]/span')
driver.execute_script("arguments[0].click();", element_signin_consent_2)

# 同意隐私条款
element_signin_consent = driver.find_element(By.XPATH, '//*[@id="consent-overlay-accept-button"]')
driver.execute_script("arguments[0].click();", element_signin_consent)

# 输入用户名
element_username = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[2]/div[1]/div/div[1]/div/form/div[1]/div[1]/input')
# time.sleep(3)
element_username.send_keys(appleid_username)

# 输入密码
element_password = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[2]/div[1]/div/div[1]/div/form/div[1]/div[2]/input')
# time.sleep(3)
element_password.send_keys(appleid_password)

# 登录
element_login = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[1]/div/form/div[2]/button')
driver.execute_script("arguments[0].click();", element_login)

# 如何收到订单商品
# （点击）继续填写送货地址
element_next_address = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/button')
driver.execute_script("arguments[0].click();", element_next_address)

# 等待跳转结账
driver.implicitly_wait(10)

# 选择发票（个人抬头）
element_fapiao = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/fieldset/div/div/div[2]/div/div/div/div/label')
driver.execute_script("arguments[0].click();", element_fapiao)

# （点击）继续选择付款方式
element_check_out_next = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[5]/div/div/div/button')
driver.execute_script("arguments[0].click();", element_check_out_next)

# 分期付款（工商银行）
driver.implicitly_wait(20)
element_fenqi = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/fieldset/div/div/div[2]/div[5]/div[1]/div[1]/div/div/label')
driver.execute_script("arguments[0].click();", element_fenqi)

# 24期
time.sleep(2)
element_fenqi_24 = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/fieldset/div/div/div[2]/div[5]/div[2]/div/div/div/div/div[1]/div/ul/li[4]/label')
driver.execute_script("arguments[0].click();", element_fenqi_24)

# 检查订单（最终）
element_check_out_next_next = driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/button')
driver.execute_script("arguments[0].click();", element_check_out_next_next)
driver.implicitly_wait(20)
time.sleep(15)

# 立即下单
element_xiadan = driver.find_element(By.ID, 'rs-checkout-continue-button-bottom')
driver.execute_script("arguments[0].click();", element_xiadan)
