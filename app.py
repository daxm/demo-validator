from flask import Flask, render_template, request, url_for
import random
from utilities import dmvpn_utilities, guacamole_utilities

app = Flask(__name__)
title = "Demo Preparation"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.htm', title=title)
    if request.method == 'POST':
        # Set up the "random" password
        cco_username = request.form.get("cconame")
        postfix = random.randint(100, 999)
        password = "{}-{}".format(cco_username, postfix)

        # Go update NHRP and guacamole passwords
        debug_log = [dmvpn_utilities.set_password(password=password),
                     guacamole_utilities.set_password(password=password)]
        return render_template('set_password.htm', password=password, debug_log=debug_log, title=title)


@app.route("/<path:path>")
def catchall(path):
    return render_template("NoneShallPass.htm", path=path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=1)
