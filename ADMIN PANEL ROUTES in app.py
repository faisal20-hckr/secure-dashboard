from flask import send_file

@app.route('/admin')
@admin_required
def admin_panel():
    users = get_all_users()
    activity = get_all_login_activity(limit=100)
    total_users = count_total_users()
    todays_logins = count_todays_logins()
    active_sessions = count_active_sessions()
    return render_template(
        'admin_panel.html',
        users=users, activity=activity,
        total_users=total_users,
        todays_logins=todays_logins,
        active_sessions=active_sessions
    )

@app.route('/admin/set-role/<int:user_id>', methods=['POST'])
@admin_required
def admin_set_role(user_id):
    role = request.form.get('role')
    set_user_role(user_id, role)
    flash("Role updated.", "success")
    return redirect(url_for('admin_panel'))

@app.route('/admin/delete-user/<int:user_id>', methods=['POST'])
@admin_required
def admin_delete_user(user_id):
    delete_user_by_id(user_id)
    flash("User deleted.", "success")
    return redirect(url_for('admin_panel'))

@app.route('/admin/export-csv')
@admin_required
def admin_export_csv():
    import csv
    from io import StringIO
    activity = get_all_login_activity(limit=1000)
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Username', 'Login Time', 'Device Info'])
    for row in activity:
        cw.writerow([row['username'], row['login_time'], row['device_info']])
    output = si.getvalue()
    return send_file(
        BytesIO(output.encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='login_activity.csv'
    )
