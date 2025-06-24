# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers import users

app = FastAPI(
    title="FastAPI 사용자 관리 시스템",
    description="FastAPI, Redis, Docker를 이용한 회원가입, 로그인 및 사용자 관리 예제입니다.",
    version="0.0.1",
)

templates = Jinja2Templates(directory="templates")

app.include_router(users.router, prefix="/redis")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)