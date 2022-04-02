from flask import Flask
bandname = Flask(__name__)
@bandname.route("/")
def run():
    return 
print("Hello " + input("What is your name? "))
x = input("What is the name of the city you grew up in? ")
y = input("What is your favourite animal? ")
print("Hope you're not disappointed but...your band name is "+x+" "+y+"!!!")

if __name__ == "__main__":
    bandname.run(host="0.0.0.0", port=int("5000"), debug=True)