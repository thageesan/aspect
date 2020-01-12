from marshmallow.exceptions import MarshmallowError
from sqlalchemy import exc
from flask import jsonify
from aspect.model import Images
from aspect.api.error import ApiError
from aspect.schemas.images import ImagesSchema


def ping():
    return jsonify({
        'result': 'pong'
    })


def get_images(limit=100, offset=1):
    per_page = limit
    page = offset
    error_object = None
    result = None
    try:
        image_pagination_object = Images.query.order_by(
            Images.id.asc()
        ).paginate(page, per_page)
        result = ImagesSchema().paginate_dump(image_pagination_object, '/api/v1/images?limit={limit}&offset={'
                                                                       'page_number}')
    except exc.SQLAlchemyError:
        error_object = ApiError('2')
    except exc.ArgumentError:
        error_object = ApiError('2')
    except MarshmallowError:
        error_object = ApiError('3')
    finally:
        if result is None:
            error_object = ApiError('2')
        if error_object is None:
            return jsonify(result)
        else:
            return error_object.message
