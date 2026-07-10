#from . import agent
'''from importlib import import_module

def __getattr__(name):
    if name == "agent":
        return import_module(".agent", __package__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ["agent"]'''

from ..agent import root_agent as agent

__all__ = ["agent"]

'''from .greeting_agent import agent

__all__ = ["agent"]'''