import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import hashlib

class AseemEnterprises:
    def __init__(self, root):
        self.root = root
        self.root.title("🏫 ASEEM ENTERPRISES")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f2f5')
        self.setup_database()
        self.current_user = None
        self.create_login_screen()
    
    def setup_database(self):
        self.conn = sqlite3.connect('aseem_enterprises.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL, role TEXT DEFAULT 'coach', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT NOT NULL, father_name TEXT NOT NULL, class TEXT NOT NULL, roll_no TEXT UNIQUE NOT NULL, phone TEXT, email TEXT, address TEXT, course TEXT, join_date DATE, fee_amount REAL, fee_status TEXT DEFAULT 'pending', created_by INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (created_by) REFERENCES users (id))''')
        self.cursor.execute("INSERT OR IGNORE INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", ("admin", "admin@aseem.com", hashlib.md5("admin123".encode()).hexdigest(), "admin"))
        self.conn.commit()
    
    def hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()
    
    def create_login_screen(self):
        for widget in self.root.winfo_children(): widget.destroy()
        main_frame = tk.Frame(self.root, bg='#667eea', height=700); main_frame.pack(fill='both', expand=True)
        
        header_frame = tk.Frame(main_frame, bg='#764ba2', height=150); header_frame.pack(fill='x', pady=(0, 20)); header_frame.pack_propagate(False)
        tk.Label(header_frame, text="🏫 ASEEM ENTERPRISES", font=('Arial', 28, 'bold'), fg='white', bg='#764ba2').pack(pady=30)
        tk.Label(header_frame, text="Student Management System", font=('Arial', 16), fg='white', bg='#764ba2').pack()
        
        form_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2); form_frame.pack(expand=True, padx=50, pady=20, fill='both')
        tk.Label(form_frame, text="🔐 LOGIN", font=('Arial', 20, 'bold'), bg='white', fg='#333').pack(pady=30)
        
        tk.Label(form_frame, text="Username", font=('Arial', 12), bg='white', fg='#555').pack(pady=5)
        self.username_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, relief='solid', bd=1); self.username_entry.pack(pady=5, padx=50); self.username_entry.insert(0, "admin")
        
        tk.Label(form_frame, text="Password", font=('Arial', 12), bg='white', fg='#555').pack(pady=(20,5))
        self.password_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, show='*', relief='solid', bd=1); self.password_entry.pack(pady=5, padx=50); self.password_entry.insert(0, "admin123")
        
        btn_frame = tk.Frame(form_frame, bg='white'); btn_frame.pack(pady=30)
        tk.Button(btn_frame, text="LOGIN", font=('Arial', 14, 'bold'), bg='#667eea', fg='white', width=12, height=2, command=self.login, relief='flat', cursor='hand2').pack(side='left', padx=10)
        tk.Button(btn_frame, text="REGISTER", font=('Arial', 14, 'bold'), bg='#28a745', fg='white', width=12, height=2, command=self.create_register_screen, relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def login(self):
        username, password = self.username_entry.get(), self.hash_password(self.password_entry.get())
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user: self.current_user = user; self.show_dashboard()
        else: messagebox.showerror("Error", "Invalid credentials!\nDefault: admin/admin123")
    
    def create_register_screen(self):
        reg_win = tk.Toplevel(self.root); reg_win.title("📝 Register"); reg_win.geometry("400x450"); reg_win.configure(bg='#f0f2f5'); reg_win.resizable(False, False)
        tk.Label(reg_win, text="REGISTER NEW ACCOUNT", font=('Arial', 18, 'bold'), bg='#f0f2f5', fg='#333').pack(pady=30)
        
        tk.Label(reg_win, text="Username", font=('Arial', 12), bg='#f0f2f5').pack(pady=(20,5)); reg_username = tk.Entry(reg_win, font=('Arial', 12), width=25); reg_username.pack(pady=5)
        tk.Label(reg_win, text="Email", font=('Arial', 12), bg='#f0f2f5').pack(pady=(20,5)); reg_email = tk.Entry(reg_win, font=('Arial', 12), width=25); reg_email.pack(pady=5)
        tk.Label(reg_win, text="Password", font=('Arial', 12), bg='#f0f2f5').pack(pady=(20,5)); reg_password = tk.Entry(reg_win, font=('Arial', 12), width=25, show='*'); reg_password.pack(pady=5)
        
        def register():
            try:
                self.cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (reg_username.get(), reg_email.get(), self.hash_password(reg_password.get())))
                self.conn.commit(); messagebox.showinfo("Success", "Registration successful!"); reg_win.destroy()
            except sqlite3.IntegrityError: messagebox.showerror("Error", "Username or Email already exists!")
        
        tk.Button(reg_win, text="REGISTER", font=('Arial', 14, 'bold'), bg='#28a745', fg='white', width=15, height=2, command=register, relief='flat', cursor='hand2').pack(pady=30)
    
    def show_dashboard(self):
        for widget in self.root.winfo_children(): widget.destroy()
        
        header_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2, height=80); header_frame.pack(fill='x', pady=(0,10)); header_frame.pack_propagate(False)
        tk.Label(header_frame, text="🏫 ASEEM ENTERPRISES", font=('Arial', 20, 'bold'), bg='white', fg='#667eea').pack(side='left', padx=20, pady=20)
        tk.Label(header_frame, text=f"Welcome, {self.current_user[1]}!", font=('Arial', 12), bg='white', fg='#666').pack(side='left', padx=20, pady=25)
        tk.Button(header_frame, text="Logout", font=('Arial', 12, 'bold'), bg='#ff6b6b', fg='white', command=self.create_login_screen, relief='flat', cursor='hand2').pack(side='right', padx=20, pady=20)
        tk.Button(header_frame, text="➕ ADD STUDENT", font=('Arial', 12, 'bold'), bg='#28a745', fg='white', width=15, height=1, command=self.show_add_student, relief='flat', cursor='hand2').pack(side='right', padx=10, pady=20)
        
        stats_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2); stats_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(stats_frame, text=f"Total Students: {self.get_student_count()}", font=('Arial', 16, 'bold'), bg='white', fg='#667eea').pack(side='left', padx=30, pady=20)
        tk.Label(stats_frame, text=f"Pending Fees: {self.get_pending_fee_count()}", font=('Arial', 16, 'bold'), bg='white', fg='#ff6b6b').pack(side='left', padx=30, pady=20)
        
        table_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2); table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        columns = ('ID', 'Name', 'Father', 'Class', 'Roll No', 'Phone', 'Fee Status')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=18)
        for col in columns: self.tree.heading(col, text=col); self.tree.column(col, width=120)
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview); self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left', fill='both', expand=True, padx=10, pady=10); scrollbar.pack(side='right', fill='y', pady=10)
        self.load_students()
    
    def get_student_count(self): self.cursor.execute("SELECT COUNT(*) FROM students WHERE created_by=?", (self.current_user[0],)); return self.cursor.fetchone()[0]
    def get_pending_fee_count(self): self.cursor.execute("SELECT COUNT(*) FROM students WHERE fee_status='pending' AND created_by=?", (self.current_user[0],)); return self.cursor.fetchone()[0]
    
    def load_students(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        self.cursor.execute("SELECT id, student_name, father_name, class, roll_no, phone, fee_status FROM students WHERE created_by=? ORDER BY id DESC", (self.current_user[0],))
        for row in self.cursor.fetchall(): self.tree.insert('', 'end', values=row)
    
    def show_add_student(self):
        add_window = tk.Toplevel(self.root); add_window.title("➕ Add New Student"); add_window.geometry("550x750"); add_window.configure(bg='#f0f2f5'); add_window.resizable(True, True)
        
        main_canvas = tk.Canvas(add_window, bg='#f0f2f5'); scrollbar = ttk.Scrollbar(add_window, orient="vertical", command=main_canvas.yview)
        scrollable_frame = tk.Frame(main_canvas, bg='#f0f2f5'); scrollable_frame.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw"); main_canvas.configure(yscrollcommand=scrollbar.set)
        
        tk.Label(scrollable_frame, text="➕ ADD NEW STUDENT", font=('Arial', 20, 'bold'), bg='#f0f2f5', fg='#333').pack(pady=20)
        
        fields = [('Student Name *', 'student_name'), ('Father Name *', 'father_name'), ('Class *', 'class'), ('Roll No *', 'roll_no'), ('Phone', 'phone'), ('Email', 'email'), ('Course', 'course'), ('Address', 'address'), ('Join Date (DD-MM-YYYY)', 'join_date'), ('Fee Amount (₹)', 'fee_amount')]
        self.entries = {}
        for label_text, field_name in fields:
            frame = tk.Frame(scrollable_frame, bg='#f0f2f5'); frame.pack(fill='x', padx=30, pady=8)
            tk.Label(frame, text=label_text, font=('Arial', 11, 'bold'), bg='#f0f2f5', fg='#555', anchor='w').pack(anchor='w')
            entry = tk.Entry(frame, font=('Arial', 11), width=40, relief='solid', bd=1, bg='white'); entry.pack(fill='x', pady=(5,0)); self.entries[field_name] = entry
        
        fee_frame = tk.Frame(scrollable_frame, bg='#f0f2f5'); fee_frame.pack(fill='x', padx=30, pady=15)
        tk.Label(fee_frame, text="Fee Status *", font=('Arial', 11, 'bold'), bg='#f0f2f5', fg='#555', anchor='w').pack(anchor='w')
        self.fee_var = tk.StringVar(value='pending'); ttk.Combobox(fee_frame, textvariable=self.fee_var, values=['pending', 'paid'], font=('Arial', 11), width=37, state='readonly').pack(fill='x', pady=(5,0))
        
        def save_student():
            try:
                required = ['student_name', 'father_name', 'class', 'roll_no']
                for field in required:
                    if not self.entries[field].get().strip(): messagebox.showerror("Error", f"{field.replace('_', ' ').title()} is required!"); return
                
                data = (self.entries[f].get() for f in ['student_name','father_name','class','roll_no','phone','email','address','course','join_date']) + (float(self.entries['fee_amount'].get() or 0), self.fee_var.get(), self.current_user[0])
                self.cursor.execute("INSERT INTO students (student_name, father_name, class, roll_no, phone, email, address, course, join_date, fee_amount, fee_status, created_by) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
                self.conn.commit(); messagebox.showinfo("✅ Success", "Student added successfully!"); add_window.destroy(); self.load_students()
            except ValueError: messagebox.showerror("Error", "Fee amount must be a number!")
            except sqlite3.IntegrityError: messagebox.showerror("Error", "Roll No already exists!")
            except Exception as e: messagebox.showerror("Error", f"Error: {str(e)}")
        
        tk.Button(scrollable_frame, text="💾 SAVE STUDENT", font=('Arial', 16, 'bold'), bg='#28a745', fg='white', width=25, height=2, command=save_student, relief='flat', cursor='hand2').pack(pady=40)
        main_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20); scrollbar.pack(side="right", fill="y", pady=20)
        main_canvas.bind_all("<MouseWheel>", lambda e: main_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        add_window.transient(self.root); add_window.grab_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = AseemEnterprises(root)
    root.mainloop()
