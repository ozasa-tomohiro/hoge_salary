from flask import flash


def judge_salary(salary):
    flag = False
    if salary == "":
        flash("給与が未記入です。入力してください。")
    elif int(salary) < 0:
        flash("給与にはマイナス値は入力できません。")
    elif len(salary) > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
    else:
        flag = True
    return flag
