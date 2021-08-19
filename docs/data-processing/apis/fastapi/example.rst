Example
=======

1. Create
---------

Create a file ``main.py`` with:

.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

2. Run
------

Run the server with:

.. code-block:: console

    $ pipenv run uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [89155] using statreload
    INFO:     Started server process [89164]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

3. Check
--------

Open your browser at http://127.0.0.1:8000/ and you will see:

.. figure:: fastapi-example.png

   :alt: FastAPI root

You will also get an interactive API documentation provided by `Swagger UI
<https://github.com/swagger-api/swagger-ui>`_ at http://127.0.0.1:8000/docs:

.. figure:: fastapi-docs-example.png

   :alt: FastAPI swagger docs

You will also get an alternative automatic documentation provided by `ReDoc
<https://github.com/Redocly/redoc>`_ at http://127.0.0.1:8000/redoc:

.. figure:: fastapi-redoc-example.png

   :alt: FastAPI ReDoc documentation

4. Update
---------

Now we modify the file ``main.py`` to receive a body from a ``PUT`` request:

.. code-block:: python
   :emphasize-lines: 3,7-10,20-22

    from typing import Optional
    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        price: float
        is_offer: Optional[bool] = None

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}

The server should reload the file automatically because we added ``--reload`` to
the uvicorn command. Also the interactive API documentation will show the new
body with ``PUT``. If you click on the button *Try it out* you will fill in
the parameter for ``item_id``. Then click on the *Execute* button and the your
browser will send the parameter to the API and show them on the screen, e.g. as
response body:

.. code-block:: javascript

    {
      "item_name": "string",
      "item_id": 1234
    }
