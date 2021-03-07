from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask.ext.session import Session
from fractions import Fraction
import random
import os


app = Flask(__name__)


values = [Fraction('25/8'), Fraction('17/4'), Fraction('38/7'), Fraction('29/3'), Fraction('44/5')]
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')

qtscnt1=0     #fraction
scorecnt1=0   #fraction
qtscnt2 = 0   #algebra
scorecnt2 = 0 #algebra

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/mixed-fraction1", methods=['POST'])
def q1():
    if request.method == 'POST':
        global qtscnt,scorecnt
        num = random.randint(1, 100)
        den = random.randint(1, 25)
        while num < den:
            num = random.randint(1, 100)
        que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
        quo = num // den
        rem = num % den
        box_ans = [quo, rem, quo, rem, den]
        answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
        hint1 = 'Try dividing numerator by denominator'
        hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
        hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
        hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
        total = qtscnt * 25
        scoredict = {'score': scorecnt, 'total': total, 'totalqts': qtscnt, 'pct': 0}
        return render_template('display copy.html', answer=answer, hints=hints, scoredict=scoredict)
    else:
        return render_template('login.html')


@app.route("/mixed-fraction")
def question():
    global qtscnt1, scorecnt1
    # print(qtscnt)
    # print(scorecnt)
    num = random.randint(1, 100)
    den = random.randint(1, 25)
    while num < den:
        num = random.randint(1, 100)
    que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
    quo = num // den
    rem = num % den
    box_ans = [quo, rem, quo, rem, den]
    answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    hint1 = 'Try dividing numerator by denominator'
    hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
    hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
    hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
    total = qtscnt1 * 25
    try:
        tcp = (scorecnt1/total)*100
    except:
        tcp = 0
    scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'tcp': tcp}
    return render_template('display copy.html', answer=answer, hints=hints, scoredict=scoredict)


@app.route('/score/<tid>/<counter>/<feedback>', methods=['POST'])
def score(counter, feedback, tid):
    if request.method == 'POST':
        if tid == '1':
            global scorecnt1, qtscnt1
            marks = 25-(int(counter)*5) - (int(feedback)*2)
            scorecnt1 += marks
            qtscnt1 += 1
            # print(scorecnt)
            # print(qtscnt)
            # print(marks)
            if marks == 25:
                comment = "Well Done!!!"
            elif 20 <= marks < 25:
                comment = "You have just about mastered it"
            elif 15 <= marks < 20:
                comment = "Keep working on it you are improving"
            else:
                comment = "That's not half bad"
            show_message1 = 'Your points : '+str(marks)+'/25.'
            flash(show_message1)
            flash(comment)
            return redirect(url_for('question'))
        
        else:
            global scorecnt2, qtscnt2
            marks = 25-(int(counter)*5) - (int(feedback)*2)
            scorecnt2 += marks
            qtscnt2 += 1
            # print(scorecnt)
            # print(qtscnt)
            # print(marks)
            if marks == 25:
                comment = "Well Done!!!"
            elif 20 <= marks < 25:
                comment = "You have just about mastered it"
            elif 15 <= marks < 20:
                comment = "Keep working on it you are improving"
            else:
                comment = "That's not half bad"
           
            show_message1 = 'Your points : '+str(marks)+'/25.'
            flash(show_message1)
            flash(comment)
            return redirect(url_for('horizontal_add'))


@app.route("/algebra-add")
def horizontal_add():
    coeff = random.sample(range(-50,50),6) #6 coefficient
    varx = ['x','x\u00b2','x\u00b3'] #x3
    vary = ['y','y\u00b2','y\u00b3'] #y2
    varz = ['z','z2','y3'] #z
    rx = random.choice(varx)
    ry = random.choice(vary)
    #rz = random.choice(varz)
    print(coeff)
    sign = []
    for i in coeff[1:6:2]:
        if i < 0:
            sign.append('')
        else:
            sign.append('+')

    haddque = 'Add horizontally '+str(coeff[0])+rx+sign[0]+str(coeff[1])+ry+','+str(coeff[2])+rx+sign[1]+str(coeff[3])+ry+','+str(coeff[4])+rx+sign[2]+str(coeff[5])+ry
    print(haddque)
    x_like = coeff[0:5:2]
    x_sum = sum(x_like)
    y_like = coeff[1:6:2]
    y_sum = sum(y_like)
    answer = {'que':haddque,'varx':rx,'vary':ry,'coeff':coeff,'x_like':x_like,'y_like':y_like,'x_sum':x_sum,'y_sum':y_sum}
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : '+str(x_sum)+rx+'+'+str(y_sum)+ry+'.'
    hints = {'h1':h1,'h2':h2,'h3':h3}    
    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2/total)*100,2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('algebra_add.html',answer=answer, hints = hints, scoredict=scoredict)


app.secret_key = 'super secret key'
app.run(debug=True)
