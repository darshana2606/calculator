from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("calculator.html")
@app.route('/submit',methods=['POST'])
def submit():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
            else:
                result = 'Invalid Operation'
        except ValueError:
            result = 'Invalid Input'

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(port=5001, debug=True)