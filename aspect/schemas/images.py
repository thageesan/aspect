from flask_sqlalchemy import Pagination

from aspect import ma


class ImagesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            'id',
            'file_name',
            'directory'
        )

    @staticmethod
    def _pagination_links(pagination_obj: Pagination, request: str):
        return {
            'first': request.format(page_number=1, limit=pagination_obj.per_page),
            'last': request.format(page_number=pagination_obj.pages,
                                   limit=pagination_obj.per_page) if pagination_obj.pages is not None else None,
            'prev': request.format(page_number=pagination_obj.prev_num,
                                   limit=pagination_obj.per_page) if pagination_obj.prev_num is not None else None,
            'next': request.format(page_number=pagination_obj.next_num,
                                   limit=pagination_obj.per_page) if pagination_obj.next_num is not None else None,
        }

    def paginate_dump(self, pagination_obj: Pagination, request: str):
        result = {}
        data = getattr(pagination_obj, 'items', [])
        result['data'] = self.dump(data, many=True)
        result['links'] = ImagesSchema._pagination_links(pagination_obj, request)
        return result
