import argparse
from flask import Flask
from web.routes import routes

from settings.data_config import Config


def start_server():
    app = Flask(__name__, static_url_path='/ghost-rider', static_folder='static')
    app.register_blueprint(routes, url_prefix='/ghost-rider')
    app.run(debug=True, host=Config.get_instance().APP_SERVER.HOST, port=Config.get_instance().APP_SERVER.PORT)


def main(config_file_path):
    Config(config_file_path)
    start_server()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ghost-rider management system script")
    parser.add_argument("-config", dest="config_file_path", required=True,
                        help="Enter location of config file")
    args = parser.parse_args()
    main(args.config_file_path)
