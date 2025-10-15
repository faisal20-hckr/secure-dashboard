import uuid
from PIL import Image

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = get_user_by_id(user_id)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        file = request.files.get('profile_pic')
        filename = None
        if file and file.filename:
            ext = file.filename.rsplit('.', 1)[-1].lower()
            filename = f"{uuid.uuid4().hex}.{ext}"
            save_path = os.path.join('static/profile_pics', filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            img = Image.open(file)
            img = img.convert("RGB")
            img.thumbnail((150, 150))
            img.save(save_path)
        update_user_profile(user_id, username, email, filename)
        flash("Profile updated.", "success")
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user)
