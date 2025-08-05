#slim là bản python mà ít thư viện đi kèm, nhẹ hơn tránh thừa thãi
#FILE DOCKER NẾU GIỮ NGUYÊN VÀ BUILD LẠI IMAGE THÌ NÓ SẼ DÙNG CACHE ĐỂ BUILD LẠI, HOẶC NẾU SỬA 1 PHẦN VÀ BUILD LẠI THÌ NÓ SẼ DÙNG CACHE BUILD ĐẾN PHẦN SỬA
FROM python:3.9-slim 

#metadata
#đơn thuần thông tin về người tạo, tổ chức, phiên bản của image
LABEL maintainer="quandv"
LABEL organization="mlopsvn"

#đường dẫn mặc định trong container
#các lệnh sau này sẽ được thực thi trong thư mục này
WORKDIR /mlflow/

#cho phép truyền biến này từ bên ngoài vào 
ARG MLFLOW_VERSION

# run các lệnh cài đặt
RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install --no-cache-dir mlflow==${MLFLOW_VERSION} psycopg2-binary

# chỉ mang tính document không có tác dụng gì khác
EXPOSE 5000

# Ref: https://github.com/mlflow/mlflow/issues/6274#issuecomment-1196106372
# BACKEND_STORE_URI sẽ cập nhật giá trị này khi chạy container docker run
#NOTE 
CMD mlflow server \
    --backend-store-uri ${BACKEND_STORE_URI} \ 
    --serve-artifacts \
    --host 0.0.0.0 \
    --port 5000

#docker build -t before_msb -f mlflow/Dockerfile --build-arg MLFLOW_VERSION=2.3.2 mlfow
#docker run before_msb
#docer exec -ti before_msb bash