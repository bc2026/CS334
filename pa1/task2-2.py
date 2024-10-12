import sys
class NDFA:
    def __init__(self, states, sigma, dlt, qs, F):
        self.states = states  # List of states
        self.sigma = sigma    # Alphabet
        self.dlt = dlt        # Transitions as a dictionary
        self.qs = qs          # Initial state
        self.F = F            # Accepting (final) states

    def create_matrix_of_zeros(self, rows=1, cols=1):
        M = []
        for s in range(rows):
            M.append([0] * cols)
        return M

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
        #print("Input String:")
        input_string = sys.stdin.readline()
        input_string = eval(input_string)
        return input_string

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
            try: next_state = self.state_to_go_to(possible_states, curr_choice)
            except IndexError: break
            states.append(next_state)                                                                                                                                                                         
            curr_state = next_state

        return ([states] + [True]) if states[-1] in self.F else ([states] + [False])

    def generate_all_processing_paths(self, tape):         
        results = {}         

        def explore(current_state, input_index, choice_sequence, state_sequence):             
            # Check if we've processed the entire tape             
            if input_index == len(tape):                 
                results[(tuple(choice_sequence), tuple(state_sequence))] = (current_state in self.F)               
                return             
                   
            symbol = tape[input_index]             

            options = self.dlt.get((current_state, symbol), [])             
            if not options:                 
                results[(tuple(choice_sequence), tuple(state_sequence))] = False                 
                return             
         
            for idx, next_state in enumerate(options):                 
                explore(next_state, input_index + 1, choice_sequence + (idx,), state_sequence + (next_state,))         

        # Start exploration from the initial state         
        explore(self.qs, 0, (), (self.qs,))         
        return results 
        
        
# Create an NDFA instance
ndfa = NDFA([], [], {}, "", [])

# Read NDFA specification from standard input
input_string = ndfa.read_from_stdin1a()



for k,v in ndfa.generate_all_processing_paths(input_string).items():
    print(f"({k[0]}, {k[1]}) --> {v}")



