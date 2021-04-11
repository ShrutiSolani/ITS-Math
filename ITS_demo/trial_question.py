from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask.ext.session imDortAnacsida
from fractions import Fraction
import random
import os
import math


app = Flask(__name__)


values = [Fraction('25/8'), Fraction('17/4'), Fraction('38/7'), Fraction('29/3'), Fraction('44/5')]
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')

qtscnt1=0     #fraction
scorecnt1=0   #fraction
qtscnt2 = 0   #algebra
scorecnt2 = 0 #algebra
##########################################3
@app.route("/")
def index():
    return render_template('index.html')

###########################################
@app.route("/login")
def login():
    return render_template('login.html')

##############################################
@app.route("/mixed-fraction1", methods=['POST'])
def q1():
    if request.method == 'POST':
        global qtscnt1,scorecnt1
        num = random.randint(1, 100)
        den = random.randint(1, 25)
        while num < den:
            num = random.randint(1, 100)
        que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
        quo = num // den
        rem = num % den
        box_ans = [quo, rem, quo, rem, den]
        answer = {'que':que,'ans':box_ans}
        # answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
        hint1 = 'Try dividing numerator by denominator'
        hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
        hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
        hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
        total = qtscnt1 * 25
        scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'pct': 0}
        return render_template('short_display.html', answer=answer, hints=hints, scoredict=scoredict)
    else:
        return render_template('login.html')

#################################################33
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
    answer = {'que':que, 'ans':box_ans}
    labels = ['Quotient', 'Remainder', 'Numerator', 'Whole Number', 'Denominator']
    labels = {'labels': labels}
    #answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    hint1 = 'Try dividing numerator by denominator'
    hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
    hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
    hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
    total = qtscnt1 * 25
    try:
        tcp = round((scorecnt1/total)*100, 2)
        print(tcp)
    except:
        tcp = 0
    scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'tcp': tcp}
    return render_template('short_display.html', answer=answer, hints=hints, scoredict=scoredict, labels = labels)

#################################################################
@app.route('/score/<tid>/<counter>/<feedback>', methods=['POST'])
def score(counter, feedback, tid):
    if request.method == 'POST':
        print('tid : ',tid)
        if tid == 1:
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


###############################################################
@app.route("/compare")
def compare():
    num1=random.randint(1,100)
    den1=random.randint(2,100)
    num2 = random.randint(1, 100)
    den2 = random.randint(2, 100)
    f1= Fraction(num1,den1)
    f2= Fraction(num2,den2)

    # que={'f1':f1,'f2':f2}
    def LCM(a, b):
        return abs(a * b) // math.gcd(a, b)
    que = "Compare "+str(f1)+" and "+str(f2)+" . "
    lcm=LCM(f1.denominator,f2.denominator)
    print(lcm)
    eqfrac1=lcm//den1
    eqfrac2=lcm//den2
    num1=num1*eqfrac1
    den1=den1*eqfrac1
    num2 = num2 * eqfrac2
    den2 = den2 * eqfrac2
    fract1=Fraction(num1,den1)
    fract2=Fraction(num2,den2)
  
    if(fract1>fract2):
        ans="1"
    elif fract2>fract1:
        ans="2"
    else:
        ans="3"
    print(que)
    print(eqfrac1,eqfrac2,fract1,fract2)
    answer={'que':que,'lcm':lcm,'num1':num1,'den1':den1,'num2':num2,'den2':den2,'ans':ans , 'f1':f1,'f2':f2}
    print(answer)
    h1="LCM of both denominators if Fraction are unlike."
    h2="EXAMPLE : LCM of 5 and 6 is 30."
    h3="Equivalent Fraction of :",str(f1)," => ",num1,"/",den1," and ",str(f2)," => ",num2,"/",den2
    h4=" 4/5 < 5/6."
    hints={'h1':h1,'h2':h2,'h3':h3,'h4':h4}
    total = qtscnt1 * 25
    try:
        tcp = round((scorecnt1/total)*100, 2)
        print(tcp)
    except:
        tcp = 0
    scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'tcp': tcp}
    print(hints)
    print(ans)
    return render_template('fracompare.html', answer=answer, hints=hints, scoredict= scoredict)


