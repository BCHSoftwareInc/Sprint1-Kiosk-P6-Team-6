"""
BCH Software Inc. | Sprint 2 - Apex Security Turnstile   (SE - Story 1)
Client: Apex Entertainment - "The Vortex" coaster

check_entry() is the decision engine. It does NOT print or ask for input -
it only takes facts in and hands a result code back. That is what makes it
unit-testable (QA and CCA are writing tests against it RIGHT NOW).

Result codes (exact strings - tests compare them, spelling matters):
    "GRANTED"                Patron may ride
    "GRANTED_VIP"            VIP may ride (fast lane)
    "DENIED_NO_TICKET"       ticket type is UNAUTHORIZED, missing, or unknown
    "DENIED_INVALID"         height or age is impossible (bad scan)
    "DENIED_TOO_SHORT"       under 48 inches - applies to VIPs too
    "DENIED_NEEDS_GUARDIAN"  under 13 with no guardian present
"""

MIN_HEIGHT_IN = 48.0
MIN_SOLO_AGE = 13
MAX_HEIGHT_IN = 96
MAX_AGE = 120
VALID_TICKETS = ("PATRON", "VIP")


def check_entry(ticket_type, height_in, age, has_guardian):
    # Check the rules IN THIS ORDER. The first rule that matches wins - return right away.

   # Rule 1: Check if ticket_type is valid. Only return if INVALID.
    if ticket_type not in VALID_TICKETS:
        return "DENIED_NO_TICKET"
        
    # Rule 2: Check for physically impossible/invalid scans
    if height_in <= 0 or height_in > MAX_HEIGHT_IN or age < 0 or age > MAX_AGE:
        return "DENIED_INVALID"
        
    # Rule 3: Physical safety height restriction (applies to VIPs too)
    if height_in < MIN_HEIGHT_IN:
        return "DENIED_TOO_SHORT"
        
    # Rule 4: Age restrictions and chaperone requirements
    if age < MIN_SOLO_AGE and not has_guardian:
        return "DENIED_NEEDS_GUARDIAN"
        
    # Rule 5: Ticket routing (VIP vs Standard Patron)
    if ticket_type == "VIP":
        return "GRANTED_VIP"
    else:
        return "GRANTED"


def is_granted(result_code):
    return result_code.startswith("GRANTED")
