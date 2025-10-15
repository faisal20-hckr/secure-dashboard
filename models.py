import sqlite3
from passlib.hash import pbkdf2_sha256

DB_PATH = "instance/secure_dashboard.sqlite3"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            otp_secret TEXT,
            role TEXT NOT NULL DEFAULT 'user',
            profile_pic TEXT DEFAULT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS login_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            device_info TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def create_user(username, email, password, role='user'):
    password_hash = pbkdf2_sha256.hash(password)
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)',
                  (username, email, password_hash, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_username(username):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id=?', (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def set_otp_secret(user_id, otp_secret):
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE users SET otp_secret=? WHERE id=?', (otp_secret, user_id))
    conn.commit()
    conn.close()

def set_user_role(user_id, role):
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE users SET role=? WHERE id=?', (role, user_id))
    conn.commit()
    conn.close()

def update_user_profile(user_id, username, email, profile_pic=None):
    conn = get_db()
    c = conn.cursor()
    if profile_pic:
        c.execute('UPDATE users SET username=?, email=?, profile_pic=? WHERE id=?',
                  (username, email, profile_pic, user_id))
    else:
        c.execute('UPDATE users SET username=?, email=? WHERE id=?',
                  (username, email, user_id))
    conn.commit()
    conn.close()

def delete_user_by_id(user_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

def log_login_activity(user_id, device_info):
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO login_activity (user_id, device_info) VALUES (?, ?)', (user_id, device_info))
    conn.commit()
    conn.close()

def get_login_activity(user_id, limit=10):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        SELECT login_time, device_info FROM login_activity
        WHERE user_id=?
        ORDER BY login_time DESC LIMIT ?
    ''', (user_id, limit))
    rows = c.fetchall()
    conn.close()
    return rows

def get_all_login_activity(limit=100):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        SELECT login_activity.*, users.username
        FROM login_activity
        JOIN users ON login_activity.user_id = users.id
        ORDER BY login_time DESC LIMIT ?
    ''', (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

def count_total_users():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    count = c.fetchone()[0]
    conn.close()
    return count

def count_todays_logins():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM login_activity WHERE DATE(login_time) = DATE("now", "localtime")')
    count = c.fetchone()[0]
    conn.close()
    return count

def count_active_sessions():
    # Dummy implementation for now (sessions are not tracked in DB)
    return 0
