from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data/Table_Input.csv")

    value_map = dict(zip(df["Index #"], df["Value"]))

    alpha = int(value_map["A5"]) + int(value_map["A20"])
    beta = int(value_map["A15"]) / int(value_map["A7"])
    charlie = int(value_map["A13"]) * int(value_map["A12"])

    table2 = {
        "Alpha": alpha,
        "Beta": beta,
        "Charlie": charlie
    }

    #(Display in the exact same format as CSV)
    table1 = df.to_html(index=False)

    return render_template("index.html", table1=table1, table2=table2)

if __name__ == "__main__":
    app.run(debug=True)