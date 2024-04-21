
import pandas as pd
from flask import Flask, render_template, request

df = pd.read_csv("E:\search_engine_project\Search-Engine")


df['webseries'].fillna('', inplace=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            
            results = df[df['webseries'].str.contains(search_text, case=False, na=False)]['webseries'].tolist()
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)