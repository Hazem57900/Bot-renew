FROM python:3.10-slim

# تثبيت Google Chrome
RUN apt-get update && apt-get install -y wget gnupg unzip && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable

# إنشاء مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . /app

# تثبيت الباكدجات المطلوبة
RUN pip install --upgrade pip && pip install -r requirements.txt

# تحديد الأمر اللي يشتغل أول ما السيرفر يشتغل
CMD ["python", "renew_bot.py"]
