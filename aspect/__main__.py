from aspect import create_app
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", help="spins up the environment in development mode", action="store_true")
    args = parser.parse_args()
    if args.dev:
        app = create_app('dev_config.ini')
    else:
        app = create_app('config.ini')
    # run standalone flask server
    app.run(port=5000)
