from functools import wraps
from models import get_user_by_id

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            flash("Please login as admin.", "danger")
            return redirect(url_for('login'))
        user = get_user_by_id(user_id)
        if not user or user['role'] != 'admin':
            flash("Access denied.", "danger")
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function
