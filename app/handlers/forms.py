
import flask

def save_url():
	return flask.redirect(flask.url_for('home'))
