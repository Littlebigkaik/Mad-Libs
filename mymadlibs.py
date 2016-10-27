from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("mad.html")

# route to display a simple web page
@app.route('/pages/chinese/')
def chinese():
    return render_template("chinese.html")

@app.route('/pages/chinesestory/', methods=['POST'])
def chinese_story():
    adj1 = request.form.get("adj1")
    adj2 = request.form.get("adj2")
    adj3 = request.form.get("adj3")
    adj4 = request.form.get("adj4")
    adj5 = request.form.get("adj5")
    noun1 = request.form.get("noun1")
    noun2 = request.form.get("noun2")
    noun3 = request.form.get("noun3")
    noun4 = request.form.get("noun4")
    celeb = request.form.get("celeb")
    food1 = request.form.get("food1")
    food2 = request.form.get("food2")
    food3 = request.form.get("food3")


    return render_template("chinesestory.html", adj1=adj1, adj2=adj2, celeb=celeb, adj3=adj3, noun1=noun1, adj4=adj4, adj5=adj5, noun2=noun2, noun3=noun3, food1=food1, food2=food2, noun4=noun4, food3=food3)
@app.route('/pages/computer/')
def computer():
    return render_template("computer.html")

@app.route('/pages/computerstory/', methods = ['POST'])
def computer_story():
    adj = request.form.get("adj")
    adverb = request.form.get("adverb")
    noun1 = request.form.get("noun1")
    noun2 = request.form.get("noun2")
    noun3 = request.form.get("noun3")
    noun4 = request.form.get("noun4")
    noun5 = request.form.get("noun5")
    noun6 = request.form.get("noun6")
    p_noun1 = request.form.get("p_noun1")
    p_noun2 = request.form.get("p_noun2")
    p_noun3 = request.form.get("p_noun3")
    p_noun4 = request.form.get("p_noun4")
    p_noun5 = request.form.get("p_noun5")
    verb1 = request.form.get("verb1")
    verb2 = request.form.get("verb2")
    m_word = request.form.get("m_word")

    return render_template("computerstory.html", adj=adj, adverb=adverb, noun1=noun1, noun2=noun2, noun3=noun3, noun4=noun4, noun5=noun5, noun6=noun6, p_noun1=p_noun1, p_noun2=p_noun2, p_noun3=p_noun3, p_noun4=p_noun4, p_noun5=p_noun5, verb1=verb1, verb2=verb2, m_word=m_word)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
