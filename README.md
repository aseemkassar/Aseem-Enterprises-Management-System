# Aseem Enterprises – Management System

Desktop applications built with **Python and Tkinter** for managing students and users. The repository contains two independent apps: one using **SQLite** and one using **MySQL**.

---

## App 1: Student Management System (SQLite)

**File:** `box2.py`

### Features
- User login and registration with hashed passwords
- Role-based data isolation: each user sees only the students they created
- Student records: name, father's name, class, roll number, phone, email, address, course, join date, fee amount and fee status
- Dashboard analytics: **total students** and **pending fees**
- Student table (Treeview) with newest records first
- SQLite database (`aseem_enterprises.db`) is created automatically on first run

### Run
```bash
python box2.py
```
Demo login: `admin` / `admin123`

---

## App 2: Management System (MySQL)

**Files:** `database.py`, `LoginForm.py`, `Register.py`, `CMS_Form.py`

### Features
- Registration and login screens connected to a MySQL database (`kryptoradb`, table `std_info`)
- Dashboard with side menu: **User Details**, **Reports**, **Settings**, **Logout**
- User Details table, total registered users report and a live date/time clock

### Requirements
- Python 3.8+
- MySQL server running on `localhost` (for example via XAMPP), user `root`, empty password
- PyMySQL:
```bash
pip install pymysql
```

### Run
```bash
python database.py     # one time: creates the database and table
python LoginForm.py    # start the app
```

---

## Project Structure
```
.
├── box2.py          # SQLite student management app
├── database.py      # MySQL database and table setup
├── LoginForm.py     # Login screen (MySQL app)
├── Register.py      # Registration screen (MySQL app)
├── CMS_Form.py      # Dashboard (MySQL app)
└── README.md
```

## Tech Stack
Python, Tkinter, SQLite, MySQL, PyMySQL

## Note
This is a learning project. Demo credentials are for testing only.

## Author
**Mohd Aseem** – [GitHub](https://github.com/aseemkassar)
