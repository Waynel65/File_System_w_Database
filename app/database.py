# a table in the file sys database
from config import db
from sqlalchemy.sql import func

class Files(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary(length=(2**24)-1)) # a medium blob that can store up to 16.78 Mb
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

def list_files():
    """
        returns a list of all files stored in DB 
    """
    files = Files.query.all()
    file_info = [{"File_ID": f.id, "File_Name": f.file_name, "Date_Added": f.date_added} for f in files]
    return file_info

def list_files_in_alph_order():
    file_info = list_files()
    sorted_list = sorted(file_info, key=lambda d: d["File_Name"])
    return sorted_list