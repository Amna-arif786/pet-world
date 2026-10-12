# 🐾 Pet World

A full-stack **Django** web application for pet lovers — share your pets, browse breeds, and learn daily care tips.

Built as a portfolio project with Python, Django, and vanilla HTML/CSS/JS.

---

## ✨ Features

### 🐶 Pets
- Share your pet with a photo, name, age, and description
- Browse pets with category filters (Dog / Cat / Bird / Other)
- Photo gallery of all shared pets
- 👍 Like / unlike pets with instant AJAX updates (no page reload)
- Homepage shows latest pets and a top-liked leaderboard

### 📖 Care
- Beginner's guide for new pet owners
- Daily care tips organized by level (Beginner, Daily Care, Health, Home Setup)
- Detailed food guides per pet type — good foods, bad foods, feeding & water tips

### 🐕 Breeds
- Browse breeds with filters by pet type
- Each breed page covers temperament, size, lifespan, daily care, food guide, dangerous foods, and common mistakes
- "Good for beginners" flag to help first-time owners

### 🌐 General
- Responsive layout with dark theme
- About and Contact pages for each section
- Session-based "liked pets" tracking per user

---

## 🛠️ Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python 3.10, Django 5.1             |
| Database  | SQLite 3 (dev)                      |
| Images    | Pillow                              |
| Frontend  | HTML5, CSS3, vanilla JavaScript     |
| Config    | `python-dotenv` (env-based settings)|

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Amna-arif786/pet-world.git
cd pet-world

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your environment file
copy .env.example .env       # Windows
# cp .env.example .env       # macOS / Linux
```

Then open `.env` and set your own `SECRET_KEY` (generate one with):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Database Setup

```bash
python manage.py migrate

# Load sample data (optional, but recommended to see the site in action)
python seed_guides.py    # care tips + food guides
python seed_pets.py      # sample pets
python seed_photos.py    # pet photos (downloads images)
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

### Admin Panel

```bash
python manage.py createsuperuser
```
Then go to **http://127.0.0.1:8000/admin/** to manage pets, tips, and breeds.

---

## 📁 Project Structure

```
pet_world/
├── pet_world/          # Project config (settings, urls, wsgi)
├── pets/               # App: pet listings, gallery, likes, add pet
├── care/               # App: care tips and food guides
├── breeds/             # App: breed directory
├── templates/          # Global + per-app HTML templates
├── static/             # CSS and JavaScript
├── media/              # Uploaded / seeded pet photos
├── seed_guides.py      # Sample care data
├── seed_pets.py        # Sample pet data
├── seed_photos.py      # Downloads sample pet photos
└── manage.py
```

---

## 🌍 Deployment Notes

For production (Render, Railway, PythonAnywhere, etc.):

1. Set `DEBUG=False` in `.env`
2. Set `ALLOWED_HOSTS` to your real domain(s)
3. Use a strong, unique `SECRET_KEY`
4. Switch to PostgreSQL by updating `DATABASES` in `pet_world/settings.py`
5. Run `python manage.py collectstatic` to gather static files

---

## 📜 License

This project is open source — feel free to use it for learning and inspiration.

---

Made with ❤️ in Python & Django
