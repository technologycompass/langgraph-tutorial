#Agent State
from typing import TypedDict, Dict
from langgraph.graph import StateGraph 

#we now create Agent State - a shared data structure that will be used to store the state of the agent
class AgentState(TypedDict): #our state schema
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """A node that updates the state with a greeting message."""
    state['message'] = "Hey there! " + state['message'] + " How can I help you today?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeting", greeting_node)
graph.set_entry_point("greeting")
graph.set_finish_point("greeting")
app = graph.compile()
