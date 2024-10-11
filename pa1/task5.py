import sys
from collections import deque

class NDFA:
    def __init__(self, states, sigma, dlt, qs, F):
        self.states = states  # List of states
        self.sigma = sigma    # Alphabet
        self.dlt = dlt        # Transitions as a dictionary
        self.qs = qs          # Initial state
        self.F = F            # Accepting (final) states

    def read_from_stdin(self):
        # Read states
        states = input()
        states = eval(states)

        # Read alphabet
        sigma = sys.stdin.readline()
        sigma = eval(sigma)

        # Read transitions
        dlt = sys.stdin.readline()
        dlt = eval(dlt)

        # Read initial state
        qs = sys.stdin.readline()
        qs = eval(qs)

        # Read final states
        F = sys.stdin.readline()
        F = eval(F)

        self.states, self.sigma, self.dlt, self.qs, self.F = states, sigma, dlt, qs, F

    @staticmethod
    def encode_set(my_set: list) -> int:
        """
        Encode a subset of states as an integer using bitwise representation.
        Each bit represents whether a state is included in the subset.
        """
        return sum(1 << state for state in my_set)

    def dfa_delta(self, subset: tuple, symbol: str) -> tuple:
        """
        Compute the union of transitions for all states in the subset on the given symbol.
        """
        next_states = set()
        for state in subset:
            next_states.update(self.dlt.get((state, symbol), []))
        return tuple(sorted(next_states))

    def convert_to_dfa(self) -> dict:
        """
        Perform subset construction via BFS to include only reachable subsets.
        Returns the transition dictionary of the DFA.
        """
        transition_dict = {}
        visited = set()
        queue = deque()

        # Initial subset
        initial_subset = frozenset([self.qs])
        encoded_initial = self.encode_set(list(initial_subset))
        queue.append(initial_subset)
        visited.add(initial_subset)

        while queue:
            current_subset = queue.popleft()
            encoded_current = self.encode_set(list(current_subset))

            for symbol in self.sigma:
                # Compute the next subset
                next_subset = self.dfa_delta(current_subset, symbol)
                encoded_next = self.encode_set(list(next_subset))
                transition_dict[(encoded_current, symbol)] = encoded_next

                frozen_next = frozenset(next_subset)
                if frozen_next not in visited:
                    visited.add(frozen_next)
                    queue.append(frozen_next)

        return transition_dict

    def reduced_dfa(self, transition_dict: dict) -> dict:
        """
        Sort the transition dictionary by state and symbol for consistent output.
        """
        return dict(sorted(transition_dict.items(), key=lambda x: (x[0][0], x[0][1])))

# Create an NDFA instance
ndfa = NDFA([], [], {}, "", [])

# Read NDFA specification from standard input
ndfa.read_from_stdin()

# Convert NDFA to DFA with reachable states
dfa_transition = ndfa.convert_to_dfa()

# Sort the transition dictionary
sorted_dfa = ndfa.reduced_dfa(dfa_transition)

# Print the sorted DFA transition function in the required format
for key, value in sorted_dfa.items():
    print(f"({key[0]}, '{key[1]}'): {value}")
