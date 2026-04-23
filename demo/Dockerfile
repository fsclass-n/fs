# 1단계: 빌드
FROM eclipse-temurin:21-jdk-jammy AS build
WORKDIR /app
COPY . .

# [수정] 실행 권한 부여 명령어 추가
RUN chmod +x gradlew

# [수정] -x test를 추가하여 테스트 실행을 건너跳니다.
# 또한 build 대신 bootJar를 사용하여 꼭 필요한 실행 파일만 만듭니다.
RUN ./gradlew clean bootJar -x test

# 2단계: 실행
FROM eclipse-temurin:21-jdk-jammy
WORKDIR /app

# 파이썬 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 빌드된 JAR 복사 (1단계 build 섹션의 WORKDIR이 /app 인지 확인)
COPY --from=build /app/build/libs/*-SNAPSHOT.jar app.jar

# [수정] 현재 Dockerfile이 demo 폴더 안에 있으므로 상대 경로로 지정
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# [수정] crawler와 data 폴더 복사
# (Dockerfile과 같은 층에 있으므로 바로 복사합니다)
COPY crawler/ ./crawler/
COPY data/ ./data/

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]