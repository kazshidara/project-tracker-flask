"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html", first=first, last=last, github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/add-student")  #arbitrary route that gets user here if they want to add a new student 
def added_to_db():
    """Show New Student Form"""

    return render_template("new_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a new student form and handle the form results and confirms new student was added."""
   
    first_n = request.form.get('first_name')
    last_n = request.form.get('last_name')
    github_n = request.form.get('github')
    hackbright.make_new_student(first_n, last_n, github_n)
    return render_template("student_added.html", first=first_n, last=last_n, github=github_n)
   






if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
