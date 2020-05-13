#!/usr/bin/env python3

import re
import sys
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


class LocalHTTPRequestHandler(SimpleHTTPRequestHandler):

    server_version = "Local (" + SimpleHTTPRequestHandler.server_version + ")"

    def do_GET(self):
        if re.match(r"^/style\..+\.css$", self.path):
            path = self.path
            self.path = "/style.css"
            sys.stderr.write(f"Intercepted {path}, rewriting to {self.path} ...\n")

        SimpleHTTPRequestHandler.do_GET(self)


def start():

    site_dir = "site"

    handler = partial(LocalHTTPRequestHandler, directory=site_dir)

    with ThreadingHTTPServer(("", 8000), handler) as httpd:
        print(f"Serving files from './{site_dir}'")
        print("  on 0.0.0.0 port 8000 (http://0.0.0.0:8000)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping.")
            sys.exit(0)


if __name__ == "__main__":

    start()
