build : index.html style.css favicon.ico robots.txt about.html open.html
	mkdir site
	cp index.html site/index.html
	cp style.css site/style.css
	cp favicon.ico site/favicon.ico
	cp robots.txt site/robots.txt
	mkdir -p site/about
	cp about.html site/about/index.html
	mkdir -p site/2020/04/open
	cp open.html site/2020/04/open/index.html

clean :
	rm -rf site
