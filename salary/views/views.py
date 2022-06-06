from flask import redirect, request, render_template, url_for
from salary import app
from salary.views.cal_salary import cal_salary
from salary.views.judge_salary import judge_salary


@app.route("/", methods=["GET"])
def input():
    if request.method == "GET":
        return render_template("input.html")


@app.route("/output", methods=["POST"])
def output():
    salary = request.form.get("salary")
    flag = judge_salary(salary)

    if flag is False:
        return redirect(url_for('input'))
    else:
        get_salary, tax_salary = cal_salary(int(salary))
        return render_template("output.html", salary=int(salary), get_salary=get_salary, tax_salary=tax_salary)
