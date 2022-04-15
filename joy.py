from numpy import append
from flask import Flask, jsonify
from flask_restful import reqparse

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/')
def fun():
    x="Hello"
    return x

@app.route('/bfhl', methods=['POST'])
def inx():
    parser = reqparse.RequestParser()
    parser.add_argument('data', type=list)
    args = parser.parse_args()  
    # print("*****",args)
    lis = args['data']
    # print("****",lis)
    is_success = True
    user_id = "joydeep_biswas_10062001"
    email = "joydeepbiswas751@gmail.com"
    roll_number = "0827CI191029"
    a, b = [], []
    print(lis)
    for i in lis:
        if (not i.isdigit() and not i.isalpha()):
            is_success= False
            break
        else:
            if i.isdigit():
                a.append(i)
            else:
                b.append(i)

    if is_success:
        dic = {
            "is_success": is_success,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": a,
            "alphabets": b
        }
    else:
        dic = {
            "is_success": is_success,
            "user_id": user_id
        }
    return jsonify(dic)


if __name__ == "__main__":
    app.run(debug=True)


# i='1A2'
# print(not i.isdigit() and not i.isalpha())