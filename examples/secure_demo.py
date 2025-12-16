import sys
import os

# Add parent dir to path to import squid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from squid.guard import SquidProxy

# 1. Define your safe schema
SCHEMA = """
Table: employees (id, name, department, salary)
Table: sales (id, employee_id, amount, date)
"""

# 2. Initialize SQUID
proxy = SquidProxy(SCHEMA)

# 3. Simulate a User Request
user_input = "Show me the top sales for the Engineering department."

# 4. Generate the Safe Prompt (Send this to your LLM)
safe_prompt = proxy.construct_prompt(user_input)
print(f"--- SENT TO LLM ---\n{safe_prompt}\n-------------------")

# 5. Simulate LLM Response (Mock)
mock_llm_response = """
__ANALYSIS__
Intent: Sales report.
Safety: Pass.
__RESULT__
SELECT s.amount, e.name FROM sales s JOIN employees e ON s.employee_id = e.id WHERE e.department = 'Engineering'
__STATE__
{"status": "OK"}
"""

# 6. Validate Output
result = proxy.process_response(mock_llm_response)
print(f"SQUID VERDICT: {result}")

