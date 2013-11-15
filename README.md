SimpleTornadoServer
===================

Use tornado's static file handler to replace `SimpleHTTPServer` in Python standard library, with this you can simply type only one command and run an HTTP server on the port you desired, the default port **8000** is as the same as the `SimpleHTTPServer` provided.

Installation
------------

    python setup.py install
    
Usage
-----

    $ python -m SimpleTornadoServer
    Serving HTTP on 0.0.0.0 port 8000 ...
    
the default port is `8000`, or

	$ python -m SimpleTornadoServer [PORT]
		
Also, you can use `SocketServer.ThreadingMixin` and `BaseHttpServer.HTTPServer` for the ability of concurrency.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/imom0/simpletornadoserver/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

