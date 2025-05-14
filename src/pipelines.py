from typing import Dict, Any
from langchain_core.messages import HumanMessage
from langchain_ollama import OllamaLLM

from agent_tools import web_search

llm = OllamaLLM(model="gemma:2b")


def research_step(query: str) -> Dict[str, Any]:
    snippet = web_search.invoke(query)
    history = [HumanMessage(content=f"User Query: {query}"), HumanMessage(content=snippet)]
    return {"query": query, "research_result": snippet, "chat_history": history}


def synthesis_step(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = HumanMessage(content=f"Based on the research below, write a detailed report:\n\n{state['research_result']}")
    output = llm.invoke([prompt] + state['chat_history'])
    state['chat_history'] += [prompt, HumanMessage(content=output)]
    state['final_report'] = output
    return state


def tweet_step(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = HumanMessage(content=f"Based on the research below, create 3 concise tweets:\n\n{state['research_result']}")
    output = llm.invoke([prompt] + state['chat_history'])
    state['chat_history'] += [prompt, HumanMessage(content=output)]
    state['tweets'] = output
    return state
