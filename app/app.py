from config import * 
from database import *


db.create_all() # table is created upon running the flask application

@app.route("/", methods=["GET", "POST"]) # index page
def index():
    if request.method == "POST": # request to upload file
        file = request.files['file']
        if file:
            upload = Files(file_name=file.filename, data=file.read())
            db.session.add(upload) # add the file to DB
            db.session.commit()
            print(f"{file.filename} was uploaded")
    file_info = list_files() # gather the updated list of files
    # print(file_info)
    return render_template("index.html", file_info=file_info) # display the list of files

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST": # a post that sends in the file ID to download the corresponding file
        file_id = request.form.get("file_id")
        file = Files.query.filter_by(id=file_id).first() 
        return send_file(BytesIO(file.data), attachment_filename=file.file_name, as_attachment=True) # convert bytes back to actual file



if __name__ == '__main__':
    app.run(debug=False)


# Notes:
# connect to docker