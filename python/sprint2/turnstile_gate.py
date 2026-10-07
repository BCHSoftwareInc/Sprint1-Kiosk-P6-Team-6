"""
BCH Software Inc. | Sprint 2 - Story 2   (SE)
TurnstileGate wraps the decision engine and keeps the day's analytics.
"""
from functools import total_ordering
from unittest import result
from gate_rules import check_entry, is_granted


class TurnstileGate:
   def __init__(self):
        self._granted_count = 0
        self._denied_count = 0

   def scan(self, ticket_type, height_in, age, has_guardian):
        # Get the decision from the rules engine
        result = check_entry(ticket_type, height_in, age, has_guardian)

        # Update the appropriate counter
        if is_granted(result):
            self._granted_count += 1
        else:
            self._denied_count += 1

        return result

   def granted_count(self):
        return self._granted_count

   def denied_count(self):
        return self._denied_count

   def total_scans(self):
        return self._granted_count + self._denied_count

   def total_scans(self):
        # TODO: return granted + denied
        
        return self._denied_count + self._granted_count
