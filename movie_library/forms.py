from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
)

from wtforms.validators import (
    InputRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()],render_kw={"placeholder": "Enter your registered email"})
    password = PasswordField("Password", validators=[InputRequired()],render_kw={"placeholder": "Enter your password"})
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()],render_kw={"placeholder": "Enter email"})

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(
                min=4,
                max=20,
                message="Your password must be between 4 and 20 characters long.",
            ),
        ],
    render_kw={"placeholder": "Password must be between 4-20 characters long."})

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="This password did not match the one in the password field.",
            ),
        ],
    )

    submit = SubmitField("Register")


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1878, message="Please enter a year in the format YYYY."),
        ],
    )

    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link",render_kw={"placeholder": "Make sure to enter the embed link"})

    submit = SubmitField("Submit")