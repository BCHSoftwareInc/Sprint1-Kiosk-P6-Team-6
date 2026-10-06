"""
BCH Software Inc. | Sprint 2 - Story 2   (SE)
TurnstileGate wraps the decision engine and keeps the day's analytics.
"""
from functools import total_ordering
from unittest import result
from gate_rules import check_entry, is_granted


class TurnstileGate:
    def __init__(self):
        self.granted_count = 0
        self.denied_count = 0

        #scans for granted and denied entries
    def scan(self, ticket_type, height_in, age, has_guardian):


        #adds 1 to granted or denied count based on the result of check_entry
        result = check_entry(ticket_type, height_in, age, has_guardian)
        if is_granted(result):
            self.granted_count += 1
        else:
            self.denied_count += 1


        return result

    def total_scans(self):
        # TODO: return granted + denied
        
        total_ordering = self.granted_count + self.denied_count

        return total_ordering
