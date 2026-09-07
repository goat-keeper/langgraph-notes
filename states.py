import os


# 1) typed DICT

from typing import TypedDict

class State(TypedDict):
    topic: str
    summary: str
    score: int
    
# 2) using pydantic 
from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic : str 
    score :int 
    summary : str = ""

    @field_validator
    def score_positive(cls,v):
        if v < 0:
            raise ValueError("score must be positive")
        
# 3)python data classes

from dataclasses import dataclass, field
@dataclass
class State:
    topic : str = ""
    summary  : str = ""
    messages : list = field(default_factory=list)

# 4) langraph message state

from langgraph.graph import MessagesState

class State(MessagesState):
    user_name:str
    language:str