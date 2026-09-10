from state import AgentState

from agents.safety_agent import SafetyAgent
from agents.intent_agent import IntentAgent
from agents.health_query_agent import HealthQueryAgent
from agents.recommendation_agent import RecommendationAgent
from agents.herb_info_agent import HerbInfoAgent


from agents.safety_agent import SafetyAgent

def safety_node(state):
    agent = SafetyAgent()

    result = agent.run(state["question"])

    state["safe"] = result["safe"]

    if not result["safe"]:
        state["answer"] = result["answer"]   

    return state


def intent_node(state: AgentState):

    intent = IntentAgent().run(state["question"])
    state["intent"] = intent

    return state


def health_node(state: AgentState):

    result = HealthQueryAgent().run(state["question"])

    state["answer"] = result["answer"]
    state["docs"] = result["sources"]
    state["herbs"] = result["herbs"]

    return state


def recommendation_node(state: AgentState):

    result = RecommendationAgent().run(state["question"])

    state["answer"] = result["answer"]
    state["docs"] = result["sources"]
    state["herbs"] = result["herbs"]

    return state


def herb_node(state: AgentState):

    result = HerbInfoAgent().run(state["question"])

    state["answer"] = result["answer"]
    state["docs"] = result["sources"]
    state["herbs"] = result["herbs"]

    return state