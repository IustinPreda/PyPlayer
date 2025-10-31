# PyPlayer
A modern, full-stack music streaming web application built with Flask and Tailwind CSS. Features user authentication, a file-explorer style music library, and a sleek audio player.

https://img.shields.io/badge/Python-3.7+-blue.svg
https://img.shields.io/badge/Flask-2.0+-green.svg
https://img.shields.io/badge/SQLite-Database-lightgrey.svg

✨ Features
🎵 Music Streaming - Play MP3 files directly in the browser

🔐 User Authentication - login and registration system

🎛️ Global Audio Player - Full controls: play, pause, next, previous, volume

💾 SQLite Database - Lightweight and efficient data storage


# Adding Music
Place your MP3 files in the music/ directory

Add song metadata to the database (see Database Setup below)

Playing Music
Click any song row to play immediately

Use the play button next to each song

Control playback from the bottom player bar

Keyboard shortcuts: Spacebar for play/pause

🏗️ Project Structure
text
pyclone-music/
├── main.py                 # Flask application
├── userbase.py            # User database setup
├── songbase.py            # Songs database setup
├── users.db               # User database (auto-generated)
├── songs.db               # Songs database (auto-generated)
├── music/                 # Your MP3 files go here
│   └── your_songs.mp3
├── templates/
│   ├── auth/
│   │   ├── login.html     # Login page
│   │   └── register.html  # Registration page
│   └── home.html          # Main music library
└── README.md

# 🎨 Tech Stack
Backend: Flask, SQLite3

Frontend: HTML5, Tailwind CSS, DaisyUI

Icons: Font Awesome

Audio: HTML5 Audio API

Styling: Modern CSS with glass morphism effects

# 🔒 API Routes
Method	Route	Description
GET	/	Redirects to login
GET/POST	/login	User login
GET/POST	/register	User registration
GET	/home	Main music library
GET	/music/<filename>	Serve music files
# 🎵 Audio Features
Global Player: Fixed bottom bar with full controls

Playlist Navigation: Next/previous song buttons

Progress Control: Seek bar with time display

Volume Control: Mute and volume slider

Auto-play: Automatically plays next song

Keyboard Controls: Spacebar for play/pause


<img width="1917" height="906" alt="Screenshot 2025-10-31 042908" src="https://github.com/user-attachments/assets/8afeaf20-0fec-4b90-8703-31e886610c6b" />


<img width="1918" height="907" alt="Screenshot 2025-10-31 042826" src="https://github.com/user-attachments/assets/ec23ef86-e7c8-4f97-8b95-f9e7cc4bc105" />


<img width="1909" height="905" alt="Screenshot 2025-10-31 043001" src="https://github.com/user-attachments/assets/746d2ee7-cc2f-4c87-a768-dac4df7db84e" />

