# imperfectbutpublished.org

Build the site:

    make clean && make

Start a local HTTP server:

    python3 -m http.server --directory site

[http://0.0.0.0:8000](http://0.0.0.0:8000)

Set up a tunnel:

    ngrok http 8000

[http://127.0.0.1:4040](http://127.0.0.1:4040)
