POST: para crear datos.
GET: para leer datos.
PUT: para actualizar datos.
DELETE: para borrar datos.

fastAPI options

```
@app.post()
@app.put()
@app.delete()
```

also:
```
@app.options()
@app.head()
@app.patch()
@app.trace()
```
Parámetros de path

Puedes declarar los "parámetros" o "variables" con la misma sintaxis que usan los format strings de Python:

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

