# Hướng dẫn Git cho người mới bắt đầu

Tài liệu này dành cho thành viên chưa quen dùng Git. Làm theo đúng thứ tự.

---

## Bước 1 — Cài đặt (chỉ làm 1 lần)

1. Tạo tài khoản GitHub tại https://github.com/signup
   **Dùng đúng email đã đăng ký trong nhóm** để commit được ghi nhận tên bạn.
2. Cài Git: https://git-scm.com/downloads
3. Cài Python 3.10+: https://www.python.org/downloads
   Khi cài nhớ tick vào ô **"Add Python to PATH"**.
4. Cài Visual Studio Code: https://code.visualstudio.com

Sau đó mở Terminal (hoặc PowerShell) và khai báo danh tính:

```bash
git config --global user.name "Nguyen Van A"
git config --global user.email "email-cua-ban@gmail.com"
```

> Thay bằng tên và email của chính bạn.

---

## Bước 2 — Nhận lời mời vào repo

Nhóm trưởng sẽ gửi lời mời cộng tác. Bạn sẽ nhận được email từ GitHub,
hoặc vào thẳng https://github.com/notifications để bấm **Accept invitation**.

Chưa bấm Accept thì bạn không push code lên được.

---

## Bước 3 — Tải code về máy

```bash
git clone https://github.com/tronghv77/tetris-game-uit.git
cd tetris-game-uit
```

---

## Bước 4 — Chạy thử game

```bash
python tetris.py
```

Không cần cài thư viện gì thêm. Hiện ra bảng chơi bằng ký tự, có khối rơi xuống
là thành công. Bấm `a` `d` để dịch trái phải, `x` rơi nhanh, `q` để thoát.

Chạy được rồi thì nhắn vào kênh Slack của nhóm báo một tiếng.

---

## Bước 5 — Quy trình làm việc hằng ngày

**Nguyên tắc vàng: không bao giờ code trực tiếp trên nhánh `main`.**

```bash
# 1. Lấy code mới nhất về (làm mỗi khi bắt đầu ngồi vào code)
git checkout main
git pull origin main

# 2. Tạo nhánh riêng cho việc mình sắp làm
git checkout -b feat/xoa-hang

# 3. Code...

# 4. Xem mình đã sửa những file nào
git status

# 5. Lưu lại thay đổi
git add .
git commit -m "feat: viết hàm remove_line"

# 6. Đẩy lên GitHub
git push -u origin feat/ve-khoi
```

Sau khi push, mở https://github.com/tronghv77/tetris-game-uit sẽ thấy nút
**Compare & pull request** màu vàng. Bấm vào, viết mô tả ngắn, bấm
**Create pull request**, rồi nhắn nhóm nhờ người khác vào duyệt.

---

## Quy ước đặt tên nhánh

| Loại việc | Mẫu tên | Ví dụ |
|-----------|---------|-------|
| Thêm tính năng | `feat/...` | `feat/khoi-roi-xuong` |
| Sửa lỗi | `fix/...` | `fix/khoi-xuyen-tuong` |
| Viết tài liệu | `docs/...` | `docs/cap-nhat-readme` |
| Dọn dẹp code | `refactor/...` | `refactor/tach-ham-ve` |

## Quy ước viết commit message

```
<loại>: <mô tả ngắn, tiếng Việt có dấu, không viết hoa đầu câu>
```

Ví dụ tốt:
- `feat: vẽ khung bảng chơi`
- `fix: sửa lỗi khối xoay xuyên tường`
- `docs: bổ sung hướng dẫn cài đặt`

Ví dụ nên tránh: `update`, `sửa tí`, `abc`, `final_v2_thatsu`.

---

## Xử lý các tình huống hay gặp

**Lỡ code thẳng trên `main` rồi, giờ sao?**
```bash
git checkout -b feat/ten-nhanh-moi   # chuyển hết thay đổi sang nhánh mới
git add .
git commit -m "feat: mô tả việc đã làm"
git push -u origin feat/ten-nhanh-moi
```

**Push bị báo `rejected` / `non-fast-forward`?**
Nghĩa là trên GitHub có code mới hơn máy bạn:
```bash
git pull origin main --rebase
git push
```

**Bị "conflict" khi merge?**

Đừng hoảng. Cả nhóm cùng sửa `tetris.py` nên chuyện này chắc chắn xảy ra, và môn
học còn *yêu cầu* nhóm phải gặp và xử lý được ít nhất 3 lần. Gặp conflict nghĩa là
nhóm đang làm đúng cách, không phải ai đó làm sai.

Conflict xảy ra khi hai người cùng sửa một chỗ trong cùng một file. Git không tự
quyết được giữ bản nào nên nhờ mình chọn.

```bash
git checkout main
git pull origin main
git checkout ten-nhanh-cua-minh
git merge main
```

VS Code sẽ tô màu đoạn bị đụng, có nút *Accept Current* (giữ bản của mình),
*Accept Incoming* (lấy bản trên main) và *Accept Both*. Thường thì cần giữ **cả
hai phần** rồi sửa lại cho khớp nhau, chứ ít khi vứt hẳn một bên.

Chọn xong nhớ xoá các dòng đánh dấu `<<<<<<<`, `=======`, `>>>>>>>`, chạy thử
game xem còn chạy không, rồi:

```bash
git add .
git commit -m "fix: xử lý conflict trong tetris.py"
git push
```

Không tự tin thì chụp màn hình gửi lên Slack, đừng đoán bừa. Và nhớ báo trong
kênh mỗi lần gặp conflict — nhóm cần ghi nhận đủ số lần để nộp cho thầy.

**Muốn bỏ hết thay đổi chưa commit, quay lại như cũ?**
```bash
git restore .
```
> Cẩn thận: lệnh này xoá vĩnh viễn các sửa đổi chưa commit.
