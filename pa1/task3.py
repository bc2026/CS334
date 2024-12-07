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
        # states
        states = input()
        states = eval(states)

        # print("Alphabet: ")
        sigma = sys.stdin.readline()
        sigma = eval(sigma)

        # print("Transitions: ")
        dlt = sys.stdin.readline()  # Changed from sys.stdin.readline() to input()
        dlt = eval(dlt)

        # print("Initial State: ")
        qs = sys.stdin.readline()  # Changed from sys.stdin.readline() to input()
        qs = eval(qs)

        # print("Final States: ")
        F = sys.stdin.readline()  # Changed from sys.stdin.readline() to input()
        F = eval(F)

        self.states, self.sigma, self.dlt, self.qs, self.F = states, sigma, dlt, qs, F

    def read_from_stdin1a(self):
        self.read_from_stdin()
        # Input string
        input_string = sys.stdin.readline() 
        input_string = eval(input_string)
        
        x2 = sys.stdin.readline()
        x2 = eval(x2)
        return [input_string, x2]

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


    @staticmethod
    def encode_set(my_set: list, numstates: int) -> tuple:
        # Initialize a binary string representation
        sum_list = ['0'] * numstates
        sum_bin = 0

        for i in range(numstates):
            if i in my_set:
                sum_bin += (2 ** i)  # Add to the binary sum
                sum_list[i] = '1'  # Update the list at position i to '1'
        
        # Convert the list back to a string and reverse it
        sum_str = ''.join(sum_list)
        
        return (sum_str, sum_bin)
    
    @staticmethod
    def decode_set(number: int, numstates: int) -> tuple:
        # Initialize an empty binary string and an empty list for the positions
        bin_string = ''
        bin_positions = []

        # Loop through the number of states from 0 to numstates - 1
        for i in range(numstates):
            # Check if the least significant bit is 1
            if number % 2 == 1:
                bin_positions.append(i)  # Add the position to the list
                bin_string = '1' + bin_string  # Prepend '1' to the binary string
            else:
                bin_string = '0' + bin_string  # Prepend '0' if the bit is 0

            # Shift the number to the right to check the next bit
            number = number // 2

        return (bin_string, tuple(bin_positions))
    
    def dfa_delta(self, subset: tuple, symbol: str) -> tuple:
        
        dfa_list = []
        for item in subset:
            if(item!=None):
                dfa_list += (self.dlt[(item, symbol)])
        
        return tuple(list(set(dfa_list)))
    
    def convert_to_dfa(self) -> dict:
                
        numstates = 2 ** len(ndfa.states)

        subset_dict = {}
        for state in range(numstates):
            x0 = self.dfa_delta(decode_set(state, numstates)[1], '0')
            x1 = self.dfa_delta(decode_set(state, numstates)[1], '1')

            subset_dict[(state, '0')] = encode_set(x0, numstates)[1]
            subset_dict[(state, '1')] = encode_set(x1, numstates)[1]
            
    return subset_dict

