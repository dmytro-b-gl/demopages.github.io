FROM python:3.12-slim
WORKDIR /app
COPY src/ src/
RUN pip install fastapi uvicorn
EXPOSE 8080
CMD ["python", "-m", "src.service.app"]
