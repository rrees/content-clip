import flask

def front_page():
	return flask.render_template('index.html')

def home_page():
	return flask.render_template('home.html')

def saved_url_page():
	return flask.render_template('url.html')