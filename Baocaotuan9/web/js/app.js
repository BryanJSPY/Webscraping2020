eel.expose(loginFacebook);
function loginFacebook() {
  let user = document.getElementById("username").value;
  let pass = document.getElementById("password").value;
  let key = document.getElementById("keyword").value;
  eel.login_fb_py(user, pass, key);
}
