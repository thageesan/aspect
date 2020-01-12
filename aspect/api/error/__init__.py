from flask import jsonify

class ApiError:
    manifest = {
        '1': {
            'detail': 'General (unknown) error.',
            'status': 500,
            'title': 'Internal Server Error.'
        },
        '2': {
            'detail': 'Could not retrieve image data.',
            'status': 404,
            'title': 'Not found.'
        },
        '3': {
            'detail': 'Issue with the image data.  Please try again later.',
            'status': 500,
            'title': 'Internal Server Error.'
        }
    }

    def __init__(self, code):
        error_object = self.manifest.get(code)
        self.message = jsonify({
            'status': error_object['status'],
            'detail': error_object['detail'],
            'title': error_object['title']
        }), error_object['status']