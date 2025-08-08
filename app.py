from flask import Flask, render_template,request
from db import get_connection, init_db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/technology', methods=['GET'])
def technology():
    return render_template('technology.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        print(f"New user submitted: Name = {name}, Email = {email}")

        # ✅ Save to DB
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return render_template('thankyou.html', name=name)

    # For GET request, just show the form
    return render_template('contact.html')

@app.route('/all_users')
def all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    return render_template('all_users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
