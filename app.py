from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

final_df = None  # GLOBAL DATAFRAME


# ---------- DURATION ----------
def days_to_duration(days):
    if days < 0:
        return f"Expired {-days} days ago"

    months = days // 30
    remaining_days = days % 30

    result = []
    if months > 0:
        result.append(f"{months} month{'s' if months > 1 else ''}")
    if remaining_days > 0:
        result.append(f"{remaining_days} day{'s' if remaining_days > 1 else ''}")

    return " ".join(result) if result else "Today"


# ---------- STATUS ----------
def get_status(days):
    if days <= 0:
        return "Expired"
    elif days <= 30:
        return "Near Expiry"
    else:
        return "Safe"


# ---------- HOME ----------
@app.route('/')
def index():
    return render_template('index.html')


# ---------- ABOUT ----------
@app.route('/about')
def about():
    return render_template('about.html')


# ---------- UPLOAD ----------
@app.route('/upload', methods=['POST'])
def upload():
    global final_df

    file = request.files['file']
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)

    df['expiry_date'] = pd.to_datetime(df['expiry_date'])
    df['today_date'] = pd.to_datetime('today')
    df['days_to_expiry'] = (df['expiry_date'] - df['today_date']).dt.days
    df['expiry_duration'] = df['days_to_expiry'].apply(days_to_duration)
    df['expiry_status'] = df['days_to_expiry'].apply(get_status)

    final_df = df

    return render_template(
        'result.html',
        safe_count=len(df[df['expiry_status'] == 'Safe']),
        near_count=len(df[df['expiry_status'] == 'Near Expiry']),
        expired_count=len(df[df['expiry_status'] == 'Expired'])
    )


# ---------- SAFE ----------
@app.route('/safe')
def safe():
    global final_df
    if final_df is None:
        return redirect(url_for('index'))

    df = final_df[final_df['expiry_status'] == 'Safe']
    return render_template('safe.html', table=df.to_html(classes='table', index=False))


# ---------- NEAR EXPIRY ----------
@app.route('/near-expiry')
def near_expiry():
    global final_df
    if final_df is None:
        return redirect(url_for('index'))

    df = final_df[final_df['expiry_status'] == 'Near Expiry']
    return render_template('near.html', table=df.to_html(classes='table', index=False))


# ---------- EXPIRED ----------
@app.route('/expired')
def expired():
    global final_df
    if final_df is None:
        return redirect(url_for('index'))

    df = final_df[final_df['expiry_status'] == 'Expired']
    return render_template('expired.html', table=df.to_html(classes='table', index=False))


if __name__ == '__main__':
    app.run(debug=True)
