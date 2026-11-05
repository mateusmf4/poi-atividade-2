FROM eclipse-temurin:17.0.21_9-jdk-noble
WORKDIR /app

COPY build/libs/psoft-commerce-1.0.0.jar app.jar
EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
