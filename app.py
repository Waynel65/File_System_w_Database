from config import * 
from database import *

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        if file:
            upload = Files(file_name=file.filename, data=file.read())
            db.session.add(upload)
            db.session.commit()
            print(f"{file.filename} was uploaded")
    file_info = list_files()
    return render_template("index.html", file_info=file_info)



if __name__ == '__main__':
    app.run(debug=True)