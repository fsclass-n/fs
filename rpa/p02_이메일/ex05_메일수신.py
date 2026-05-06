# pip install imap_tools
from imap_tools import MailBox
from account import *
from datetime import datetime
from zoneinfo import ZoneInfo # Python 3.9 이상

# 한국 시간대(Asia/Seoul) 설정
now_korea = datetime.now(ZoneInfo("Asia/Seoul"))
print(now_korea.strftime("%Y-%m-%d %H:%M:%S"))

# 보낼때: smtp.gmail.com, 587
# 받을때: imap.gmail.com, 993
mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit=1 -> 최대 메일 갯수, 1개만 수신
# reverse=True -> True 이면 최근 메일부터, False 이면 과거 메일부터 수신
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목:", msg.subject)
    print("발신자:", msg.from_)
    print("수신자:", msg.to)
    # print("참조자:", msg.cc)
    # print("비밀참조자:", msg.bcc)
    print("날짜:", msg.date)
    print("본문내용:", msg.text)
    # print("HTML 메시지:", msg.html)
    print("="*50)

    # 첨부 파일 정보 터미널 출력
    for att in msg.attachments:
        # d:\\wi\\git\\fs\\rpa\\p02_이메일\\python.png
        print("첨부 파일명:", att.filename.split("\\")[-1])
        print("첨부 파일 MIME-Type:", att.content_type)
        print("첨부 파일 크기:", att.size)
        print("="*50)

        # 파일 다운로드
        with open("downloads_" + att.filename.split("\\")[-1], "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))

mailbox.logout()