import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

options = uc.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.binary_location = "/usr/bin/google-chrome"  # المكان الافتراضي للكروم داخل الحاوية

driver = uc.Chrome(options=options)

try:
    driver.get("https://www.mcserverhost.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "auth-username").send_keys("HaZeM579")
    driver.find_element(By.ID, "auth-password").send_keys("12345QWert")

    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'LOGIN')]")
    login_button.click()
    time.sleep(5)

    driver.get("https://www.mcserverhost.com/servers/b35e01fd/dashboard")
    time.sleep(5)

    while True:
        try:
            renew_button = driver.find_element(By.XPATH, "//a[contains(@class, 'billing-button') and contains(text(), 'RENEW')]")
            renew_button.click()
            print("\u2705 تم الضغط على زر RENEW")
        except Exception as e:
            print(f"⚠️ الزر مش ظاهر أو حصل خطأ: {e}")

        print("⏳ انتظار دقيقة...")
        time.sleep(5)

except Exception as e:
    print(f"❌ حصل خطأ في التسجيل: {e}")
finally:
    driver.quit()
