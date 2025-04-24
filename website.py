from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Your HTML content (as string)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vulnerable Practice Site</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
    }
    body {
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(135deg, #e0eafc, #cfdef3);
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 600px;
      margin: 60px auto;
      background-color: #fff;
      padding: 40px 30px;
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    h1 {
      color: #2c3e50;
      font-size: 28px;
      margin-bottom: 10px;
    }
    h2 {
      color: #34495e;
      font-size: 18px;
      margin-top: 30px;
    }
    p {
      font-size: 14px;
      color: #555;
      line-height: 1.6;
    }
    input[type="text"], input[type="password"] {
      width: 100%;
      padding: 12px;
      margin: 10px 0 20px;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 14px;
    }
    button {
      width: 100%;
      padding: 12px;
      background-color: #003366;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    button:hover {
      background-color: #001f4d;
    }
    a {
      color: #e74c3c;
      display: inline-block;
      margin-top: 8px;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to the Vulnerable Practice Site</h1>
    <p>This page intentionally includes common misconfigurations for security testing purposes.</p>

    <h2>Login (Default Credentials: admin / admin)</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="Username" value="admin">
      <input type="password" name="password" placeholder="Password" value="admin">
      <button type="submit">Login</button>
    </form>

    <h2>Admin Panel</h2>
    <p>This page is publicly accessible without authentication:</p>
    <a href="/admin">Go to Admin Panel</a>

    <h2>Configuration Exposure</h2>
    <p>Click to access potentially sensitive files:</p>
    <a href="/.env">.env File</a>
    <a href="/.git/config">.git/config</a>
  </div>
</body>
</html>
"""


# Main login route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            return redirect(url_for("admin_panel"))
        return "Invalid credentials"
    return render_template_string(html_content)

# Publicly accessible admin page
@app.route("/admin")
def admin_panel():
    return "<h1>Admin Panel</h1><p>Welcome, admin. This page is not protected.</p>"

# Simulate config file exposure
@app.route("/.env")
@app.route("/.git/config")
def exposed_config():
    return "Sensitive config exposed!", 200

# Run the app
if __name__ == "__main__":
 app.run(debug=True)