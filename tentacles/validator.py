import sqlglot
from sqlglot import exp

class TentacleValidator:
    """
    Layer 3: The Tentacles
    Deterministic SQL Validation using Abstract Syntax Tree (AST) parsing.
    """

    def validate(self, sql_query: str):
        """
        Returns (is_valid: bool, message: str)
        """
        try:
            # Parse SQL into AST
            parsed = sqlglot.parse_one(sql_query)
        except Exception as e:
            return False, f"SYNTAX ERROR: {str(e)}"

        # RULE 1: Must be SELECT
        if not isinstance(parsed, exp.Select):
            return False, "VIOLATION: Only SELECT statements are allowed."

        # RULE 2: No Destructive Commands (Defense in Depth)
        for node in parsed.walk():
            if isinstance(node, (exp.Drop, exp.Delete, exp.Update, exp.Insert, exp.Alter)):
                return False, "VIOLATION: Destructive command found in sub-query."

        # RULE 3: Complexity Limit (Anti-DoS)
        joins = list(parsed.find_all(exp.Join))
        if len(joins) > 3:
            return False, "VIOLATION: Complexity Limit (Max 3 Joins)."

        return True, "SAFE"
      
