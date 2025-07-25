# 🌾 Farmer-Middleman Web Platform (Flask + SQLite)

### ⚙️ A full-stack web application designed to streamline communication and transactions between Farmers and Middlemen

---

## 📜 About This Project

This project is a **major real-world-inspired web platform** aimed at helping **farmers and middlemen** manage crop sales, loans, interest tracking, and essential agricultural transactions.

I started building this application **right after learning the web development basics**, using **Flask, HTML, CSS, JavaScript, and SQLite**. Back then, I didn't know React, MongoDB, or how to structure large-scale applications.

> ⚠️ **Disclaimer**: This project is currently not fully functional — many features are incomplete or broken, and the UI design is very basic. It was my **very first project**, so naturally it has a lot of rough edges. But it’s where my developer journey truly began.

Since then, I’ve learned a lot — from building **clean UIs** to working with **modern stacks** like **MERN, REST APIs, and React**. I’ve developed and deployed multiple functional, scalable applications.  
However, this project holds a special place in my growth, and I’ve decided to **revisit and rebuild it**, now that I have the knowledge and experience to do it justice.

---

## 🎯 Core Objectives

- Provide an online platform for **farmers** to:

  - Register their land and crop details
  - Manage debt taken from middlemen
  - Track repayment history

- Allow **middlemen** to:
  - Manage financial loans to farmers
  - Track interest rates and transactions
  - View farmer records and crop associations

---

## 🛠 Tech Stack

| Layer       | Technologies                          |
| ----------- | ------------------------------------- |
| Frontend    | HTML, CSS, JavaScript                 |
| Backend     | Python (Flask)                        |
| Database    | SQLite                                |
| Environment | Python-dotenv (for secret management) |

---

## 🚀 Current Features

✅ User Registration & Login (Farmer / Middleman)  
✅ Session Management  
✅ Basic Dashboards for both roles  
✅ Data storage  
✅ Responsive templates using Jinja2

---

## ❌ Limitations (For Now)

- UI/UX is very basic
- No CRUD operations yet for transactions or crops
- Many pages are placeholders or partially implemented
- No validations or security enhancements
- Not yet mobile responsive
- Project may not run properly without minor fixes

---

## 📌 Pending Features

- [ ] Proper dashboard design & data visualization
- [ ] Role-based transaction tracking
- [ ] Loan repayment system
- [ ] Email-based verification & alerts
- [ ] Full CRUD operations for crops, loans, fertilizers
- [ ] Admin Panel (future enhancement)

---

## 🧠 Why I’m Revisiting It

> _"This was my very first step into full-stack development — raw, messy, and experimental. But it was mine."_

I never pushed this project to GitHub earlier, and I kept putting off revisiting it. But now, with a solid grasp of:

- React & MERN stack
- RESTful APIs
- Scalable app architecture
- UI design principles

I’m **ready to complete and improve this project** — not just to fix it, but to **transform it into something truly valuable**.

---

## Future Plans

I plan to either:

- **Complete this version using Flask**, or
- **Refactor the entire app using a modern stack** with REST APIs and better UI

Either way, this repo will always stand as a symbol of **progress**.

---

## 🤝 Contributing

This is currently a **solo personal project**, but if you'd like to share ideas or improvements, feel free to open an issue or reach out via [LinkedIn](https://www.linkedin.com/in/hitesh-kumar-248540270).

---

## 📂 Project Setup

```bash
# Clone the repo
git clone https://github.com/hitesh-minhas/farmer-middleman-platform.git
cd farmer-middleman-platform

# Install dependencies
pip install -r requirements.txt

# Create a .env file in the root directory and add your secret key
echo "SECRET_KEY=your_secret_key_here" > .env

# Run the app
python main.py
```
