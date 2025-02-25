# HTML Parsing Microservice

This Microservice will receive a URL, and then return all the text on the webpage utilizing ZeroMQ, and BeautifulSoup for web parsing.

# REQUEST and Receive Data

To request data, your program (or client like we did in the Microservices Startup assignment) will send a text string using socket.send_string(). The
service will take the string (url) and pull the website data, find the HTML <body> tag and pull all text located inside. The text is then sent back through the
main program. Below is an example code snippet of calling it (with a random URL for a website I already had open, MOST URL's will work but some give an error):

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

url = "https://loudwire.com/history-evolution-prog-metal-albums/"

socket.send_string(url)
message = socket.recv()
print(message.decode())
```

# UML Diagram
![image](https://github.com/user-attachments/assets/f1c1f623-b1a4-402e-aa32-20a7c622625b)
