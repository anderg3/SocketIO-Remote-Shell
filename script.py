from re import sub
from aiohttp.http_websocket import WSHandshakeError
from pyngrok import ngrok
import threading
import socketio
from aiohttp import web
import os
import requests

def StartNgrok():
    ngrok_process = ngrok.get_ngrok_process()
    try:
        ngrok.connect(8080, "http")
        tunnels = ngrok.get_tunnels()
        tunnels_split = str(tunnels[0]).split('NgrokTunnel: "')
        tunnel = str(tunnels_split[1]).split('" ->')[0]
        url = "http://localhost:9000/ngrok?link=" + tunnel
        requests.get(url=url) 
        print(tunnel) 
        ngrok_process.proc.wait()
    except KeyboardInterrupt:
        ngrok.kill()

StartNgrokThread = threading.Thread(target=StartNgrok)
StartNgrokThread.start()

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.on('message')
async def ExecuteCommand(sid, message):
    stream = os.popen(message)
    output = stream.read()
    whoami_stream = os.popen("whoami")
    whoami_output = whoami_stream.read()
    pwd_stream = os.popen("pwd")
    pwd_output = pwd_stream.read()
    await sio.emit("response", {
        "msg": str(output),
        "user": str(whoami_output),
        "directory": str(pwd_output)
    })

web.run_app(app)