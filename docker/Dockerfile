# Base image Ubuntu với Python 3.9
FROM python:3.9-slim

# Cài đặt các thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    build-essential \
    libopencv-dev \
    python3-dev \
    git \
    && apt-get clean

# Tạo thư mục làm việc
WORKDIR /jetson-inference

# Copy file requirements.txt
COPY requirements.txt /jetson-inference/

# Cài đặt các thư viện Python
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --no-warn-script-location -r requirements.txt


# Clone và cài đặt jetson-inference (nếu cần)
# RUN git clone https://github.com/dusty-nv/jetson-inference.git && \
#     cd jetson-inference && mkdir build && cd build && \
#     cmake ../ && make && make install

# Copy mã nguồn vào container
COPY . /jetson-inference/

# Expose cổng Flask
EXPOSE 5000

# Lệnh chạy ứng dụng Flask
CMD ["python", "app.py"]
