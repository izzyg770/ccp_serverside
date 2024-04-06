"""CCP package initializer."""
import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name

app.config.from_object('ccp.config')

app.config.from_envvar('CCP_SETTINGS', silent=True)

import ccp.views  
import ccp.model  