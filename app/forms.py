from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class SoilDataForm(FlaskForm):
    nitrogen = FloatField('Nitrogen (N)', validators=[DataRequired(), NumberRange(min=0)])
    phosphorus = FloatField('Phosphorus (P)', validators=[DataRequired(), NumberRange(min=0)])
    potassium = FloatField('Potassium (K)', validators=[DataRequired(), NumberRange(min=0)])
    temperature = FloatField('Temperature (°C)', validators=[DataRequired()])
    humidity = FloatField('Humidity (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    ph = FloatField('pH', validators=[DataRequired()])
    rainfall = FloatField('Rainfall (mm)', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Get Crop Recommendation')
