FROM python:3.14-slim
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app/src DIP_DATA_DIR=/data
EXPOSE 8080
CMD ["python", "-m", "dip", "serve", "--host", "0.0.0.0", "--port", "8080"]
