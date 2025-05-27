#complimenting agent
from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message: str
    name: str

def compliment_node(state: AgentState) -> AgentState:
    """A node that updates the state with a compliment message."""
    state['message'] = f"{state['name']}, you are doing a great job!"
    return state

graph = StateGraph(AgentState)
graph.add_node("compliment", compliment_node)
graph.set_entry_point("compliment")
graph.set_finish_point("compliment")
app = graph.compile()
# The app can now be used to manage the agent's state
import graphviz
from IPython.display import display, Image
display(Image(app.get_graph().draw_mermaid_png()))
result = app.invoke(AgentState(name="Dilip"))
# Display the result    
print(result["message"])  # Output: "Dilip, you are doing a great job!"
# Display the graph