from flask import Flask,request,jsonify
import string
import secrets


app=Flask(__name__ , static_url_path="",static_folder="static")

@app.route("/")
def index ():
    return app.send_static_file("index.html")



def  generate_password (lenght=8,
                      include_uppercase=True,
                      include_numbers=True,
                      include_special=True):
    char=string.ascii_lowercase

    if include_uppercase:
        char+=string.ascii_uppercase
    if include_numbers:
        char+=string.digits
    if include_special:
        char+=string.punctuation  

    if not char :
        return ""

    password="".join(secrets.choice(char)for _ in range(lenght))     
    return password


@app.route("/generate_password",methods=["POST"])
def generat ():
    data=request.get_json() or {}

    lenght=data.get("lenght",8)
    include_uppercase=data.get("include_uppercase",True)
    include_numbers=data.get("include_numbers",True)  
    include_special=data.get("include_special",True)

    try:
        lenght = int(lenght)
    except ValueError:
        return jsonify({"error":"Length must be an integer"}),400
    
    if lenght<= 0 :
        return jsonify ({"error":"lenght must positive"})
    
    password=generate_password(lenght,include_uppercase,include_numbers,include_special)
    return jsonify({"password":password})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 