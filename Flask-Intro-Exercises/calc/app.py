from flask import Flask, request
from operations import add, sub, mult, div

app = Flask (__name__)

@app.route("/add")
def do_add():
    """Add a and b param"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract a and b param"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route("/mult")
def do_mult():
    """Multipy a and b param"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b param"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


math_operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operator>")
def do_math(operator):
    """Do math using a and b param"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    reult = math_operators[operator](a, b)
    return str(result)