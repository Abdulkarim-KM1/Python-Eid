import uvicorn # pip install uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app:app", port=8000, reload=True)
