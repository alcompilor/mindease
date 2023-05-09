"""Run flask app as production."""

import os
from setproctitle import setproctitle
from waitress import serve
from src.app import app

PORT = int(os.getenv("APP_PORT"))  # type: ignore
setproctitle("mindease")  # sets custom name for process

# servers flask app using waitress
serve(app, host="0.0.0.0", port=PORT, threads=8)
