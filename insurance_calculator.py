def calculate_annual_premium(age, vehicle_type, past_accidents):
    """Calculates yearly car insurance premium based on risk factors."""
    base_price = 500  # Base rate

    # 1. Age risk factor
    if age < 25:
        base_price += 300
    elif age > 65:
        base_price += 150

    # 2. Vehicle risk factor
    if vehicle_type.lower() == "sports":
        base_price += 250
    elif vehicle_type.lower() == "suv":
        base_price += 100

    # 3. Accident history ($150 added per past accident)
    base_price += past_accidents * 150

    return base_price


def process_claim(claim_amount, total_coverage_limit):
    """Checks whether an insurance claim should be approved or reviewed."""
    if claim_amount > total_coverage_limit:
        return "REJECTED: Claim exceeds total policy coverage."
    elif claim_amount > (total_coverage_limit * 0.75):
        return "FLAGGED: High-value claim requires manual agent review."
    else:
        return "APPROVED: Claim is within instant payout limits."


# --- Program Execution ---
if __name__ == "__main__":
    print("=== INSURANCE QUOTE GENERATOR ===")
    
    # Sample Customer
    customer_age = 22
    car_type = "sports"
    prior_accidents = 1
    coverage = 10000

    # Calculate Price
    yearly_price = calculate_annual_premium(customer_age, car_type, prior_accidents)
    print(f"Customer: Age {customer_age}, Car: {car_type}, Accidents: {prior_accidents}")
    print(f"Estimated Yearly Premium: ${yearly_price}\n")

    # Process Sample Claim
    print("=== CLAIM EVALUATION ===")
    claim_val = 8000
    result = process_claim(claim_val, coverage)
    print(f"Claim Amount: \({claim_val} (Coverage Limit:\){coverage})")
    print(f"Status: {result}")
