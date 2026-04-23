# 1단계: 빌드 (Java)
FROM gradle:8.5-jdk21 AS build
WORKDIR /app
COPY . .
RUN gradle build -x test

# 2단계: 실행
FROM eclipse-temurin:21-jdk-jammy
WORKDIR /app

# 파이썬 설치 (crawler.py 실행 환경 대비)
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# 빌드된 JAR 및 소스 복사
COPY --from=build /app/build/libs/*-SNAPSHOT.jar app.jar
COPY crawler/ ./crawler/
COPY data/ ./data/

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
