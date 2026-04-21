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