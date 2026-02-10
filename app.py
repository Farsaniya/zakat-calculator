from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    zakat_amount = None
    wealth_value = None
    error = None

    if request.method == "POST":
        try:
            # Get the wealth amount typed by the user
            wealth_value = request.form.get("wealth", "").strip()
            if wealth_value == "":
                error = "Please enter your total wealth."
            else:
                wealth = float(wealth_value)
                if wealth < 0:
                    error = "Wealth cannot be negative."
                else:
                    # Basic Zakat: 2.5% of eligible wealth
                    zakat_amount = round(wealth * 0.025, 2)
        except ValueError:
            error = "Please enter a valid number (e.g., 100000 or 100000.50)."

    return render_template("index.html",
                           zakat=zakat_amount,
                           wealth=wealth_value,
                           error=error)

if __name__ == "__main__":
    # debug=True is helpful while developing
    app.run(debug=True)