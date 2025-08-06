
class StringTokeniser:
    def tokenise(self, input_val):
        if not input_val:
            return []
        tokens = input_val.split(",") # Returns a LIST
        return [ token.strip() for token in tokens ]
