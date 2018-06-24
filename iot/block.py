from flask import Flask
from flask_restful import Api, Resource
import grovepi
import time


app = Flask(__name__)
api = Api(app)


# Connect the Grove LED to digital port D3
# SIG,NC,VCC,GND
led = 3

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4

# set the pinmode to Output
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(relay,"OUTPUT")

class RelayListAPI(Resource):
  def get(self):
    grovepi.digitalWrite(relay, 0)
    time.sleep(.05)
    return {"status" : 0}

class RelayAPI(Resource):
  def get(self, action):
    # If the action part of the URL is "on," execute the code indented below:
    if action == "on":
      # Set the pin high:
      grovepi.digitalWrite(relay, 1)
      return {"status" : 1}
    else:
      # Set the pin low:
      grovepi.digitalWrite(relay, 0)
      time.sleep(.05)
      return {"status" : 0}



api.add_resource(RelayListAPI, '/api/relay', endpoint = 'relays')
api.add_resource(RelayAPI, '/api/relay/<string:action>', endpoint = 'relay')

class LedListAPI(Resource):
  def get(self):
    grovepi.digitalWrite(led, 0)
    time.sleep(.05)
    return {"status" : 0}

class LedAPI(Resource):
  def get(self, action):
    # If the action part of the URL is "on," execute the code indented below:
    if action == "on":
      # Set the pin high:
      grovepi.digitalWrite(led, 1)
#      print("on")
      return {"status" : 1}
    else:
      # Set the pin low:
      grovepi.digitalWrite(led, 0)
#      print("off")
      time.sleep(.05)
      return {"status" : 0}


api.add_resource(LedListAPI, '/api/led', endpoint = 'leds')
api.add_resource(LedAPI, '/api/led/<string:action>', endpoint = 'led')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

