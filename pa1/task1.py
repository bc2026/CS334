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
        print("Input String:")
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
            next_state = self.state_to_go_to(possible_states, curr_choice)
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





