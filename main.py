import mysql.connector

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
            (b'content-length', b'11'),
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello Ian4!',
    })
