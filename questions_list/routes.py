from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app


choice_bp = Blueprint('choice_bp', __name__, template_folder='templates', static_folder='static')


@choice_bp.route('/fraction-intermediate')
def fraction_intermediate():
    full = {'f1': {'q1': 'Expressed as Mixed Fraction', 'h1': 'Mixed Fraction', 'link': '/mixed-fraction'},
            'f2': {'q1': 'Compare Two Fraction', 'h1': 'Compare', 'link': '/compare'},
            'f3': {'q1': 'Convert Mixed to Normal Form', 'h1': 'Normal Form', 'link': '/normal-form'},
            'f4': {'q1': 'Divide Fraction by Whole Number', 'h1': 'Fraction Division', 'link': '/divide_with_whole'},
            'f5': {'q1': 'Add or Subtract Two fractions', 'h1': 'Fraction Operation', 'link': '/unlike-add'}}
    return render_template('easy_qts_choice.html', topic=full, unit='UNIT: Fractions')


@choice_bp.route('/algebra-intermediate')
def algebra_intermediate():
    full = {'f1': {'q1': 'Addition of Algebraic Expressions', 'h1': 'Horizontal Addition', 'link': '/algebra-add'},
            'f2': {'q1': 'Subtraction of Algebraic Expressions', 'h1': 'Vertical Subtraction', 'link': '/vertical_sub'}}
    return render_template('easy_qts_choice.html', topic=full, unit='UNIT: Algebra')


@choice_bp.route('/fraction-easy')
def fraction_easy():
    full = {'f1': {'q1': 'Convert to Simplest Form', 'h1': 'Simplest Form', 'link': '/simplest-form'},
            'f2': {'q1': 'Find Quotient and Remainder', 'h1': 'Fraction Division', 'link': '/division'},
            'f3': {'q1': 'Add / Subtract like Fraction', 'h1': 'Fraction Operation', 'link': '/add-fractions'},
            'f4': {'q1': 'Multiply Fraction by Whole Number', 'h1': 'Fraction Multiplication',
                   'link': '/multiply-with-whole'}}
    return render_template('easy_qts_choice.html', topic=full, unit='UNIT: fractions')


@choice_bp.route('/algebra-easy')
def algebra_easy():
    full = {'f1': {'q1': 'Find Coefficient of Terms', 'h1': 'Find Coefficient', 'link': '/coefficient'},
            'f2': {'q1': 'Find value of Variable', 'h1': 'Find value', 'link': '/value-of-expression'},
            'f3': {'q1': 'Classify into Monomial, Bionomial, Trinomial ', 'h1': 'Classification', 'link': '/monomial'},
            'f4': {'q1': 'Identify Like or Unlike', 'h1': 'Identification', 'link': '/like-unlike'}}
    return render_template('easy_qts_choice.html', topic=full, unit='UNIT: Algebra')
