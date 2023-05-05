# Microblog Tutorial

Following along in the steps of the Flask Mega Tutorial

## Note

- Also learning git at the same time which might not be a good decision, we'll see..
- The backslash character forces a newline in markdown

## Info

- {{ varName }} will dynamically add data from passed paramters
- {% ... &} can contain nsna run pthon logic
- Use render_template() from flask to improve readability and seperate html and python
- Add a base.html to hold some common assets and use the {% block content %}{% endblock %} to indicate where derived templates can insert themselves

- Input is through WTForms, each form is a class where class variables represent the fields. Use wtforms fields and wtforms.validators
