from bs4 import BeautifulSoup
import requests, zmq, json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

waiting = True
while waiting:
    # url sent by client
    message = json.loads(socket.recv())
    url = message['url']
    print(f"URL Found! Pulling data from \n{url}")

    #pulls data from website
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    '''
    I went ahead and designed this to go ahead and pull the entire body text to be sent back
    I tried to send the body object so you could parse it yourself, but zeroMQ was giving a
    recursion error, so this sends back all the text from p tags and then sends them in an array.
    '''
    body = soup.find('body')
    body_p_tags = body.find_all('p')

    #For loop to move all p tags into a list
    paragraphs = []
    for i in range(0, len(body_p_tags)):
        paragraphs.append(body_p_tags[i].text)

    socket.send_string(json.dumps({'data': paragraphs}))
    if url:
        waiting = False