"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""
    form_github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(form_github)

    grades = hackbright.get_grades_by_github(form_github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add-form")
def display_student_add_form():

    return render_template("create_new_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first = request.form.get('fname')
    last = request.form.get('lname')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)


@app.route("/project/<title>")
def display_project(title):
    """Displays project info."""

    # title = request.args.get("title")
    project_info = hackbright.get_project_by_title(title)
    print len(project_info)
    
    return render_template("project_info.html",
                            project_info=project_info[1:])


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
