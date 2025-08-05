## Multi stage build
### Before

docker build	Dùng để build image từ Dockerfile
-t before_msb	Gán tên before_msb cho image
-f mlflow/Dockerfile	Chỉ rõ Dockerfile nằm tại mlflow/Dockerfile
--build-arg MLFLOW_VERSION=2.3.2	Truyền biến môi trường MLFLOW_VERSION vào Dockerfile
mlflow	Là đường dẫn thư mục ngữ cảnh build (context) chứa Dockerfile, file cần copy vào container

```bash
docker build -t before_msb -f mlflow/Dockerfile --build-arg MLFLOW_VERSION=2.3.2 mlflow && docker run -p 5000:5000 before_msb
```

### After

```bash
docker build -t after_msb -f mlflow/Dockerfile-multistage-build --build-arg MLFLOW_VERSION=2.3.2 mlflow && docker run -p 5000:5000 after_msb
```

## Docker Compose
- Up and running MLFlow application with Docker Compose
    
    ```shell
    docker compose -f mlflow-docker-compose.yaml up -d
    ```
- Similarly, you can do it for Trino
    
    ```shell
    docker compose -f trino-docker-compose.yaml up -d
    ```