############################################
@app.route("/algebra-add")
def horizontal_add():
    coeff = random.sample(range(-50,50),6) #6 coefficient
    varx = ['x','x\u00b2','x\u00b3'] #x3
    vary = ['y','y\u00b2','y\u00b3'] #y2
    #svarz = ['z','z2','y3'] #z
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

############################################
@app.route('/vertical_sub')
def vertical_sub():
    coeff = random.sample(range(-50, 50), 6)  # 6 coefficient
    varx = ['x', 'x\u00b2', 'x\u00b3']  # x3
    vary = ['y', 'y\u00b2', 'y\u00b3']  # y2
    varz = ['z', 'z\u00b2', 'z\u00b3']  # z
    rx = random.choice(varx)
    ry = random.choice(vary)
    rz = random.choice(varz)
    sign_1 = []
    for i in coeff[1:3]:
        if i < 0:
            sign_1.append('')
        else:
            sign_1.append('+')
    sign_2=[]
    for j in coeff[4:7]:
        if(j<0):
            sign_2.append("")
        else:
            sign_2.append('+')
    haddque = 'Sub Vertically ' + str(coeff[0])+rx+str(sign_1[0])+str(coeff[1])+ry+str(sign_1[1])+str(coeff[2])+rz+' , '+str(coeff[3])+rx+str(sign_2[0])+str(coeff[4])+ry+str(sign_2[1])+str(coeff[5])+rz+' . '
    print(haddque)
    x_diff = coeff[0] - coeff[3]
    y_diff = coeff[1] - coeff[4]
    z_diff = coeff[2] - coeff[5]
    answer = {'que': haddque, 'varx': rx, 'vary': ry,'varz':rz,'coeff': coeff,'x_diff': x_diff, 'y_diff': y_diff,'z_diff':z_diff}
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(x_diff) + rx + '+' + str(y_diff) + ry + ' + ' + str(z_diff) + rz + '.'
    hints={'h1':h1,'h2':h2,'h3':h3}
    # print(x_sum,y_sum,z_sum)
    print(hints)

    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2 / total) * 100, 2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('vertical_sub.html', answer=answer, hints=hints, scoredict=scoredict)

@app.route('/simplest-form')
def simplest_form():
    num = random.randint(1,50)
    den = random.randint(2,50)
    que = "Find simplest form of fraction "+ str(num)+"/"+ str(den)
    simple = Fraction(num, den)
    answer = {'que': que, 'num_ans': simple.numerator, 'den_ans': simple.denominator}
    print(answer)
    scoredict={}
    hints={}
    return render_template('simplestForm.html',answer=answer,hints=hints,scoredict=scoredict)

    return render_template('simplest_form.html', answer=answer, hints=hints, scoredict=scoredict)


#simplest_form()

#mixed to normal form
@app.route('/normal-form')
def mixed_to_normal():
    num = random.randint(1,50)
    den = random.randint(2,50)
    whole = random.randint(2,20)
    que = "Convert "+str(whole)+" "+str(num)+"/"+str(den)+" to normal form and find simplest form"
    num_ans = (den*whole)+num
    frac = Fraction(num_ans,den)
    answer = {'que':que, 'num_ans':frac.numerator, 'den_ans':frac.denominator,'den':den,'num':num_ans}
    # print(answer)
    # scoredict = 0
    # hints = {}
    # return render_template('normalForm.html', answer=answer, hints=hints, scoredict=scoredict)
    den_ans=den
    whole_ans=whole
    num1=num
    frac = Fraction(num_ans,den_ans)
    answer = {'que':que, 'num_ans':num_ans, 'den_ans':den_ans,'whole_ans':whole_ans,'num1':num1}
    print(answer)
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(num_ans)+ '/' + str(den)
    hints = {'h1': h1, 'h2': h2, 'h3': h3}
    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2 / total) * 100, 2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('normal-form.html', answer=answer, hints=hints, scoredict=scoredict)

#mixed_to_normal()


app.secret_key = 'super secret key'
app.run(debug=True)
