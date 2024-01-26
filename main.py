from fastapi import FastAPI
from routes.api_routes_genarate import courses_routes_qrcode

app = FastAPI()

app.include_router(courses_routes_qrcode)



# import uvicorn

# async def app(scope, receive, send):
#     assert scope['type'] == 'http'

#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })