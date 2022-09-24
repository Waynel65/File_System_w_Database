from config import *

class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

def list_files():
    files = Files.query.all()
    file_info = [{"File_Name": f.file_name, "Date_Added": f.date_added}for f in files]
    return file_info