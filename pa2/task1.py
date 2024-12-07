import sys

class CFL:
    def __init__(self, terminals: list, variables: list, productions: dict, left: bool):
        self.terminals = terminals
        self.variables = variables
        self.productions = productions
        self.left = left

    @staticmethod
    def read_from_stdin1():
        terminals = input("Enter terminals: ")
        terminals = eval(terminals)

        variables = input("Enter variables: ")
        variables = eval(variables)

        productions = input("Enter productions: ")
        productions = eval(productions)

        mystring = input("Enter the string: ")
        mystring = eval(mystring)

        rule_num = int(input("Enter the rule number: "))
        left = eval(input("Enter left (True or False): "))

        return terminals, variables, productions, mystring, rule_num, left

    def apply_single_production(self, string: str, index: int, left: bool) -> str:
        if left:
            for i in string:
                if i in self.variables:
                    until_v = string[:string.index(i)]
                    after_v = string[1 + string.index(i):]

                    replacement = until_v + self.productions[i][index] + after_v
                    return replacement  # return once replacement is done
        else:
            for i in string:
                if i in self.variables:
                    new_index = len(string) - string[::-1].index(i) - 1

                    until_v = string[:new_index]
                    after_v = string[new_index + 1:]

                    replacement = until_v + self.productions[i][index] + after_v
                    return replacement  # return once replacement is done

        return string  # return unchanged string if no production applied

def main():
    # Read input data
    parameters = CFL.read_from_stdin1()

    # Unpack parameters
    terminals, variables, productions, mystring, rule_num, left = parameters

    # Create the CFL object
    cfl = CFL(terminals, variables, productions, left)

    # Apply single production and print result
    result = cfl.apply_single_production(mystring, rule_num, left)
    print("Result after applying production:", result)

if __name__ == "__main__":
    main()
