'''from .greeting_agent.agent  import root_agent as agent

__all__ = ["agent"]'''
from .agent import root_agent as agent

__all__ = ["agent"]
'''import sys, os
print("CWD:", os.getcwd())
print("PYTHONPATH:", sys.path)
try:
    import basicagent101
    print("✅ Imported basicagent101:", basicagent101)
    print("Has agent?", hasattr(basicagent101, "agent"))
except Exception as e:
    print("❌ Import failed:", e)'''