#!/home/dh_vd6eid/aspect/bin/python3.6
from aspect import create_app


if __name__ == '__main__':
    app = create_app('dev_config.ini')
    from flup.server.fcgi_fork import WSGIServer
    WSGIServer(app).run()
