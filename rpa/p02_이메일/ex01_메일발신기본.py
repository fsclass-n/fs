import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # smtp server에 접속 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "테스트 메일" # 메일 제목
    body = "이것은 테스트 메일입니다." # 메일 본문

    msg = f"Subject: {subject}\n{body}" # 메일 합치기

    # smtp.sendmail(발신자, 수신자, 메시지)
    smtp.sendmail(EMAIL_ADDRESS, "whyeil29@gmail.com", msg)