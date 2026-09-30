# 🍽️ Calorie Counter Application

This is a **calorie tracking web application** built using Python and the Django framework. It allows users to calculate their BMR (Basal Metabolic Rate) and track their daily food intake and calorie consumption.

## ✨ Features
- **User System:** Account registration, login, logout, and password change.
- **Profile Management:** Update profiles by setting age, weight, height, and gender.
- **BMR Calculator:** Dynamic BMR calculation based on user data.
- **Daily Food Log:** Ability to add and delete daily food entries.
- **Dashboard Summary:** Animated progress bars and dynamic health guidelines.

## 🚀 How to Run

Follow the steps below to run the project on your local computer:

### 1. Clone the project
```bash
git clone https://github.com
cd calorie-counter
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```
Now, visit the following URL in your browser: `http://127.0.0`

## 🛠️ Technology Stack
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite