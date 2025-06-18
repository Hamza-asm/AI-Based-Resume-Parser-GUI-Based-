# 🧠 AI-Based Resume Parser (GUI Based)

This project is an AI-powered resume parser and scoring system built with Python. It allows recruiters or institutions to automatically score and filter resumes based on relevance to specific job categories using keyword matching and a graphical interface (GUI).

## 📌 Project Description

Recruiters often receive hundreds of resumes for a single job post. Manually reviewing them is time-consuming. This tool streamlines that process by:
- Reading resumes from a CSV file.
- Matching content against predefined job-category keywords.
- Assigning a suitability score (0–10) to each resume.
- Exporting the results in a new CSV file sorted by scores.
- Providing a simple GUI for file upload and result export.



## 🛠️ Features

- ✅ Resume scoring based on relevance to job categories.
- ✅ GUI-based interaction using Tkinter.
- ✅ Output as a new CSV file sorted by score.
- ✅ Lightweight and beginner-friendly (no NLTK or ML libraries).

---

## 🗂️ Dataset Format

The tool expects a CSV file with the following two columns:

| Category     | Resume                          |
|--------------|----------------------------------|
| Data Science | Areas of Interest Deep Learning, Control System Design, Programming in-Python, Electric Machinery, Web Development, Analytics Technical Activities       |
| HR           | Training in Special Education (Certificate Course) Education Details July 2016 to October 2018 M.Sc Psychology with specialization in Organizational Behaviour Malappuram, Kerala Calicut University |
| Web Developer | Technical Skills Web Technologies: Angular JS, HTML5, CSS3, SASS, Bootstrap, Jquery, Javascript. Software: Brackets, Visual Studio, Photoshop, Visual Studio Code     |

---

## 💻 GUI Preview

### Initial UI
![image](https://github.com/user-attachments/assets/dced99f1-0ed8-4405-8834-ff53b8b619d4)

### Selecting File
![image](https://github.com/user-attachments/assets/b8df1802-56af-4927-b33f-7eefe42a8fee)



---

## 🧾 Dependencies

Install these packages before running the project:

```bash
pip install pandas
pip install tk
