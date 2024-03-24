from flask import render_template, request
from app import app
from app.forms import SoilDataForm
from app.recommender import predict_crops


@app.route("/", methods=["GET", "POST"])
def index():
    form = SoilDataForm()
    if request.method == "POST" and form.validate_on_submit():
        soil_data = [
            form.nitrogen.data,
            form.phosphorus.data,
            form.potassium.data,
            form.temperature.data,
            form.humidity.data,
            form.ph.data,
            form.rainfall.data,
        ]
        recommended_crops = predict_crops(soil_data)
        return render_template(
            "recommendation.html", recommended_crops=recommended_crops
        )
    return render_template("index.html", form=form)
