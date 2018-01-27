from flask import Flask
from facebook_robot.config import configure_app
from facebook_robot.main.apibot.controllers import apibot
from facebook_robot.main.admin.controllers import admin
from facebook_robot.data.models import db
from facebook_robot.cache import config_cache


app = Flask(__name__ ,
                      template_folder='templates' # specifies the main template folder for the application
            )
configure_app(app)
config_cache(app)
db.init_app(app)

app.register_blueprint(apibot, url_prefix='/apibot')
app.register_blueprint(admin, url_prefix='/admin')