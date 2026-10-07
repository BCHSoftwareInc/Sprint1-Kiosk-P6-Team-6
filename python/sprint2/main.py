"""
BCH Software Inc. | Sprint 2 - Story 2   (SE)
Console front end for the Vortex turnstile. Type END SHIFT as the ticket to stop.
"""
from unittest import result
from turnstile_gate import TurnstileGate


def ask_number(prompt):
    # Keeps asking until the user types a real number (a crash here = failed Desk Hack)
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("  Please enter a number.")


def main():
    gate = TurnstileGate()
    print("=== APEX VORTEX TURNSTILE - ONLINE ===")

    granted = 0
    denied = 0
    total = 0

    while True:
        ticket_type = input("Enter your ticket type: ").strip().upper()

        if ticket_type == "END SHIFT":
            break

        height = ask_number("Enter your height: ")
        age = int(ask_number("Enter your age: "))

        guardian_answer = input("Guardian present? (y/n): ").strip().lower()
        guardian_bool = guardian_answer == "y"

        result = gate.scan(0, ticket_type, height, age, guardian_bool)
        print(result)

        total += 1

        if "GRANTED" in str(result).upper():
            granted += 1
        else:
            denied += 1

    print("\n=== SHIFT REPORT ===")
    print(f"Granted: {granted}")
    print(f"Denied: {denied}")
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
