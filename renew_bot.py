import undetected_chromedriver as uc
import time
import os

# إعداد المتصفح
options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=options)

try:
    driver.get("https://example.com/login")  # <-- عدل اللينك حسب موقعك

    # لو عندك login:
    username = os.getenv("BOT_USERNAME")
    password = os.getenv("BOT_PASSWORD")

    # مثال فقط لتسجيل الدخول (عدله حسب الموقع الحقيقي)
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "login").click()

    # انتظار تحميل الصفحة والدخول للداشبورد
    time.sleep(5)

    # تكرار الضغط على زرار renew كل 5 ثواني
    while True:
        renew_button = driver.find_element("id", "renew")  # <-- عدّل حسب الزرار
        renew_button.click()
        print("Renew clicked!")
        time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
