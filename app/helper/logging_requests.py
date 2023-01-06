import logging
import os
import sys
import textwrap
from logging.handlers import TimedRotatingFileHandler

import requests

httplogger = logging.getLogger("httplogger")


def logRoundtrip(response, *args, **kwargs):
    extra = {"req": response.request, "res": response}
    httplogger.debug("HTTP roundtrip", extra=extra)


class HttpFormatter(logging.Formatter):
    def _formatHeaders(self, d):
        return "\n".join(f"{k}: {v}" for k, v in d.items())

    def formatMessage(self, record):
        result = super().formatMessage(record)
        if record.name == "httplogger":
            result += textwrap.dedent(
                """
                ---------------- request ----------------
                {req.method} {req.url}
                {reqhdrs}

                {req.body}
                ---------------- response ----------------
                {res.status_code} {res.reason} {res.url}
                {reshdrs}

                {res.text}
            """
            ).format(
                req=record.req,
                res=record.res,
                reqhdrs=self._formatHeaders(record.req.headers),
                reshdrs=self._formatHeaders(record.res.headers),
            )

        return result


class RequestsStreamHandler(logging.StreamHandler):
    def __init__(self, formatter: logging.Formatter):
        super().__init__(sys.stdout)
        self.setFormatter(formatter)


class RequestsTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, formatter: logging.Formatter):
        path = "logs"

        if not os.path.exists(path):
            os.mkdir(path)

        super().__init__(path + "/requests.log", when="d")
        self.setFormatter(formatter)


formatter = HttpFormatter("{asctime} {levelname} {name} {message}", style="{")

# root.addHandler(RequestsStreamHandler(formatter))
httplogger.addHandler(RequestsTimedRotatingFileHandler(formatter))
httplogger.setLevel(logging.DEBUG)

session = requests.Session()
session.hooks["response"].append(logRoundtrip)
