import panel as pn

from bokeh.embed import server_document
from sliders.pn_app import createApp

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def bkapp_page(request: Request):
    script = server_document("http://127.0.0.1:5000/app")
    return templates.TemplateResponse(
        "base.html", {"request": request, "script": script}
    )


pn.serve(
    {"/app": createApp},
    address="127.0.0.1",
    port=5000,
    show=False,
    allow_websocket_origin=["127.0.0.1:8000"],
)
