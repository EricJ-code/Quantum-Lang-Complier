import re

# Define patterns for different categories
PATTERNS = {
    'literals': r'\b\d+\.?\d*|\'.*?\'\b',  # Numbers and strings
    'operators': r'\b(H|X|Y|Z|CNOT|np\.dot)\b',  # Quantum gates and np.dot
    'variables': r'\bqubit_state_[0-9]+\b',  # Variables like qubit_state_0, qubit_state_1, etc.
    'reserved_words': r'\b(qubit|quantum-circuit|apply|measure)\b',  # Keywords in the language
    'data_types': r'\bQubits\b'  # Simplified to 'Qubits' for this context
}

def tokenize(code):
    """
    Tokenize the input code into categories based on PATTERNS.
    """
    tokens = {category: [] for category in PATTERNS}

    for category, pattern in PATTERNS.items():
        matches = re.findall(pattern, code)
        tokens[category].extend(matches)
    
    return tokens

def print_report(tokens):
    """
    Print a report based on the categorized tokens.
    """
    print("Parsing Report:")
    print("="*40)
    for category, items in tokens.items():
        unique_items = set(items)  # Remove duplicates for listing
        print(f"{category.capitalize()} (count: {len(items)}): {', '.join(unique_items) if items else 'None'}")
    
    print("="*40)
    print(f"Total lines processed: {len(code.splitlines())}")

# Example usage
if __name__ == "__main__":
    # Sample code (you can replace this with file reading logic)
    code = """
    qubit q1
    qubit q2
    H(q1)
    CNOT(q1, q2)
    measure(q1)
    measure(q2)
    np.dot(H, qubit_state_0)
    """

    tokens = tokenize(code)
    print_report(tokens)
