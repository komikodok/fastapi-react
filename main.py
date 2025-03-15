from fastapi import FastAPI
from router.user_router import user_router


app = FastAPI(
    title="Rest API with Firebase Firestore.",
    description="Integrate fastapi with cloud firestore."
)

app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)