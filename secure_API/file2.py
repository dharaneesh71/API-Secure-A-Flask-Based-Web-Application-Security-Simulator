import tkinter as tk
import requests

def simulate_sql_injection():
    username = entry_username.get()
    password = entry_password.get()
    response = requests.post("http://127.0.0.1:5000/vulnerable_sql", data={'username': username, 'password': password})
    result_label.config(text=f"Response: {response.json().get('message')}")

def simulate_xss():
    comment = entry_comment.get()
    response = requests.post("http://127.0.0.1:5000/vulnerable_xss", data={'comment': comment})
    result_label.config(text=f"Response: {response.json().get('message')} - Comment: {response.json().get('comment')}")

# Set up the Tkinter GUI
app = tk.Tk()
app.title("Attack Simulator")

tk.Label(app, text="SQL Injection Simulator").pack()
tk.Label(app, text="Username:").pack()
entry_username = tk.Entry(app)
entry_username.pack()
tk.Label(app, text="Password:").pack()
entry_password = tk.Entry(app, show='*')
entry_password.pack()
tk.Button(app, text="Simulate SQL Injection", command=simulate_sql_injection).pack()

tk.Label(app, text="XSS Simulator").pack()
tk.Label(app, text="Comment:").pack()
entry_comment = tk.Entry(app)
entry_comment.pack()
tk.Button(app, text="Simulate XSS", command=simulate_xss).pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
