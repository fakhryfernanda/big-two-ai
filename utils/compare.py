def compare_group(group1, group2):
    """
    Compare two groups of the same type (pair, triple, quad) based on the highest card.
    
    Parameters:
    - group1 (list of Card): The first group of cards (e.g., a pair, triple, or quad).
    - group2 (list of Card): The second group of cards (same type as group1).
    
    Returns:
    - 1 if group1 is stronger
    - -1 if group2 is stronger
    - 0 if they are equal
    """
    max_card1 = max(group1, key=lambda c: c.value())
    max_card2 = max(group2, key=lambda c: c.value())
    
    return (max_card1.value() > max_card2.value()) - (max_card1.value() < max_card2.value())