import json
from flask import Flask
from datasource import PostgreSQL

CONFIG_FILENAME = "resources/config.json"

# server
host = None
port = None

# application context
app = None
debug = None

# datasource for PostgreSQL
datasource = None

with open(CONFIG_FILENAME) as f:
    config = json.load(f)

    host = config["server"]["host"]
    port = config["server"]["port"]

    app = Flask(config["application"]["name"])
    debug = True if config["application"].get("debug") == "True" else False

    datasource = PostgreSQL(
        hostname=config["datasource"]["hostname"],
        port=config["datasource"]["port"],
        dbname=config["datasource"]["dbname"],
        user=config["datasource"]["user"],
        password=config["datasource"]["password"]
    )
