from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# create State
class workerState(TypedDict):
    worker_name: str
    uan: str
    esic: str
    status: str

initial_state = {
    "worker_name": "Rahul Kumar",
    "uan": "123456789012",
    "esic": "1234567890",
    "status": "Pending"
}

#Create node
def validate_worker(state: workerState):

    if state["uan"] and state["esic"]:
        return {"status": "Valid"}

    return {"status": "Invalid"}

def approve_worker(state: workerState):
    print("Worker approved:", state["worker_name"])
    return {"status": "Approved"}

""" Important: A node normally returns a dictionary containing only the state fields it wants to update."""

##create edges and connect node (decide workflow)

builder = StateGraph(workerState)

builder.add_node("validate", validate_worker)
builder.add_node("approve", approve_worker)

builder.add_edge(START, "validate")
builder.add_edge("validate", "approve")
builder.add_edge("approve", END)

graph = builder.compile()

result = graph.invoke(initial_state)

print(result)




