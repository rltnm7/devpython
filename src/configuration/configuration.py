import os
import json
from flask import Flask

profile = os.getenv("PYTHON_PROFILE", "default")

if profile == "test":
    from tests.datasource.mock_datasource import MockPostgreSQL as PostgreSQL
else:
    # ユニットテストでmockを挿し込む用の分岐のため、挿し込まない分岐はカバレッジが通せいない
    from datasource import PostgreSQL

# コンフィグファイル名
CONFIG_FILENAME = "resources/config.json"
if profile == "test":
    CONFIG_FILENAME = "tests/resources/config.json"

# 接続許可IP
host = None

# server port
port = None

# application context
app = None

# debug mode flag
debug = None

# datasource for PostgreSQL
datasource = None

# コンフィグファイルから設定情報のインポート
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
