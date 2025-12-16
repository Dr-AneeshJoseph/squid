import re

class InkMasker:
    """
    Layer 2: The Ink
    Responsible for sanitizing user input and handling parameterization.
    """
    
    @staticmethod
    def quarantine_input(user_query: str) -> str:
        """
        Wraps user input in triple quotes and escapes existing quotes
        to prevent 'breakout' attacks.
        """
        # 1. Neutralize triple quotes to prevent escaping the wrapper
        safe_query = user_query.replace('"""', "'")
        
        # 2. Return the Quarantined Block
        return f'"""\n{safe_query}\n"""'

    @staticmethod
    def extract_result(llm_response: str) -> str:
        """
        Parses the __RESULT__ block from the LLM output.
        """
        match = re.search(r"__RESULT__\s*(.*?)\s*(__STATE__|$)", llm_response, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
      
