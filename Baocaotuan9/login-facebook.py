from __future__ import print_function
import eel
from main import loginFB


eel.init('web')


@eel.expose
def login_fb_py(user, pwd, key):
    loginFB(user, pwd, key)



eel.start("login.html", size=(450, 600))
