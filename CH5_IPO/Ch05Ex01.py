# This program calculates the property tax on the assessment value of property (75% of actual property value)

ASSESS_PRECENTAGE = 0.75
PROP_TAX = 1.11

def assessment_calc(property_value: float) -> float:
    assess_value = property_value * ASSESS_PRECENTAGE
    return assess_value

def property_tax_calc(assess_value: float) -> float:
    tax = assess_value // 100 * PROP_TAX
    return tax

def main() -> None:
    prop_value = float(input("Enter the actual property value: "))
    assess_value = assessment_calc(prop_value)
    prop_tax = property_tax_calc(assess_value)

    print(f"The assessed value is ${assess_value:,.2f}")
    print(f"The property tax is ${prop_tax:,.2f}")

if __name__ == "__main__":
    main()