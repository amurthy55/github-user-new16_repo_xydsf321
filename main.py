```json
{
  "files": [
    {
      "file_name": "main.py",
      "content": "from flask import Flask, render_template, request, jsonify\nimport requests\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\n@app.route('/github_user/<seed>', methods=['GET'])\ndef github_user(seed):\n    token = request.args.get('token')\n    username = request.args.get('username')\n    headers = {'Authorization': f'token {token}'} if token else {}\n    response = requests.get(f'https://api.github.com/users/{username}', headers=headers)\n    if response.status_code == 200:\n        data = response.json()\n        created_at = data['created_at'][:10]  # YYYY-MM-DD\n        return jsonify({'created_at': created_at})\n    return jsonify({'error': 'User not found'}), 404\n\nif __name__ == '__main__':\n    app.run(debug=True)"
    },
    {
      "file_name": "README.md",
      "content": "# GitHub User Fetcher\n\nThis is a minimal Flask application that fetches a GitHub user's account creation date.\n\n## Setup\n1. Install Flask and Requests:\n   ```bash\n   pip install Flask requests\n   ```\n2. Run the application:\n   ```bash\n   python main.py\n   ```\n3. Open your browser and go to `http://127.0.0.1:5000/`.\n\n## Usage\n- The main page contains a form to input a GitHub username.\n- Optionally, you can provide a GitHub token as a query parameter.\n- The account creation date will be displayed in the format YYYY-MM-DD UTC."
    }
  ]
}
```