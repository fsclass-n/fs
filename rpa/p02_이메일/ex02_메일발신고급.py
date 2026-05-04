import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일" # 메일 제목
msg["From"] = EMAIL_ADDRESS # 발신자
msg["To"] = "whyeil29@gmail.com" # 수신자
msg.set_content("이것은 테스트 메일입니다.") # 메일 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # smtp server에 접속 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    smtp.send_message(msg)