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
# The app can now be used to manage the agent's state

#now display the graph in an image format
import graphviz
from IPython.display import display, Image
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke(AgentState(message="Dilip"))


result["message"]  # This will return the updated message with the greeting
# Output: "Hey there! Dilip How can I help you today?"
# Display the result
print(result["message"])  # Output: "Hey there! Dilip How can I help you today?"
# Display the graph
