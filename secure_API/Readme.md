# Flask API Security Simulation Report

## Overview
This Flask-based web application demonstrates the simulation of various security vulnerabilities such as:
- **SQL Injection**
- **Cross-Site Scripting (XSS)**  
It also showcases protection techniques like input sanitization and rate limiting. The goal is to educate users about common attack vectors in web applications and the corresponding mitigation techniques. The application features a logging mechanism to record detected attacks and provides an interface to view and manage these logs.

---

## Features
1. **SQL Injection Simulation**  
   - Demonstrates SQL Injection vulnerabilities and their detection.  
   - Logs detected attacks in a secure database.

2. **XSS Simulation**  
   - Uses the Bleach library for input sanitization.  
   - Protects user inputs by filtering out malicious content.

3. **Rate Limiting**  
   - Implements rate limiting using Flask-Limiter to mitigate Denial of Service (DoS) attacks.

4. **Attack Logging System**  
   - Maintains a log of detected attack attempts for analysis.  
   - Provides routes to view and clear logs.

---

## Technologies Used
- **Flask**: Lightweight Python web framework.
- **SQLAlchemy**: ORM for database management.
- **SQLite**: Database to store user credentials and attack logs.
- **Bleach**: Library for sanitizing user inputs.
- **Flask-Limiter**: Library for implementing rate limits.

---

## Application Routes
### Simulation Routes
- `/vulnerable_sql`  
  Simulates SQL Injection and logs any detected attacks.  
- `/vulnerable_xss`  
  Simulates XSS vulnerabilities with sanitized input handling.

### Protection and Utility Routes
- `/rate_limited_api`  
  Enforces a rate limit of 5 requests per minute per IP.  
- `/logs`  
  Displays all logged attacks in a user-friendly interface.  
- `/clear_logs`  
  Allows clearing of all attack logs from the database.

---

## Database Models
1. **User Model**  
   - Fields: `id`, `username`, `email`, `password`.

2. **Log Model**  
   - Fields: `id`, `attack_type`, `timestamp`.

---

## Future Improvements
- **User Authentication**  
  Implement session-based authentication with hashed passwords.  
- **Advanced Logging**  
  Include details like IP addresses and request headers.  
- **Comprehensive Testing**  
  Add unit tests for improved robustness and reliability.

---

## How to Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
