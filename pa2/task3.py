class CFG:
def __init__(self, terminals, variables, rules):
self.terminals = terminals
self.variables = variables
self.rules = rules

def apply_single_rule(self, sequence, rule_index, left_to_right):
# Apply a single rule based on left-to-right or right-to-left approach
if left_to_right:
for idx, symbol in enumerate(sequence):
if symbol in self.variables:
return sequence[:idx] + self.rules[symbol][rule_index] + sequence[idx+1:]
else:
for idx in range(len(sequence) - 1, -1, -1):
if sequence[idx] in self.variables:
return sequence[:idx] + self.rules[sequence[idx]][rule_index] + sequence[idx+1:]
return sequence

def apply_multiple_rules(self, sequence, rule_indices, left_to_right):
# Apply each rule from the rule list
for rule_index in rule_indices:
sequence = self.apply_single_rule(sequence, rule_index, left_to_right)
return sequence

def construct_parse_tree(self, sequence, rule_sequence, parse_tree, left_to_right):
# Base case: If no more rules or all symbols are terminals, return the parse tree
if not rule_sequence or all(symbol in self.terminals for symbol in sequence):
return parse_tree

# Determine the next variable to replace
if left_to_right:
target_symbol = next((symbol for symbol in sequence if symbol in self.variables), None)
target_index = sequence.index(target_symbol)
else:
target_symbol = next((symbol for symbol in reversed(sequence) if symbol in self.variables), None)
target_index = sequence.rindex(target_symbol)

if target_symbol is None:
return parse_tree # No more variables left to substitute

# Retrieve the production rule for the current variable
production = self.rules[target_symbol][rule_sequence[0]]
rule_sequence.pop(0) # Remove the applied rule from the sequence

# Construct a subtree for the selected production
new_subtree = [[char, []] for char in production]

# Recursive helper to place the subtree in the correct position
def insert_subtree(node, target, subtree):
if node[0] == target and not node[1]:
node[1] = subtree
return True
for branch in node[1]:
if insert_subtree(branch, target, subtree):
return True
return False

# Update parse tree with the newly constructed subtree
insert_subtree(parse_tree, target_symbol, new_subtree)

# Modify the sequence based on the applied production
updated_sequence = sequence[:target_index] + production + sequence[target_index + 1:]

# Recursively apply remaining rules
children = []
if left_to_right:
# Process leftmost productions recursively
for char in updated_sequence:
subtree = self.construct_parse_tree(char, rule_sequence, [char, []], left_to_right)
children.append(subtree)
else:
# Process rightmost productions recursively
for char in reversed(updated_sequence):
subtree = self.construct_parse_tree(char, rule_sequence, [char, []], left_to_right)
children.insert(0, subtree)

# Attach the children nodes to the parse tree
parse_tree[1] = children

return parse_tree

@staticmethod
def extract_leaves(tree):
# Retrieve leaf nodes from the parse tree
if not tree[1]:
return [tree[0]]
leaves = []
for branch in tree[1]:
leaves.extend(CFG.extract_leaves(branch))
return leaves


def parse_input():
terminals = eval(input().strip())
variables = eval(input().strip())
productions = eval(input().strip())
start_symbol = eval(input().strip())
rule_sequence = eval(input().strip())
is_left = eval(input().strip())

return terminals, variables, productions, start_symbol, rule_sequence, is_left

def main():
terminals, variables, productions, start_symbol, rule_sequence, is_left = parse_input()
initial_tree = [start_symbol, []]
cfg = CFG(terminals, variables, productions)

# Construct the parse tree based on production rules
result_tree = cfg.construct_parse_tree(start_symbol, rule_sequence, initial_tree, is_left)
print(result_tree)

if __name__ == '__main__':
    main()

