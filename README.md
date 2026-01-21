# 🚀 Hướng dẫn cài đặt Odoo - FitDNU

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

---

## 📋 Mục lục

1. [Cài đặt công cụ và môi trường](#1-cài-đặt-công-cụ-và-môi-trường)
2. [Cấu hình cơ sở dữ liệu](#2-cấu-hình-cơ-sở-dữ-liệu)
3. [Thiết lập tham số hệ thống](#3-thiết-lập-tham-số-hệ-thống)
4. [Khởi chạy ứng dụng](#4-khởi-chạy-ứng-dụng)

---

## 1. 🔧 Cài đặt công cụ và môi trường

### 1.1. Clone dự án

```bash
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
cd odoo-fitdnu
git checkout <branch_name>
```

### 1.2. Cài đặt các thư viện hệ thống

Thực thi lệnh sau để cài đặt các dependencies cần thiết:

```bash
sudo apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    python3.10-distutils \
    python3.10-dev \
    python3.10-venv \
    build-essential \
    libffi-dev \
    zlib1g-dev \
    libpq-dev
```

### 1.3. Khởi tạo môi trường ảo Python

Tạo và kích hoạt môi trường ảo:

```bash
# Tạo môi trường ảo
python3.10 -m venv ./venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt các thư viện Python
pip3 install -r requirements.txt
```

> **💡 Lưu ý:** Đảm bảo rằng môi trường ảo đã được kích hoạt trước khi cài đặt requirements.

---

## 2. 🗄️ Cấu hình cơ sở dữ liệu

Khởi tạo PostgreSQL database bằng Docker Compose:

```bash
docker-compose up -d
```

Lệnh này sẽ khởi động PostgreSQL container trong chế độ detached mode.

---

## 3. ⚙️ Thiết lập tham số hệ thống

### 3.1. Tạo file cấu hình `odoo.conf`

Tạo file **odoo.conf** tại thư mục gốc của dự án với nội dung:

```ini
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5432
xmlrpc_port = 8069
```

> **💡 Gợi ý:** Bạn có thể sao chép từ file mẫu:
> ```bash
> cp odoo.conf.template odoo.conf
> ```

### 3.2. Các tham số tùy chọn

Bạn có thể bổ sung thêm các tham số sau khi khởi chạy Odoo:

| Tham số | Mô tả |
|---------|-------|
| `-c <đường_dẫn>` | Chỉ định đường dẫn đến file cấu hình |
| `-u <tên_addons>` | Cập nhật addons trước khi khởi chạy |
| `-d <tên_database>` | Chỉ định database sử dụng |
| `--dev=all` | Bật chế độ developer mode |

**Ví dụ:**

```bash
./odoo-bin -c odoo.conf -d odoo_db -u base --dev=all
```

---

## 4. 🎯 Khởi chạy ứng dụng

### 4.1. Chạy Odoo server

```bash
./odoo-bin -c odoo.conf
```

### 4.2. Truy cập hệ thống

Mở trình duyệt và truy cập:

```
http://localhost:8069
```

### 4.3. Cài đặt các ứng dụng

Sau khi đăng nhập thành công, bạn có thể cài đặt các ứng dụng cần thiết từ Apps menu.

---

## ✅ Hoàn tất

Chúc mừng! Bạn đã cài đặt thành công Odoo - FitDNU. 

**🔗 Các liên kết hữu ích:**
- [Tài liệu Odoo chính thức](https://www.odoo.com/documentation)
- [Repository GitLab](https://gitlab.com/anhlta/odoo-fitdnu)

---

## 📞 Hỗ trợ

Nếu gặp vấn đề trong quá trình cài đặt, vui lòng tạo issue trên GitLab repository.
