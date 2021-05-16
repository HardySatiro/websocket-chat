from browser import prompt, websocket, window, document, html, bind

def on_message(evt):
    messages = document['messages']
    messages <= html.P(evt.data)
    if f'{user} disse' not in evt.data:
        document["hardao"].play()

def on_open(evt):
    ws.send(f'{user} Entrouuuu na salala')

@bind('#send', 'click')
def on_enviar(evt):
    message = document["text_message"].value
    if len(message) > 1 or "\n" not in message:
        ws.send(f'{user} disse: {message}')
        document["text_message"].value = ""
    else:
        document["text_message"].value = ""

@bind('#text_message', 'keydown')
def on_lala(evt):
    if evt.which == 13:
        on_enviar(evt)

user = prompt('Digite seu nome para o chat')

if window.location.protocol == "https:":
    ws_scheme = "wss://"
else:
    ws_scheme = "ws://"
print(f'{ws_scheme}{window.location.host}/ws/duplex/{user}')
ws = websocket.WebSocket(f'{ws_scheme}{window.location.host}/ws/duplex/{user}')
ws.bind('message', on_message)
ws.bind('open', on_open)