import os

# Create project structure
folders = [
    "student-registration",
    "student-registration/public",
    "student-registration/models"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -------------------- server.js --------------------
server_js = """\
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const Student = require('./models/Student');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public'));

mongoose.connect('mongodb://127.0.0.1:27017/studentdb', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

app.post('/register', async (req, res) => {
  try {
    const { studentName, studentEmail, studentId } = req.body;

    if (!studentName || !studentEmail || !studentId) {
      return res.status(400).json({ message: 'All fields are required' });
    }

    const newStudent = new Student({ studentName, studentEmail, studentId });
    await newStudent.save();

    res.status(201).json({ message: 'Student registered successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

app.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
"""

# -------------------- Student.js --------------------
student_model = """\
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema({
  studentName: { type: String, required: true },
  studentEmail: { type: String, required: true },
  studentId: { type: String, required: true }
});

module.exports = mongoose.model('Student', studentSchema);
"""

# -------------------- index.html --------------------
index_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Student Registration Form</h2>
        <form id="registrationForm">
            <div class="form-group">
                <label for="studentName">Full Name:</label>
                <input type="text" id="studentName" name="studentName" required>
            </div>

            <div class="form-group">
                <label for="studentEmail">Email:</label>
                <input type="email" id="studentEmail" name="studentEmail" required>
            </div>

            <div class="form-group">
                <label for="studentId">Student ID:</label>
                <input type="text" id="studentId" name="studentId" required>
            </div>

            <button type="submit">Register</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

# -------------------- style.css --------------------
style_css = """\
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background-color: #fff;
    padding: 20px 40px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

.form-group {
    margin-bottom: 15px;
}
label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"] {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}
button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
"""

# -------------------- script.js --------------------
script_js = """\
document.getElementById('registrationForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const studentName = document.getElementById('studentName').value;
    const studentEmail = document.getElementById('studentEmail').value;
    const studentId = document.getElementById('studentId').value;

    fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ studentName, studentEmail, studentId })
    })
    .then(res => res.json())
    .then(data => alert(data.message))
    .catch(err => alert('Error: ' + err.message));
});
"""

# Write files
files_to_create = {
    "student-registration/server.js": server_js,
    "student-registration/models/Student.js": student_model,
    "student-registration/public/index.html": index_html,
    "student-registration/public/style.css": style_css,
    "student-registration/public/script.js": script_js
}

for path, content in files_to_create.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Project created: student-registration")
print("👉 Now run: cd student-registration && npm init -y && npm install express mongoose body-parser cors")