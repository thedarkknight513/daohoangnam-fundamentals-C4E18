from flask import Flask, render_template
app = Flask(__name__)

# without render_template
@app.route('/notemplate/bmi/<int:weight>/<int:height_in_m>')
def bmi_calculate(weight, height_in_m):
    bmi_figure = int(float(weight) / float(((height_in_m)/100) ** 2))
    if bmi_figure < 16:
        health_status = "Severely underweight"
    elif bmi_figure >= 16 and bmi_figure < 18.5:
        health_status = "Underweight"
    elif bmi_figure >= 18.5 and bmi_figure < 25:
        health_status = "Normal"
    elif bmi_figure >= 25 and bmi_figure < 30:
        health_status = "Overweight"
    elif bmi_figure >= 30:
        health_status = "Obese"

    string_1 = "Hi your BMI is {0} and you are {1}".format(bmi_figure,health_status)
    return string_1

# with render_template
@app.route('/withtemplate/bmi/<int:weight2>/<int:height_in_m2>')
def bmi_calculate2(weight2,height_in_m2):
    bmi_figure2 = int(float(weight2) / float(((height_in_m2)/100) ** 2))
    if bmi_figure2 < 16:
        health_status2 = "Severely underweight"
    elif bmi_figure2 >= 16 and bmi_figure2 < 18.5:
        health_status2 = "Underweight"
    elif bmi_figure2 >= 18.5 and bmi_figure2 < 25:
        health_status2 = "Normal"
    elif bmi_figure2 >= 25 and bmi_figure2 < 30:
        health_status2 = "Overweight"
    elif bmi_figure2 >= 30:
        health_status2 = "Obese"

    string_2 = "Hi your BMI is {0} and you are {1}".format(bmi_figure2,health_status2)
    return render_template("bmi.html", string_2 = string_2)


if __name__ == '__main__':
  app.run(debug=True)
 