from flask import Flask, render_template, request

app = Flask(__name__)

def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

@app.route("/")
def home():
    return render_template("Input.html")

@app.route("/greet", methods=["POST"])
def greet():
    ip = safe_int(request.form.get("ip"))
    cp = safe_int(request.form.get("cp"))
    tp = safe_int(request.form.get("tp"))
    ap = safe_int(request.form.get("ap"))
    wc = safe_int(request.form.get("wc"))
    twh = safe_int(request.form.get("2h"))
    thh = safe_int(request.form.get("3h"))
    dp = safe_int(request.form.get("dp"))

    # Airfare cost
    a = (cp + tp) * 2600 + (ap * 30000)

    # Hotel cost
    h = (twh * 10000) + (thh * 15000)

    # Meal count: adults + half of kids/teens
    men = ap + (tp + cp) / 2

    # Meal cost
    me = 1500 * men if dp == 1 else 900 * men

    # Infant cost
    mi = ip * 2000

    # Base cost (added ₹3000 for service as you had in earlier examples)
    tc = a + h + me + mi + 3000

    # Taxes
    itc = tc * 0.05
    gst = (tc + itc) * 0.18
    gtc = tc + itc + gst

    return render_template(
    "Output.html",
    a=round(a, 2),
    h=round(h, 2),
    me=round(me, 2),
    mi=round(mi, 2),
    tc=round(tc, 2),
    itc=round(itc, 2),
    gst=round(gst, 2),
    gtc=round(gtc, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
