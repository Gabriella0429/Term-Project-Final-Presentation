from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Your HTML content (as string)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vulnerable Practice Site</title>
  <style>
    body { font-family: Arial; background-color: #f4f4f4; }
    .container { width: 80%; margin: auto; padding: 20px; background: white; margin-top: 50px; border-radius: 10px; }
    input { padding: 10px; margin: 10px 0; width: 100%; }
    button { padding: 10px 20px; background: #003366; color: white; border: none; cursor: pointer; }
    a { color: red; }
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
