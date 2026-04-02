import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Static fayllar (rasm, favicon) uchun
script_dir = os.path.dirname(__file__)
app.mount("/static", StaticFiles(directory=os.path.join(script_dir, "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # vizitka.html faylini o'qib, brauzerga yuboramiz
    with open("templates/vizitka.html", "r", encoding="utf-8") as f:
        return f.read()