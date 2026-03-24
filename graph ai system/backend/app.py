from fastapi import FastAPI
from query_engine import process_query
from graph_builder import build_graph

app = FastAPI()

graph = build_graph()

@app.get("/")
def home():
    return {"message": "Graph AI System Running"}

@app.post("/query")
def query(q: str):
    response = process_query(q, graph)
    return {"response": response}
