@app.route("/",methods=['POST', 'GET")
def dashboard():
return render template ("home.html")

fapp.route('/login', methods=['GET', 'POST'])
def login():
msg ="
if request.method == 'POST'
USERNAME = request. form['usernane']
PASSWORD = request. form['password']
sql = "SELECT * FROM USER] WHERE USERNAME=? AND PASSWORD=2"
stmt = ibm db.prepare (conn, sql)
ibm_db.bind_param(stmt, 1, USERNAME)
ibm_db.bind_param(stmt, 2, PASSWORD)
ibm_db. execute (stmt)
account = ibm_db. fetch_assoc (stmt)

print (account)

if account:
session["USERNAME"] = account ["USERNAME"]
session['USERID'] = account['USERID']

msg = 'Logged in successfully !'
return redirect (url for('pets'))
SEY
msg = 'Incorrect username / password !'
return render_template ('newlogin.htnl', msg=nsg)

@app.route ("/admin-login", methods=["GET", "POST"])
def admin_login()
if request.method == "EOST":

# session.clear()

USERNAME = request. form.get ("username")

PASSWORD = request. form.get("password™)

sql = "SELECT* FROM USER] WHERE USERNAME=? AND PASSWORD=2"

stmt = ibm_db.prepare (conn, sql)

ibm_db.bind_param(stmt, 1, USERNAME)

ibm_db.bind_param(stmt, 2, PASSWORD)

ibm db. execute (stmt)

result = ibm db. fetch assoc (stmt)

print (result)

if resul
session['Loggedin']=True
session["USERID"]=result['USERID']
Userid=result['USERNAME']
session’ USERNAME ']-result [USERNAME]
msg="logged in successfully
return redirect (url_for('home'))

els

msg="Incorrect username/password!"
return render template ('admin_login.html', msg-msq)
return render template ('admin login.html')

@app.route('/register’, method:
aes register (x

‘GET, 'POST'l)

msg
if request.method = 'poST
USERNAME = request. form("usernane"]
PASSWORD = request. form "passuozd™]
EMATL = request. form( "ena: l"]
ql = "SELECT FROM USER] WHERE USERNAME= ? AND PASSWORD=2"
stmt = ibm db.prepare (conn, sal)

ibm_db.bind param (stmt, 1, USERNAME)
ibm db bind param (stat, 2, PASSWORD)
Som ab. execnte (stmt)

account = ibm db. fetch assoc (stat)
Print (account)

Lt account

msg - ‘Account already exists
lif not re.mateh(s’[~@1+[~01+\.[*€]+", BMATL):

msg - "invalid email address |
lif not re.mateh(s[A-2a-—20-5]+, USERNAME:

msg = ‘Username must contain only characters and numbers !'
lif not USERNAME or nol PASSWORD ox nol EMAIL:

msg = ‘Please Fill cur the form !'
else:

sq12 = "SELECT count (¥) FROM USERL™

stmt2 = ibm db.prepare (conn, sq12)
ibm_db_execure (stmc2)

length = ibm db. fetch assoc(stmt2)

print (Length)

Sql = "INSERT INTO USERL VALUES(?,2,7,2,7)"
Semt = ibm db.prepare (conn, sal)
ibm_db.bind_param (stmt, 1, USERNAME)

ibm db bind param (stmt, 2, EMAIL)

ibm_db_ bind param (stmt, 3, PASSWORD)

ibm db bind param (stmt, 4, lengthl'l'1+l)
ibm db_bind param (stmt, 5, ROLE)

ibmoab_ execute (stme)

app. route ("/ownersignup”, methods=["GET", "FOSTT])
ef ownersigmp():
pe
if request.method == "2057":

# session.clear()

USERNAME = request. form. get ("usernane")

EMAIL = request. form. get ("enail")

PASSWORD = request. form.get ("password")

ROLE=1

# password = request. form.get ("password")

sql ="SELECT + FROM USER] WHERE USERNAME=? AND EASSWORD=2"

stat = ibn db.prepare (conn, sql)

ibm_db.bind param(stnt, 1, USERNAME)

ibm db.bind param(stat, 2, PASSHORD)

ibm db. execute (stat)

data = ibn db. fetch assoc(stmt)

if data:
return render_template("ounersignup.hinl”, message="Usernane already exists!")

else:
sql2 = "SELECT count (¥) FROM USERL"
stat2 = ibm db. prepare (com, sql2)
ibm_db.execute (stut2)
length = ibm db. fetch assoc (stmt2)
print (length)
sql = "INSERT INTO USERL VALUES(2,2,2,2,2)"
stat = ibn db. prepare (com, sql)
ibm db.bind paran(stut, 1, USERNAME)
ibn_db.bind param(stnt, 2, EMAIL)
ibm db.bind param(stnt, 3, PASSWORD)
ibm db. bind param(stat, 4, length['l']+1)
ibm db.bind param (stmt, 5, ROLE)


