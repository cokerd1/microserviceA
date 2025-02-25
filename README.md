# HTML Parsing Microservice

This Microservice will receive a URL, and then return all the text on the webpage utilizing ZeroMQ, and BeautifulSoup for web parsing.

# REQUEST and Receive Data

To request data, your program (or client like we did in the Microservices Startup assignment) will send a JSON including a text string using socket.send_string(). The
service will take the url inside the JSON and pull the website data, find the HTML <body> tag and pull all text located inside <p> tags. The text is then sent back to the main program
as a JSON including a "data" then list (so you can parse you a character limit or something similar if you would like.)
Below is an example code snippet of using it to pull a website from the Associated Press:

```
import zmq, json

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

url = "https://apnews.com/article/pope-vatican-hospital-pneumonia-sepsis-ec28babfc64d4f7086a2ba5db52fd69f"

socket.send_string(json.dumps({'url': url}))
message = json.loads(socket.recv())

for each in message['data']:
    print(each)
```

# UML Diagram
![image](https://github.com/user-attachments/assets/f1c1f623-b1a4-402e-aa32-20a7c622625b)
