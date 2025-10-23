from fastapi import FastAPI
from data_loader import load_all_data

app = FastAPI(title="TFT Recommender API")

# 预加载静态数据
champions, traits, items = load_all_data()

@app.get("/")
def root():
    return {"message": "TFT Recommender API is running 🚀"}

@app.get("/data/champions")
def get_champions():
    return {"count": len(champions), "data": champions[:10]}  # 只返回前10个避免太大
from fastapi import FastAPI
from data_loader import load_all_data

app = FastAPI(title="TFT Recommender API")

# 预加载静态数据
champions, traits, items = load_all_data()

@app.get("/")
def root():
    return {"message": "TFT Recommender API is running 🚀"}

@app.get("/data/champions")
def get_champions():
    return {"count": len(champions), "data": champions[:10]}  # 只返回前10个避免太大
