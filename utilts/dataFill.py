import time
import asyncio
from DrissionPage import *
from utilts.cloudFlare import cloudflare
from utilts.imageCaptcha import solve_captcha_and_submit
from utilts.fillTextfield import fillTextfield
from utilts.personelInfoPage import personelInfoPage
from utilts.datePage import datePage
from utilts.additionalServices import additionalServices

async def main(smsCode,data):
    while True:
        if len(data.value) > 0:
            userTryCount = 0
            while True:
                try:
                    options = ChromiumOptions()
                    options.headless(False)
                    options.set_browser_path("../chromedriver")
                    p = ChromiumPage(addr_or_opts=options)
                    p.get("https://ita-schengen.idata.com.tr/tr")

                    if p.title != "iDATA -":
                        cloudflare(p)
                    solve_captcha_and_submit(p)
                    time.sleep(2)
                    fillTextfield(p, data.value[0])
                    time.sleep(2)
                    personelInfoPage(p, data.value[0])
                    time.sleep(4)
                    datePage(p, data.value[0])
                    time.sleep(2)
                    additionalServices(p, data.value[0], smsCode)
                    break

                except Exception as e:
                    print(f"Hata oluştu: {e}. Sayfa yenileniyor ve işlemler tekrardan başlatılıyor.")
                    print(smsCode)
                    userTryCount += 1
                    p.get("https://ita-schengen.idata.com.tr/tr")
                    time.sleep(1)
                    print(userTryCount)
                    if userTryCount > 2:
                        print(userTryCount)
                        data_list = data.value
                        if data_list:
                            first_element = data_list.pop(0)
                            data_list.append(first_element)
                        data.value = data_list
                        break




