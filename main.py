from fastapi import FastAPI, HTTPException

app = FastAPI(title="Secure API Security Lab - Vulnerable Version")

# Fake database
users = {
    1: {"id": 1, "name": "Alice", "balance": 5000},
    2: {"id": 2, "name": "Bob", "balance": 3000},
    3: {"id": 3, "name": "Charlie", "balance": 7000},
}

@app.get("/")
def root():
    return {"message": "Vulnerable API running"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user