# 1단계: 빌드 (Java)
FROM gradle:8.5-jdk21 AS build
WORKDIR /app
COPY . .
RUN gradle build -x test

# 2단계: 실행
FROM eclipse-temurin:21-jdk-jammy
WORKDIR /app

# 파이썬 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 빌드된 JAR 복사
COPY --from=build /app/build/libs/*-SNAPSHOT.jar app.jar

# [핵심] demo 폴더 내의 requirements.txt를 복사하여 설치
COPY demo/requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# 실제 소스 코드 복사 (경로 유지)
COPY demo/crawler/ ./demo/crawler/
COPY demo/data/ ./demo/data/

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
