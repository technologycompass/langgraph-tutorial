from typing import List, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    """
    Represents the state of the agent in the graph.
    """
    values: list[int]
    name: str
    result: str


def process_values(state: AgentState) -> AgentState:
    """
    Processes a list of integers and returns a string representation.
    """
    state["result"] = f"Hi there, {state['name']}! Your sum = {sum(state['values'])} values: {', '.join(map(str, state['values']))}."
    return state

graph = StateGraph(AgentState)
graph.add_node("processor", process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")
app = graph.compile()

# Import and use graphviz directly
import graphviz
from PIL import Image

# Create and configure the graph
dot = graphviz.Digraph(comment='Multi Value State Graph')
dot.attr(rankdir='LR')
dot.node('processor', 'Process Values')
dot.edge('START', 'processor')
dot.edge('processor', 'END')

# Save the graph
dot.render('multi_value_graph', format='png', cleanup=True)

# Display using PIL
img = Image.open('multi_value_graph.png')
img.show()
