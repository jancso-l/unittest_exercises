def calculate_tax(amount, age, tax_rate=17.0):
    """Calculate income tax based on the amount and the age of the person."""
 
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be an integer or a float")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
 
    if age < 0:
        raise ValueError("Age cannot be negative")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
 
    if age <= 18:
        return int(min(amount * tax_rate / 100, 6000))
    elif age <= 65:
        return int(amount * tax_rate / 100)
    else:
        return int(min(amount * tax_rate / 100, 9000))