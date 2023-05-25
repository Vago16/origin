from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    """Generate form to ask for words"""
    prompts = story.prompts
    return render_template("question.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Shows generated story"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)