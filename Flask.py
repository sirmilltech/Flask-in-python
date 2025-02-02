from flask import Flask
from flask_restful import Api, Resource, regparse
import pandas as import pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    # Write method to fetch data from the CSV file
    def get(self):
        pass

    def post(self):
    # Write method to write data to the CSV file
        pass

    def delete(self):
    # Write method to update data in the CSV file
        pass
    
# Add URL endpoints
api.add_resource(Users, '/users')

from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'name'      : [args['name']],
            'age'       : [args['age']],
            'city'      : [args['city']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('users.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['name'] != args['name']]

        data.to_csv('users.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()
    
    
    # imports the JSON library to work in python
import json

# assign the JSON data to a variable
json_data = """{
                "data": [
                    {
                        "type": "articles",
                        "id": "1",
                        "attributes": {
                            "title": "Working with JSON Data in python",
                            "description": "This article explains the various ways to work with JSON data in python.",
                            "created": "2020-12-28T14:56:29.000Z",
                            "updated": "2020-12-28T14:56:28.000Z"
                        },
                        "author": {
                            "id": "1",
                            "name": "Aveek Das"
                        }
                    }
                ]
            }"""

# Print the datatype of the original variable before deserialization
print(f'Datatype before deserialization: {str(type(json_data))}')
print("\n")

# Deserialize the JSON to a python dictionary object
new_data = json.loads(json_data)

# Print the datatype of the new variable after deserialization
print(f'Datatype after deserialization: {str(type(new_data))}')
print(new_data)
print("\n")


# Serialize the python dictionary object back to JSON string
reset_data = json.dumps(new_data)

# Print the datatype of the new variable after deserialization
print(f'Datatype after serialization: {str(type(reset_data))}')
print(reset_data)


 REST APIs