from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates')

EXCLUDE_DIRS = {
    ".venv", "venv", "__pycache__",
    ".git", ".github", ".idea", ".vscode",
    "node_modules", "dist", "build",
    ".pytest_cache", ".mypy_cache", ".cache",
    "env", "envs", "site-packages",
    ".DS_Store", "__MACOSX"
}

def get_tree_lines(startpath, prefix="", depth=0, max_depth=5):
    if depth > max_depth:
        return []

    lines = []
    try:
        items = os.listdir(startpath)
    except Exception as e:
        lines.append(prefix + f"⚠️ [Error accessing]: {e}")
        return lines

    for index, item in enumerate(sorted(items)):
        path = os.path.join(startpath, item)
        connector = "├── " if index < len(items) - 1 else "└── "
        lines.append(prefix + connector + item)

        if os.path.isdir(path) and item.lower() not in EXCLUDE_DIRS:
            extension = "│   " if index < len(items) - 1 else "    "
            lines.extend(get_tree_lines(path, prefix + extension, depth + 1, max_depth))
    return lines





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-tree', methods=['POST'])
def get_tree():
    data = request.get_json()
    folder_path = data.get('path', '')

    if not os.path.exists(folder_path):
        return jsonify({"error": "Path not found"}), 404

    tree_lines = get_tree_lines(folder_path, max_depth=4)  # Limit to 4 levels deep

    return jsonify({"tree": tree_lines})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)