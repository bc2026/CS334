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
        states = input("States: ")
        states = eval(states)

        print("Alphabet: ")
        sigma = sys.stdin.readline()
        sigma = eval(sigma)

        print("Transitions: ")
        dlt = sys.stdin.readline()
        dlt = eval(dlt)

        print("Initial State: ")
        qs = sys.stdin.readline()
        qs = eval(qs)

        print("Final States: ")
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
        curr_choice = choice_sequence[0]
        curr_string_input = input_string[0]
        curr_state = 
        
        possible_states = self.dlt[(current_state, curr_string_input)]
        next_state = state_to_go_to(possible_states, curr_choice)



