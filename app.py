from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def date_time_calculator():
    result = None
    calculator_type = None

    if request.method == "POST":
        calculator_type = request.form.get("calculator_type")
        
        try:
            if calculator_type == "date_difference":
                date1 = datetime.strptime(request.form.get("date1"), "%Y-%m-%d")
                date2 = datetime.strptime(request.form.get("date2"), "%Y-%m-%d")
                difference = abs((date2 - date1).days)
                result = f"Total Days Difference: {difference} days"

            elif calculator_type == "add_days":
                base_date = datetime.strptime(request.form.get("base_date"), "%Y-%m-%d")
                days_to_add = int(request.form.get("days_to_add"))
                new_date = base_date + timedelta(days=days_to_add)
                result = f"New Date: {new_date.strftime('%Y-%m-%d')}"

            elif calculator_type == "subtract_days":
                base_date = datetime.strptime(request.form.get("base_date"), "%Y-%m-%d")
                days_to_subtract = int(request.form.get("days_to_subtract"))
                new_date = base_date - timedelta(days=days_to_subtract)
                result = f"New Date: {new_date.strftime('%Y-%m-%d')}"

            elif calculator_type == "time_difference":
                time1 = datetime.strptime(request.form.get("time1"), "%H:%M")
                time2 = datetime.strptime(request.form.get("time2"), "%H:%M")
                time_diff = abs((time2 - time1).seconds)
                hours, remainder = divmod(time_diff, 3600)
                minutes = remainder // 60
                result = f"Time Difference: {hours} hours, {minutes} minutes"

        except Exception as e:
            result = f"Error: {e}"

    return render_template(".templates\index.html", result=result, calculator_type=calculator_type)

if __name__ == "__main__":
    app.run(debug=True)
