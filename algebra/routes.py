import datetime
import json
import os
import random

from flask import Blueprint, render_template, session

from ..log import Log


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

algebra_bp = Blueprint('algebra_bp', __name__, template_folder='templates', static_folder='static')
log_object = Log()
json_url = os.path.join(SITE_ROOT, "static/data", "qid.json")
data = json.load(open(json_url))
count = 0
startTym = datetime.datetime.now()


@algebra_bp.route("/like-unlike")
def like_unlike():
    global count
    global startTym
    startTym = datetime.datetime.now()
    qid = data['like-unlike']
    q3 = 'State whether a given pair of terms is of like or unlike terms'
    term1 = ['x', 'y', 'xy', 'xy\u00b2', 'x\u00b2y']
    term2 = ['x', 'y', 'yx', random.choice(['y\u00b2x', 'xy\u00b2']), random.choice(['yx\u00b2', 'x\u00b2y'])]
    answers = []
    terms = []
    cnt = 0
    while cnt <= 3:
        t1 = random.choice(term1)
        t2 = random.choice(term2)
        x = str(random.randint(1, 25))
        y = str(random.randint(1, 25))
        if term1.index(t1) == term2.index(t2):
            answer = "Like"
        else:
            answer = "Unlike"
        t1 = x + t1
        t2 = y + t2
        terms.append([t1, t2])
        answers.append(answer)
        cnt += 1
    contexts = {'qid': qid, 'question': q3, 'options': terms, 'answer': answers, 'num': 2, 'topic': 'Like-Unlike Terms'}
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))

    return render_template('algebra2.html', easy=contexts)


@algebra_bp.route('/value-of-expression')
def value_of_expression():
    global count
    global startTym
    startTym = datetime.datetime.now()
    qid = data['value-of-expression']
    cnt = 0
    variable = ["", "p", "p\u00b2", "p\u00b3"]
    sign = ["+", "-"]
    terms = []
    answers = []
    num = random.randint(2, 10)
    q4 = "If p = " + str(num) + ", find the value of "
    while cnt < 4:
        c1 = random.randint(1, 10)
        c2 = random.randint(1, 10)
        c3 = random.randint(1, 10)
        s1 = random.choice(sign)
        s2 = random.choice(sign)
        v1 = random.choice(variable)
        v2 = random.choice(variable)
        v3 = random.choice(variable)
        term = str(c1) + str(v1) + str(s1) + str(c2) + str(v2) + str(s2) + str(c3) + str(v3)
        i1 = find_term(v1, variable)
        i2 = find_term(v2, variable)
        i3 = find_term(v3, variable)
        var1 = num ** i1
        var2 = num ** i2
        var3 = num ** i3
        if s1 == "+" and s2 == "+":
            answer = c1 * var1 + c2 * var2 + c3 * var3
        elif s1 == "+" and s2 == "-":
            answer = c1 * var1 + c2 * var2 - c3 * var3
        elif s1 == "-" and s2 == "-":
            answer = c1 * var1 - c2 * var2 - c3 * var3
        else:
            answer = c1 * var1 - c2 * var2 + c3 * var3
        terms.append(term)
        answers.append(answer)
        cnt += 1
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))

    return render_template('algebra_easy.html',
                           easy={'topic': 'Value of Expression', 'question': q4, 'options': terms, 'answer': answers,
                                 'num': 2, 'qid': qid})


def find_term(v, a):
    return a.index(v)


@algebra_bp.route('/coefficient')
def coefficient():
    global count
    global startTym
    startTym = datetime.datetime.now()
    qid = data['coefficient']
    q1 = 'Identify the numerical coefficients of terms (other than constants) in the following expressions'
    variable = ["x", "x\u00b2", "x\u00b3"]
    sign = ["+", "-"]
    terms = []
    answers = []
    cnt = 0
    while cnt <= 3:
        coeff = random.randint(1, 10)
        num = random.randint(1, 30)
        op = random.choice(sign)
        term = str(num) + op + str(coeff) + random.choice(variable)
        terms.append(term)
        if op == "-":
            answers.append(-coeff)
        else:
            answers.append(coeff)
        cnt += 1
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))
    return render_template('algebra_easy.html',
                           easy={'topic': 'Identifying Coefficient', 'question': q1, 'options': terms,
                                 'answer': answers, 'num': 1, 'qid': qid})


