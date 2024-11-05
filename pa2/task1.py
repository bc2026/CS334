class CFL:
    def __init__(terminals : list, variables : list, productions : dict, left : bool):
        self.terminals   = terminals
        self.variables   = variables
        self.productions = productions
        self.left = left
    
        def read_from_stdin1():
            terminals = input()
            terminals = eval(terminals)

            variables = sys.stdin.readline()
            variables = eval(variables)

            productions = sys.stdin.readline()
            productions = eval(productions)

            mystring = sys.stdin.readline()
            mystring = eval(mystring)

            rule_num = sys.stdin.readline()
            rule_num = eval(rule_num)

            left = sys.stdin.readline()
            left = eval(left)

            return terminals, variables, productions, mystring, rule_num, left
        
        def apply_single_production(self, string, index, left):
            if left:
                for i in string:
                    if i in variables:
                        until_v = string[:string.index(i)]
                        after_v = string[1+string.index(i):]

                        replacement = until_v + self.productions[i][index] + after_v
            else:
                replacement = ""
                for i in string:
                    if i in variables:
                        new_index = len(str) - str[::-1].index(i)

                        until_v = string[:new_index]
                        after_v = string[1+new_index:]

                        replacement = until_v + self.productions[i][index] + after_v
                        break

                return replacement
                # '(a+b)*(E+E) => 