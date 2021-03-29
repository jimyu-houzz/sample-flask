from flask import Flask, render_template
# render_template is used to connect to HTML file

app = Flask(__name__)

@app.route("/")
def index():
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    count += 1

    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # run the html file, and pass variable "count"
    # render_template looks for the html files under the template directory
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()