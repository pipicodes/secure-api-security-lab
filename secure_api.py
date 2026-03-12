from fastapi import FastAPI, HTTPException, Header

app = FastAPI(title="Secure API Security Lab - Secure Version")

users = {
    1: {"id": 1, "name": "Alice", "balance": 5000},
    2: {"id": 2, "name": "Bob", "balance": 3000},
    3: {"id": 3, "name": "Charlie", "balance": 7000},
}

def get_current_user(x_user_id: str = Header(None)):
    if x_user_id is None:
        raise HTTPException(status_code=401, detail="Missing X-User-Id header")

    try:
        user_id = int(x_user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid X-User-Id header")

    if user_id not in users:
        raise HTTPException(status_code=401, detail="Invalid user")

    return user_id

@app.get("/")
def root():
    return {"message": "Secure API running"}

@app.get("/users/{user_id}")
def get_user(user_id: int, x_user_id: str = Header(None)):
    current_user = get_current_user(x_user_id)

    if user_id != current_user:
        raise HTTPException(status_code=403, detail="Access denied")

    user = users.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
