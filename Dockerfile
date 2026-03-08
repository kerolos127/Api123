# Dockerfile for Exos Terminal API V5
# Author: @HackerExos

# استخدم Python خفيف الوزن
FROM python:3.11-slim

# اعمل مجلد العمل (كل الملفات في الجذر)
WORKDIR /app

# انسخ جميع الملفات من المشروع إلى الحاوية
COPY . .

# ثبت المكتبات المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# افتح المنفذ 8000
EXPOSE 8000

# الأمر لتشغيل السيرفر
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]