@algebra_bp.route('/monomial')
def monomial():
    global count
    global startTym
    startTym = datetime.datetime.now()
    qid = data['monomial']
    q2 = 'Classify into monomials, binomials and trinomials'
    variable = ["x", "y", "z", "xy", "yz", "xz", "xyz"]
    sign = ["+", "-"]
    answers = []
    terms = []
    cnt = 0
    while cnt <= 3:
        x = random.randint(1, 3)
        if x == 1:
            answer = "Monomial"
            term = str(random.randint(1, 25)) + random.choice(variable)
        elif x == 2:
            answer = "Binomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable)
        else:
            answer = "Trinomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable)
        answers.append(answer)
        terms.append(term)
        cnt += 1

    contexts = {'qid': qid, 'question': q2, 'options': terms, 'answer': answers, 'num': 1,
                'topic': 'Monomial Binomial Trinomial'}
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))

    return render_template('algebra2.html', easy=contexts)


@algebra_bp.route("/algebra-add")
def horizontal_add():
    global count
    global startTym
    startTym = datetime.datetime.now()
    qid = data['algebra-add']
    coeff = random.sample(range(-50, 50), 6)
    varx = ['x', 'x\u00b2', 'x\u00b3']
    vary = ['y', 'y\u00b2', 'y\u00b3']
    rx = random.choice(varx)
    ry = random.choice(vary)
    sign = []
    for i in coeff[1:6:2]:
        if i < 0:
            sign.append('')
        else:
            sign.append('+')

    haddque = 'Add horizontally ' + str(coeff[0]) + rx + sign[0] + str(coeff[1]) + ry + ',' + str(coeff[2]) + rx + sign[
        1] + str(coeff[3]) + ry + ',' + str(coeff[4]) + rx + sign[2] + str(coeff[5]) + ry
    x_like = coeff[0:5:2]
    x_sum = sum(x_like)
    y_like = coeff[1:6:2]
    y_sum = sum(y_like)
    answer = {'qid': qid, 'que': haddque, 'varx': rx, 'vary': ry, 'coeff': coeff, 'x_like': x_like, 'y_like': y_like,
              'x_sum': x_sum, 'y_sum': y_sum}
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))
    return render_template('algebra_add.html', answer=answer)


@algebra_bp.route('/vertical_sub')
def vertical_sub():
    global count
    global startTym
    startTym = datetime.datetime.now()

    qid = data['vertical-sub']
    coeff = random.sample(range(-50, 50), 6)
    varx = ['x', 'x\u00b2', 'x\u00b3']
    vary = ['y', 'y\u00b2', 'y\u00b3']
    varz = ['z', 'z\u00b2', 'z\u00b3']
    rx = random.choice(varx)
    ry = random.choice(vary)
    rz = random.choice(varz)
    sign_1 = []
    for i in coeff[1:3]:
        if i < 0:
            sign_1.append('')
        else:
            sign_1.append('+')
    sign_2 = []
    for j in coeff[4:7]:
        if j < 0:
            sign_2.append("")
        else:
            sign_2.append('+')
    haddque = 'Sub Vertically ' + str(coeff[0]) + rx + str(sign_1[0]) + str(coeff[1]) + ry + str(sign_1[1]) + str(
        coeff[2]) + rz + ' , ' + str(coeff[3]) + rx + str(sign_2[0]) + str(coeff[4]) + ry + str(sign_2[1]) + str(
        coeff[5]) + rz + ' . '
    x_diff = coeff[0] - coeff[3]
    y_diff = coeff[1] - coeff[4]
    z_diff = coeff[2] - coeff[5]
    answer = {'qid': qid, 'que': haddque, 'varx': rx, 'vary': ry, 'varz': rz, 'coeff': coeff, 'x_diff': x_diff,
              'y_diff': y_diff, 'z_diff': z_diff}
    count += 1
    message = {"userid": session['userid'], "qid": qid, "qcount": count}
    log_object.log_entry(json.dumps(message))
    return render_template('vertical_sub.html', answer=answer)
