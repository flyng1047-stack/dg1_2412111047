# DG1 – Nguyễn Anh Quân – 2412111047

## Student Management Web Application

Ứng dụng quản lý sinh viên được xây dựng bằng Flask và Python.

### Features
- Hiển thị danh sách sinh viên.
- Tra cứu sinh viên theo ID.
- Lọc danh sách theo lớp.
- Thêm sinh viên qua REST API.
- Kiểm tra sức khỏe ứng dụng qua `/api/health`.

### Docker Deployment
- Dockerfile để đóng gói ứng dụng.
- Docker Compose để chạy ứng dụng và Nginx.
- Nginx reverse proxy chuyển tiếp yêu cầu đến Flask.
- Dữ liệu sinh viên được lưu bằng volume.