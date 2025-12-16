import os
from .ink.masker import InkMasker
from .tentacles.validator import TentacleValidator

class SquidProxy:
    def __init__(self, schema_str: str):
        self.masker = InkMasker()
        self.validator = TentacleValidator()
        self.schema = schema_str
        
        # Load System Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'beak', 'system_prompt.md')
        with open(prompt_path, 'r') as f:
            self.base_prompt = f.read()

    def construct_prompt(self, user_query: str) -> str:
        """Constructs the full Context Sandwich."""
        quarantined_input = self.masker.quarantine_input(user_query)
        
        full_prompt = (
            f"{self.base_prompt}\n\n"
            f"# ACTIVE SCHEMA\n{self.schema}\n\n"
            f"USER_DATA_STRING:\n{quarantined_input}"
        )
        return full_prompt

    def process_response(self, llm_raw_response: str):
        """
        Pipeline: Extract -> Validate -> Return
        """
        # 1. Extract SQL from __RESULT__
        sql_candidate = self.masker.extract_result(llm_raw_response)
        if not sql_candidate:
            return {"valid": False, "error": "Output format violation (No __RESULT__)"}

        # 2. Validate SQL via AST
        is_valid, msg = self.validator.validate(sql_candidate)

        if is_valid:
            return {"valid": True, "sql": sql_candidate, "status": "SECURE"}
        else:
            return {"valid": False, "error": msg, "rejected_sql": sql_candidate}
          
