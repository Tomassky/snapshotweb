from flask import Blueprint, render_template


web_index = Blueprint('web_index', __name__)

@web_index.route("/")
def index():
  return render_template('index_view.html')