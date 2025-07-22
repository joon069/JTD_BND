import uvicorn
from fastapi import FastAPI
from app.routers import diary, auth, todo
from app.database import create_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5501", #프론트가 여기에 있으면 이걸 허용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 허용할 origin 목록
    allow_credentials=True,
    allow_methods=["*"],              # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],              # 모든 헤더 허용
)

app.include_router(diary.router)
app.include_router(auth.router)
app.include_router(todo.router)

create_tables()

@app.get("/")
def root():
    return {"message": "FastAPI 서버가 잘 실행되고 있습니다!"}

@app.delete("/test-delete/{item_id}")
async def test_delete(item_id: int):
    print(f"DELETE 요청 받음: {item_id}")
    return {"msg": f"Deleted item {item_id}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)