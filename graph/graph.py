from langgraph.graph import StateGraph, END
from state import AgentState

from graph.nodes import (
    safety_node,
    intent_node,
    health_node,
    recommendation_node,
    herb_node
)

graph = StateGraph(AgentState)

graph.add_node("safety", safety_node)
graph.add_node("intent", intent_node)
graph.add_node("health", health_node)
graph.add_node("recommendation", recommendation_node)
graph.add_node("herb", herb_node)

graph.set_entry_point("safety")

graph.add_edge("safety", "intent")


def route(state: AgentState):

    if state["safe"] is False:
        return END

    if state["intent"] == "health_query":
        return "health"

    elif state["intent"] == "recommendation":
        return "recommendation"

    else:
        return "herb"


graph.add_conditional_edges("intent", route)

graph.add_edge("health", END)
graph.add_edge("recommendation", END)
graph.add_edge("herb", END)

app = graph.compile()