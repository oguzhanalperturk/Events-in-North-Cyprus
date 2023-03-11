from flask import *
import sqlite3


app = Flask(__name__)
app.secret_key = "it should be secret"


@app.route('/')
@app.route("/home_page")
def home_page():

    if 'search_result_list' in session:

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM city")
        cities = c.fetchall()

        conn.close()

        search_result_list = session["search_result_list"]
        session.pop("search_result_list", None)

        return render_template("home.html", events=search_result_list, cities=cities)

    elif 'username' in session:

        home_page_data = []

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM city")
        cities = c.fetchall()

        for city in cities:

            c.execute(
                "SELECT * FROM event WHERE event_city_id=? AND isActive=1 ORDER BY date ASC, time ASC LIMIT 5", (city[0],))
            events = c.fetchall()
            home_page_data.append(events)

        conn.close()

        return render_template("home.html", username=session['username'], events=home_page_data, cities=cities)
    else:
        home_page_data = []

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM city")
        cities = c.fetchall()

        for city in cities:

            c.execute(
                "SELECT * FROM event WHERE event_city_id=? AND isActive=1 ORDER BY date ASC, time ASC LIMIT 5", (city[0],))
            events = c.fetchall()
            home_page_data.append(events)

        conn.close()

        return render_template("home.html", events=home_page_data, cities=cities)


@app.route("/login", methods=["POST"])
def login():
    username = escape(request.form["username"])
    password = escape(request.form["password"])

    response = []

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE username=? AND password=?",
              (username, password))
    row = c.fetchone()
    conn.close()
    if row != None:
        session["username"] = username
        return redirect(url_for('home_page'))
    else:
        if (username == "" or password == ""):
            response.append("Please fill all the input boxes !!")
        else:
            response.append(
                "There is not any registered user have this username and password pair !!")
        session["message"] = response
        return redirect(url_for("message_page"))


@app.route("/message_page")
def message_page():
    message = session["message"]
    session["message"] = ""
    return render_template("message.html", message=message)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home_page"))


@app.route("/register_page")
def register_page():
    if 'error_message' in session:
        error_message = session["error_message"]
        session["error_message"] = []
        return render_template("register.html", error_message=error_message)
    else:
        return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    username = escape(request.form["username"])
    password = escape(request.form["password"])
    firstname = escape(request.form["firstname"])
    lastname = escape(request.form["lastname"])
    email = escape(request.form["email"])

    error_flag = 0
    response = []

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()

    if row != None:
        response.append(
            "This username is already taken. Please enter another username!")
        error_flag = 1

    if (error_flag == 0):

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("INSERT INTO user VALUES(?,?,?,?,?)",
                  (username, password, firstname, lastname, email))

        conn.commit()
        session["message"] = "Registration is successful !!"
        return redirect(url_for("message_page"))

    else:
        session["error_message"] = response
        return redirect(url_for("register_page"))


@app.route("/create_event_page")
def create_event_page():

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    row = ""
    cities = []
    c.execute("SELECT * FROM city")
    while (row != None):
        row = c.fetchone()
        if (row != None):
            cities.append(row)

    conn.close()

    return render_template("create_event.html", cities=cities)


@app.route("/create_event", methods=["POST"])
def create_event():

    eventName = escape(request.form["event_name"])
    description = escape(request.form["description"])
    location = escape(request.form["location"])
    city_id = escape(request.form["cities"])
    ticketPrice = escape(request.form["ticket_price"])
    date_time = escape(request.form["date_time"]).split("T")
    username = session["username"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO event(name,description,price,date,time,location,isActive,event_city_id,event_username) VALUES(?,?,?,?,?,?,?,?,?)",
              (eventName, description, ticketPrice, date_time[0], date_time[1], location, 1, city_id, username))

    conn.commit()

    session["message"] = "Event is created !!"

    return redirect(url_for("message_page"))


@app.route("/display_events_page")
def display_events_page():

    username = session["username"]
    cities = []

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM event WHERE event_username=? ORDER BY date ASC, time ASC", (username,))
    events = c.fetchall()

    for event in events:
        c.execute("SELECT * FROM city WHERE cityid=?", (event[8],))
        cities.append(c.fetchone()[1])

    conn.close()

    return render_template("display_events.html", events=events, cities=cities)


@app.route("/deactivate_event", methods=["GET"])
def deactivate_event():

    del_event_id = request.args.get('type')

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute(
        "UPDATE event SET isActive=0 WHERE eventid=?", (del_event_id,))

    conn.commit()

    return redirect(url_for("display_events_page"))


@app.route("/activate_event", methods=["GET"])
def activate_event():

    activate_id = request.args.get('activate')

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute(
        "UPDATE event SET isActive=1 WHERE eventid=?", (activate_id,))

    conn.commit()

    return redirect(url_for("display_events_page"))


@app.route("/event_details", methods=["GET"])
def event_details():

    eventid = request.args.get('eventid')

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM event WHERE eventid=?", (eventid,))
    event = c.fetchone()

    c.execute(
        "SELECT * FROM city WHERE cityid=?", (event[8],))
    city_name = c.fetchone()[1]

    conn.close()

    return render_template("event_details.html", event=event, city_name=city_name)


@app.route("/search_event", methods=["POST"])
def search_event():

    home_page_data = []

    search_str = escape(request.form["search_str"])

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM city")
    cities = c.fetchall()

    for city in cities:

        c.execute(
            "SELECT * FROM event WHERE event_city_id=? AND isActive=1 ORDER BY date ASC, time ASC", (city[0],))
        events = c.fetchall()
        home_page_data.append(events)

    conn.close()

    search_result_list = []

    for city in home_page_data:

        event_list = []

        for event in city:

            flag = 0

            if (search_str in event[1]):
                flag = 1
            elif (search_str in event[2]):
                flag = 1
            elif (search_str in event[6]):
                flag = 1

            if (flag == 1):
                event_list.append(event)

        search_result_list.append(event_list)

    session["search_result_list"] = search_result_list

    return redirect(url_for("home_page"))


if __name__ == "__main__":
    app.run(debug=True)
