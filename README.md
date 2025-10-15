# secure-dashboard
# Secure Dashboard

A modern, offline-first web-based Secure Dashboard built with Flask, SQLite, Passlib, PyOTP, QR Code, User Agents, and a beautiful responsive UI.  
Includes role-based access control, 2FA (Google Authenticator), device monitoring, admin panel, analytics, profile editing, dark mode, and CSV export.

---

## 🚀 Features

- **User Registration/Login** with hashed passwords and device recognition
- **Google Authenticator 2FA** (PyOTP)
- **Role-Based Access (Admin/User)**
- **Admin Panel**: User management, role change, delete, activity export
- **Device/Browser Monitoring** for each login
- **Profile Editing** with picture upload
- **Responsive and Modern UI** (Bootstrap, SweetAlert2, Dark/Light mode)
- **Login Analytics** (Chart.js): logins per day, devices, etc.
- **Export login activity** as CSV (PDF optional)
- **Works 100% Offline:** No CDN or external API required

---

## 🧱 Folder Structure

```
secure-dashboard/
├── app.py
├── requirements.txt
├── instance/
│   └── secure_dashboard.sqlite3
├── static/
│   ├── bootstrap/         # Bootstrap CSS/JS (local)
│   ├── sweetalert2/       # SweetAlert2 CSS/JS (local)
│   ├── chart.js/          # Chart.js (local)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── profile_pics/
│   └── images/
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── twofa.html
│   ├── dashboard.html
│   ├── admin_panel.html
│   ├── profile.html
├── models.py
├── utils.py
├── forms.py
└── README.md
```

---

## ⚡️ Quick Start

1. **Clone the repo**
    ```bash
    git clone https://github.com/faisal20-hckr/secure-dashboard.git
    cd secure-dashboard
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **(Optional) Download frontend dependencies (Bootstrap, SweetAlert2, Chart.js)**
    - Download and extract [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/download/) to `static/bootstrap/`
    - Download [SweetAlert2](https://sweetalert2.github.io/) to `static/sweetalert2/`
    - Download [Chart.js](https://www.chartjs.org/download/) to `static/chart.js/`

4. **Run the app**
    ```bash
    python app.py
    ```
    The app will start at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

5. **Register a user**
    - The first registered user can be made admin (edit directly in DB or via admin panel).
    - Scan the QR code with Google Authenticator during 2FA setup.

6. **Login & Explore**
    - Try user, admin, profile, and analytics features.
    - Use the admin panel to manage users and export login activity.

---

## 💡 Notes

- **Works offline:** All JS/CSS dependencies are local—no CDN.
- **Security:** Change the `app.secret_key` in `app.py` for production.
- **Database:** The SQLite database is auto-created in `instance/secure_dashboard.sqlite3`.
- **Profile Images:** Uploaded profile pictures are stored in `static/profile_pics/`.

---

## 🛠 Requirements

- Python 3.8+
- Flask, passlib, pyotp, qrcode, Pillow, user-agents

---

## 📦 Main Python Dependencies

```
Flask
passlib
pyotp
qrcode
Pillow
user-agents
```

---

## ✨ Credits

- [Bootstrap](https://getbootstrap.com/)
- [SweetAlert2](https://sweetalert2.github.io/)
- [Chart.js](https://www.chartjs.org/)
- [PyOTP](https://pyauth.github.io/pyotp/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)
- [QRCode](https://pypi.org/project/qrcode/)
- [Pillow](https://python-pillow.org/)
- [user-agents](https://pypi.org/project/user-agents/)

---

## 📝 License

[MIT](LICENSE)
