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

## 로그 보기
```
git log
git log --oneline
```

두 브랜치의 차이점 보기
```
git log branchB..branchA
git diff branchB..branchA
```

한 파일의 히스토리 살펴보기
```
git log --follow [파일명]
```

깃 오브젝트 정보 보기
```
git show [오브젝트 체크섬]
```


## 브랜치와 병합
로컬 브랜치 목록 보기
```
git branch
```

현재 커밋에서 브랜치 만들기
```
git branch [새 브랜치명]
git switch [새 브랜치명]
git checkout [새 브랜치명]
```

브랜치 생성과 동시에 이동
```
git checkout -b [새 브랜치명]
git switch -c [새 브랜치명]
```

브랜치 삭제
```
git branch -d [브랜치명]
```

브랜치 이름 바꾸기
```
git branch -m [브랜치명]
```

현재 브랜치와 지정된 브랜치 병합
```
git merge [브랜치명]
git rebase [브랜치명]
```

## 임시 저장
작업 내용 임시 저장
```
git stash
```

임시 저장 목록 보기
```
git stash list
```

가장 최근 임시 저장 꺼내오기 (꺼낸 저장 내용은 목록에서 사라짐)
```
git stash pop
```

임시 저장 내용을 반영하고 스태시 목록에 남져놓기
```
git stash apple
```

임시 저장 내용 반영 없이 삭제하기
```
git stash drop
```
