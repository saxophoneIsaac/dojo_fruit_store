from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print('quantities of strawberries')
    print(request.form.get('strawberry'))
    total_fruits = int(request.form.get('strawberry')) + int(request.form.get('raspberry')) + int(request.form.get('apple'))
    print(total_fruits)
    return render_template("checkout.html", quantity_of_strawberries = request.form.get('strawberry'), quantity_of_raspberries = request.form.get('raspberry'), quantity_of_apples = request.form.get('apple'), first_name = request.form.get('first_name'), last_name = request.form.get('last_name'), count = total_fruits)
    # return redirect("checkout.html", quantity_of_strawberries = request.form.get('strawberry'), quantity_of_raspberries = request.form.get('raspberry'), quantity_of_apples = request.form.get('apple'), first_name = request.form.get('first_name'), last_name = request.form.get('last_name'))

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)