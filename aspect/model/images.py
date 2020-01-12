from aspect import db


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(length=128))
    directory = db.Column(db.String(length=128))

    # def __repr__(self):
    #     return '<Images(file_name="{0}", directory="{1}")>'.format(self.file_name, self.directory)
