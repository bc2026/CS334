import sys

class NDFA:
    def __init__(self, states, sigma, dlt, qs, F):
        self.states = states  # List of states
        self.sigma = sigma    # Alphabet
        self.dlt = dlt        # Transitions as a dictionary
        self.qs = qs          # Initial state
        self.F = F            # Accepting (final) states

    @staticmethod
    def generate_binary_combinations(l):
        # Base case: if l is 0, return an empty list
        if l == 0:
            return [[]]
        
        # Recursive case: generate combinations of size l-1
        smaller_combinations = NDFA.generate_binary_combinations(l - 1)  # Add class name

        # Add '0' or '1' to each combination of size l-1
        result = []
        for comb in smaller_combinations:
            result.append([0] + comb)
            result.append([1] + comb)
        
        
        return result

    def read_from_stdin(self):
        states = input()
        states = eval(states)

        # print("Alphabet: ")
        sigma = input()  # Changed from sys.stdin.readline() to input()
        sigma = eval(sigma)

        # print("Transitions: ")
        dlt = input()  # Changed from sys.stdin.readline() to input()
        dlt = eval(dlt)

        # print("Initial State: ")
        qs = input()  # Changed from sys.stdin.readline() to input()
        qs = eval(qs)

        # print("Final States: ")
        F = input()  # Changed from sys.stdin.readline() to input()
        F = eval(F)

        self.states, self.sigma, self.dlt, self.qs, self.F = states, sigma, dlt, qs, F

    def read_from_stdin1a(self):
        self.read_from_stdin()
        print("Input String:")
        input_string = input()  # Changed from sys.stdin.readline() to input()
        input_string = eval(input_string)
        return input_string

    def generate_all_processing_paths(self, input_string: str):
        possible_options = NDFA.generate_binary_combinations(len(input_string))  # Fixed to input_string
        input_string_size = len(input_string)

        for comb in possible_options:
            try:
                print("({0}, {1})->{2}".format(comb, self.follow_choices(comb, input_string)[0], self.follow_choices(comb, input_string)[1] ))  # Fixed
            except IndexError:
                break

    @staticmethod
    def state_to_go_to(option_list: list, index: int):
        try:
            return option_list[index]
        except IndexError:
            error_msg = "No state to go to with index " + str(index)
            raise IndexError(error_msg)
            
    def follow_choices(self, choice_sequence: list, input_string: str) -> list:
        curr_state = self.qs
        states = [curr_state]
        
        for i in range(len(input_string)):
            curr_choice = choice_sequence[i]
            curr_string_input = input_string[i]
            possible_states = self.dlt.get((curr_state, curr_string_input), [])  # Use get to avoid KeyError

            try:
                next_state = self.state_to_go_to(possible_states, curr_choice)
            except IndexError: 
                break

            states.append(next_state)
            curr_state = next_state

        return ([states] + [True]) if states[-1] in self.F else ([states] + [False])

# Define the elements for the NDFA
states = [0, 1, 2, 3]
sigma = ['0', '1']
dlt = {
    (0, '0'): [0, 1],
    (0, '1'): [0],
    (1, '0'): [2],
    (1, '1'): [2],
    (2, '0'): [3],
    (2, '1'): [],
    (3, '0'): [3],
    (3, '1'): [3]
}
qs = 0
F = [3]

# Create the NDFA instance
ndfa = NDFA(states, sigma, dlt, qs, F)

# Define the choice sequence and input string
choice_sequence = [0, 0, 0, 0, 1, 0]
input_string = '101101'

# Test the follow_choices method
result = ndfa.follow_choices(choice_sequence, input_string)

# Print the result
print(ndfa.generate_all_processing_paths(input_string))
