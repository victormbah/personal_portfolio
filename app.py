from flask import Flask, render_template  # Import Flask and render_template function

app = Flask(__name__)  # Create a Flask app instance

# Define the home route (URL: "/")
@app.route('/')
def home():
    return render_template('index.html')  # Load the homepage

# Define the projects route (URL: "/projects")
@app.route('/projects')
def projects():
    return render_template('projects.html')  # Load the projects page

# Define the contact route (URL: "/contact")
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Load the contact page

# Run the app 
if __name__ == '__main__':
    app.run(debug=True)
