# 📁 Folder Tree to Mermaid Diagram

🎯 Purpose

This project was built to make it easier for developers, students, and teams to understand the folder structure of their projects at a glance.

Instead of reading through nested folders manually, this tool:

    📂 Reads the folder structure from a given path

    🧠 Converts it into a clean, visual Mermaid.js diagram

    👁️ Helps you quickly visualize your project's architecture

⚠️ This tool is designed to run locally on your own machine.

It’s perfect for:

    Software development

    Research projects

    Codebase audits

    Learning project structure patterns

Whether you're reviewing your own project or helping others understand theirs — this tool keeps things simple, safe, and helpful.


A Flask-powered web app that lets you input a local folder path and visualize its structure as a [Mermaid.js](https://mermaid.js.org/) diagram.  
Supports layout direction switching, zooming, and downloading the diagram as SVG.

---

## 🚀 Features

- ✅ Converts any folder tree into a Mermaid diagram
- ✅ Choose layout direction: `Top-Down (TD)`, `Left-Right (LR)`, `Bottom-Top (BT)`, `Right-Left (RL)`
- ✅ Zoom in/out and reset zoom
- ✅ Ctrl + scroll zoom support
- ✅ Download diagram as `.svg`
- ✅ Built with **Flask** + **Vanilla HTML/JS**

---

## 📦 Project Structure

TreeFolderProject/
├── Tree_Folder.py # Flask backend
└── templates/
└── index.html # Frontend interface

---

## 🛠 Requirements

- Python 3.7+
- Flask

---

## ⚙️ Setup Instructions

```bash
# 1. Clone this repo or copy the files
git clone https://github.com/your-username/folder-tree-mermaid.git
cd folder-tree-mermaid

# 2. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install Flask
pip install flask

# 4. Run the app
python Tree_Folder.py

Then visit: http://127.0.0.1:5000

🧪 How to Use
Enter the full path to a folder on your computer.

Choose a layout direction from the dropdown.

Click Generate to render the Mermaid diagram.

Use the Zoom buttons or Ctrl + scroll to zoom in/out.

Click Download to save the diagram as an SVG file.

💡 Tips
Large folder structures may exceed Mermaid's size limits.

Try reducing tree depth or limiting file count.

You can modify the backend to cap folder depth (e.g., max_depth=4).- 

Other Info : EXCLUDE_DIRS List

📦 Explanation of Each:
Folder Name	                    Reason to Exclude
.venv, venv, env, envs	        Python virtual environments (can have 1000s of files)
__pycache__	                    Python compiled bytecode
.git, .github	                Git internals and workflows
.vscode, .idea	                IDE/editor settings (VS Code, PyCharm)
node_modules	                JavaScript dependencies — often >10,000 files
dist, build	                    Build output (e.g. from Webpack, PyInstaller, etc.)
.pytest_cache	                Pytest run cache
.mypy_cache	                    Mypy type check cache
.cache	                        Generic tool cache (e.g. pip, poetry)
site-packages	                Python installed packages (if not inside .venv)
.DS_Store, __MACOSX	            MacOS system folders

