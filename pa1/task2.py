import sys
>>>>>>> 11f9850b774729d751c4fe5d57764ca9f16e18ab

<<<<<<< HEAD
    # @staticmethod
    # def create_matrix_of_zeros(self, rows=1, cols=1):
    #     M = []
    #     for s in range(rows):
    #         M.append([0] * cols)
    #     return M

    @staticmethod
    def generate_binary_combinations(l):
    # Base case: if l is 0, return an empty list
    if l == 0:
        return ['']
    
    # Recursive case: generate combinations of size l-1
    smaller_combinations = generate_binary_combinations(l - 1)
    
    # Add '0' or '1' to each combination of size l-1
    result = []
    for comb in smaller_combinations:
        result.append('0' + comb)
        result.append('1' + comb)
    
    return result

    def read_from_stdin(self):
        states = input()
        states = eval(states)

        # print("Alphabet: ")
        sigma = sys.stdin.readline()
        sigma = eval(sigma)

        #print("Transitions: ")
        dlt = sys.stdin.readline()
        dlt = eval(dlt)

        #print("Initial State: ")
        qs = sys.stdin.readline()
        qs = eval(qs)

        #print("Final States: ")
        F = sys.stdin.readline()
        F = eval(F)

        self.states, self.sigma, self.dlt, self.qs, self.F = states, sigma, dlt, qs, F

    def read_from_stdin1a(self):
        self.read_from_stdin()
        print("Input String:")
        input_string = sys.stdin.readline()
        input_string = eval(input_string)
        return input_string

    
    def generate_all_processing_paths(self, input_string: str) -> str:
        possible_options = generate_binary_combinations(len(input))
        input_string_size = len(input_string)

        for comb in possible_options:
            try:
                print("({0})->({1})".format(comb, follow_choices(comb, input_string))
            except IndexError:
                continue

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
            possible_states = self.dlt[(curr_state, curr_string_input)]

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
print(result)






=======
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

        results = {}  # To store processing paths and accept/reject status
        
        for comb in possible_options:
            try:
                states, accepted = self.follow_choices(comb, input_string)  # Get states and acceptance status
                results[(tuple(comb), tuple(states))] = accepted  # Store result in dictionary
            except IndexError:
                continue  # Skip invalid paths

        # Print the results in the required format
        for key, value in results.items():
            print(f"{key} --> {value}")

    @staticmethod
    def state_to_go_to(option_list: list, index: int):
        try:
            return option_list[index]
        except IndexError:
            error_msg = "No state to go to with index " + str(index)
            raise IndexError(error_msg)
            
    def follow_choices(self, choice_sequence: list, input_string: str) -> tuple:
        curr_state = self.qs
        states = [curr_state]
        
        for i in range(len(input_string)):
            curr_choice = choice_sequence[i]
            curr_string_input = input_string[i]
            possible_states = self.dlt.get((curr_state, curr_string_input), [])  # Use get to avoid KeyError

            try:
                next_state = self.state_to_go_to(possible_states, curr_choice)
            except IndexError: 
                break  # If no valid state, break the loop

            states.append(next_state)
            curr_state = next_state

        # Return states and True if final state is accepting, False otherwise
        return (states, True) if states[-1] in self.F else (states, False)

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
ndfa.generate_all_processing_paths(input_string)

>>>>>>> 11f9850b774729d751c4fe5d57764ca9f16e18ab