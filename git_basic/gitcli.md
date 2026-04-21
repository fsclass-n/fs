# Git CLI

## 환경 설정
```
git config [--global] user.name "사용자이름"
git config [--global] user.email "사용자이메일"
```

## 저장소 초기화
현재 디렉터리를 Git 저장소로 초기화
```
git init
```
별칭 이름으로 원격 저장소 추가
```
git remote add [별칭] [저장소 URL]
```
원격 저장소 복제
```
git clone [저장소 URL]
```

## 스테이징과 커밋
작업 디렉터리와 스테이징 영역 상태 확인
```
git status
git status -s
```

작업 파일 스테이지에 올리기
```
git add [파일명]
```

스테이지 작업 내용 내리기
```
git reset [파일명]
git reset --soft [커밋 ID]
git reset --hard [커밋 ID]
```

코드 차이점 확인하기
```
git diff
git diff --staged
```

스테이지에 올라간 내용 커밋하기
```
git commit -m "커밋 메시지"
```

## 업로드 및 업데이트
원격 저장소에 있는 최신 이력을 로컬로 가져오기
```
git fetch [별칭]
```

원격 저장소의 브랜치를 현재 브랜치에 병합
```
git merge [별칭] / [브랜치명]
```

원격 저장소에 브랜치 업로드
```
git push [-u] [별칭] [브랜치명]
```

원격 저장소의 최신 내용을 가져와서(fetch) 내 로컬 코드와 즉시 병합(merge)
```
git pull
```

