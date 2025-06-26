# ☁️ Everskies Set Manager – CRUD App with File Persistence

This Python application helps manage virtual fashion sets for **Everskies.com** — a creativity-driven dress-up and social platform.

Built as an assignment for **Python Programming** at **Sheridan College**, the project uses **OOP**, **JSON data persistence**, and clean **exception handling** to allow users to create, view, edit, and delete set records with ease.

---

## 🧩 Features

* 🌟 Add a new set with **Designer** and **Set Name**
* 🔍 Search sets by **Designer** or **Set Name**
* 📝 Edit a set’s name using its unique ID
* 🗑️ Delete a set by ID
* 💾 All data is saved to a `JSON` file automatically
* 🧠 Graceful error handling (invalid input, missing files, etc.)
* 🧙🏻‍♀️ Cute interface inspired by the ✨Everskies aesthetic

---

## 🚀 How to Run

### 1. Clone or Download the Repository

```bash
git clone https://github.com/MaryamElhamidi/A4_Repository.git
cd A4_Repository
```

### 2. Run the Program

Make sure you have Python 3 installed, then:

```bash
python main.py
```

You’ll be greeted with a menu where you can start managing your virtual fashion sets.

---

## 📂 Project Structure

| File                 | Purpose                                                |
| -------------------- | ------------------------------------------------------ |
| `main.py`            | Entry point – initializes UI and runs main loop        |
| `UI.py`              | Handles user input/output and connects logic           |
| `Resource.py`        | Class for individual sets (`id`, `designer`, `name`)   |
| `ResourceManager.py` | Logic for creating, searching, updating, deleting sets |
| `Application.py`     | Manages saving/loading JSON data                       |
| `data.json`          | Local storage file (automatically created)             |

---

## 🎨 Sample Program Flow

```
┌── ⋆⋅☆⋅⋆ ──┐
✰ Welcome to Everskies Set Creation Centre ✰
└── ⋆⋅☆⋅⋆ ──┘

1. Create
2. Read (Search)
3. Edit
4. Delete
0. Exit
Enter your choice ₍ ᐢ.ˬ.ᐢ₎: 1
```

---

## ❗ Exception Handling

The program gracefully handles:

* Invalid menu inputs (non-integers, out-of-range)
* File not found errors (when reading JSON)
* Corrupt or empty `data.json` file
* Search or edit attempts on missing IDs

No crashing — just helpful messages and retry opportunities. 🌟

---

## ✏️ Sample JSON Output (Saved Automatically)

```json
[
  {
    "id": "1234",
    "set_Designer": "helmi",
    "set_Name": "clouds"
  },
  {
    "id": "5678",
    "set_Designer": "yammy",
    "set_Name": "setters"
  }
]
```

---

## ⚙️ Tech Used

* 🐍 Python 3
* 🗃️ JSON for local file storage
* 👩‍💻 Object-Oriented Programming (4 classes)
* 🛡️ Try/Except blocks for error control

---

## 💡 Future Improvements

* Add timestamp or creation date
* Limit duplicate IDs or names
* Add sorting or filtering options
* GUI version with `tkinter` or `PyQt`

---
