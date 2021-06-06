import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'odoo'
USER = 'mohammedegila@gmail.com'
PASS = '136537f7438091a4e9f92f10f46b8df5aefb2f18'


def json_rpc(method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(service, method, *args):
    return json_rpc("call", {"service": service, "method": method, "args": args})


def fetch_data_from_odoo(*args):
    return call("object", "execute", DB, uid, PASS, 'pharmacy.pharmacy', 'search_read', *args)


def sync_data_to_odoo(*args):
    return call("object", "execute", DB, uid, PASS, 'pharmacy.pharmacy', 'create', *args)


url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call("common", "login", DB, USER, PASS)
