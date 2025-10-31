import sqlite3
from flask import Flask, redirect, render_template, request, request,g, send_from_directory, url_for, flash
import userbase, songbase    
app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "users.db"
    

userbase.initialize_db()
songbase.song_db()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def add_user_to_db(username, email, password):
    """Add a new user to the database"""
    try:
        db = get_db()
        db.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )
        db.commit()
        return True
    except sqlite3.IntegrityError:
        return False   
    except Exception as e:
        print(f"Error adding user: {e}")
        return False
    
    
def get_all_songs():
    """Get all songs from the songs database"""
    try:
        conn = sqlite3.connect("songs.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()
        conn.close()
        return songs
    except Exception as e:
        print(f"Error getting songs: {e}")
        return []

@app.route("/home", methods=["POST", "GET"]) 
def home():
    songs = get_all_songs()  # Get songs from database
    return render_template("home.html", songs=songs)

@app.route('/music/<path:filename>')
def serve_music(filename):
    """Serve music files from your music directory"""
    return send_from_directory('music', filename)

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        db = get_db()
        cur = db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cur.fetchone()
        
        if user:
            return redirect(url_for("home"))
        else:
            return "Invalid credentials. Please try again."
    return render_template("auth/login.html")
        

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        if not username or not email or not password:
            flash("Please fill in all fields", "error")
            return render_template("auth/register.html")
        
        if len(username) < 3:
            flash("Username must be at least 3 characters long", "error")
            return render_template("auth/register.html")
        
        if len(password) < 6:
            flash("Password must be at least 6 characters long", "error")
            return render_template("auth/register.html")
        
        if add_user_to_db(username, email, password):
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        else:
            flash("Error: Username or email already exists", "error")
    
    return render_template("auth/register.html")


if __name__ == "__main__":
    app.run(debug=True)     