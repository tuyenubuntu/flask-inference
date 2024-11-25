# flask-inference
# flask-inference

stream/
├── flaskapp/                      # Thư mục chứa mã nguồn chính của ứng dụng
│   ├── app.py           # Khởi tạo ứng dụng Flask, đăng ký các module/extension
│   ├── stream.py             # Định nghĩa các route (URL endpoint)
│   ├── models.py             # Định nghĩa các model cơ sở dữ liệu
│   ├── forms.py              # Các biểu mẫu (form) nếu sử dụng Flask-WTF
│   ├── static/               # Chứa các tệp tĩnh (CSS, JavaScript, hình ảnh, fonts)
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── app.js
│   │   └── images/
│   │       └── logo.png
│   ├── templates/            # Chứa các tệp HTML template
│   │   ├── stream.html         # Template cơ bản để các trang khác mở rộng
│   │   ├── index.html        # Trang chủ
│   │   └── info.html        # Trang lỗi 404, 500
│   └── utils.py              # Các hàm tiện ích hoặc logic tái sử dụng
├── docker/                      # Thư mục chứa mã nguồn chính của ứng dụng
│   ├── Dockerfile           # Khởi tạo docker
│   ├── requirements.txt            # requirements
│   ├── 


├── config.py                 # Tệp cấu hình ứng dụng
├── instance/                 # Thư mục chứa cấu hình môi trường cục bộ (nếu cần)
│   └── config.py             # Tệp cấu hình riêng tư (có thể bị ignore)
├── migrations/               # Thư mục chứa các tệp di trú cơ sở dữ liệu (tự tạo bởi Flask-Migrate)
├── tests/                    # Thư mục chứa các tệp kiểm thử
│   ├── __init__.py
│   ├── test_routes.py        # Kiểm thử các route
│   └── test_models.py        # Kiểm thử các model
├── run.py                    # Điểm khởi chạy ứng dụng Flask
├── requirements.txt          # Danh sách các thư viện cần thiết
├── .env                      # Tệp chứa các biến môi trường (bí mật, ví dụ SECRET_KEY)
└── venv/                     # Virtual environment (thư mục môi trường ảo - tùy chọn)



