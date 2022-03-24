import sqlite3
from flask import *
import pandas as pd
class ops:
    df = pd.read_csv('datasets/crop1.csv')
    df1=pd.read_csv('datasets/crops.csv')
    def byState(self,s):
        return self.df[self.df['State']==s].to_html()

    def byCrop(self,c):
        return self.df[self.df['Crop']==c].to_html()

    def bySeason(self,sn):
        return self.df[self.df['Season']==sn].to_html()

    def bySoil(self,st):
        return self.df1[self.df1['SOIL TYPE1']==st].to_html()

    def bestinstate(self,s):
        dfd=self.df[self.df['State']==s]
        #adding pheromone value
        dfd['ph']=1/(dfd['Cost of Cultivation']*dfd['Cost of Production'])
        #calculating function
        dfd['f']=dfd['Yield']*dfd['ph']
        tmax=max(dfd['f'])
        name = dfd[dfd['f'] == tmax]
        return name.to_html()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bestcrop')
def bestcrop():
    return render_template('bestcrop.html')

@app.route('/bestcropinstate',methods=["POST", "GET"])
def bestcropinstate():
    state=request.form['field1']
    s=ops()
    t=s.bestinstate(state)
    text_file = open("templates/bestcrop1.html", "w")
    text_file.write(t)
    text_file.close()
    return render_template('bestcrop1.html')


@app.route('/soiltesting')
def testing():
    return render_template('soiltesting.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/contactus')
def contact():
    return render_template('contactus.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/showstates',methods=["POST", "GET"])
def showstates():
    state=request.form['field1']
    s=ops()
    t=s.byState(state)
    text_file = open("templates/cropbystate.html", "w")
    text_file.write(t)
    text_file.close()
    return render_template('cropbystate.html')

@app.route('/showcrops',methods=["POST", "GET"])
def showcrops():
    state=request.form['field1']
    s=ops()
    t=s.byCrop(state)
    text_file = open("templates/cropbycrop.html", "w")
    text_file.write(t)
    text_file.close()
    return render_template('cropbycrop.html')

@app.route('/showseason',methods=["POST", "GET"])
def showseason():
    state=request.form['field1']
    s=ops()
    t=s.bySeason(state)
    text_file = open("templates/cropbyseason.html", "w")
    text_file.write(t)
    text_file.close()
    return render_template('cropbyseason.html')

@app.route('/showsoil',methods=["POST", "GET"])
def showsoil():
    state=request.form['field1']
    s=ops()
    t=s.bySoil(state)
    text_file = open("templates/cropbysoil.html", "w")
    text_file.write(t)
    text_file.close()
    return render_template('cropbysoil.html')

@app.route('/season')
def season():
    return render_template('season.html')

@app.route('/soil')
def soil():
    return render_template('soil.html')

@app.route('/crop1')
def crop1():
    return render_template('crop1.html')

@app.route('/state')
def state():
    return render_template('state.html')

@app.route('/arhar')
def arhar():
    return render_template('arhar.html')

@app.route('/coffee')
def coffee():
    return render_template('coffee.html')

@app.route('/cotton')
def cotton():
    return render_template('cotton.html')

@app.route('/turmeric')
def turmeric():
    return render_template('turmeric.html')

@app.route('/gram')
def gram():
    return render_template('gram.html')

@app.route('/mustard-rapeseed')
def mustard_rapeseed():
    return render_template('mustard-rapeseed.html')

@app.route('/maize')
def maize():
    return render_template('maize.html')

@app.route('/potato')
def potato():
    return render_template('potato.html')

@app.route('/onion')
def onion():
    return render_template('onion.html')

@app.route("/help", methods=["POST", "GET"])
def help():
    msg = "msg"
    if request.method=="POST":
        try:
            name = request.form["field1"]
            contact = request.form["field2"]
            address = request.form["field3"]
            state = request.form["field4"]
            pincode = request.form["field5"]
            areasize = request.form["field6"]
            with sqlite3.connect("hackathon22.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into HelpDetails  values (?,?,?,?,?,?)", (name, contact, address,state,pincode,areasize))
                con.commit()
                msg = "Help Details Received successfully you will be contacted soon"
        except:
            con.rollback()
            msg = "We can not add the details to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/soil1", methods=["POST", "GET"])
def soilsuccess():
    msg = "msg"
    if request.method=="POST":
        try:
            name = request.form["field1"]
            contact = request.form["field2"]
            address = request.form["field3"]
            state = request.form["field4"]
            pincode = request.form["field5"]
            with sqlite3.connect("hackathon22.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into SoilTest  values (?,?,?,?,?)", (name, contact, address,state,pincode))
                con.commit()
                msg = "Help Details Received successfully you will be contacted soon"
        except:
            con.rollback()
            msg = "We can not add the details to the list"
        finally:
            return render_template("soilsuccess.html", msg=msg)
            con.close()


@app.route('/soil1')
def soil1():
    return render_template('soilsuccess.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
