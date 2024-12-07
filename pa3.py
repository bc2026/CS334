import sys
global MAX_LVL
def read_from_stdin():
    stra = "['S', [['A', []], ['C', []]]]"
    return eval(stra.strip())

def disp_tree(tree_list):
    # Helper function for recursion
    def helper(current_node, lvl, spacing):
        nonlocal MAX_LVL
        # Ensure lvls and positions are initialized for the current lvl
        if len(lvls) <= lvl:
            lvls.append([])
            positions.append([])

        # Add the current current_node to the lvls and positions
        current_node_str = f"'{current_node[0]}'"  # Enclose character in single quotes
        lvls[lvl].append(current_node_str)
        positions[lvl].append(spacing)

        # Update maximum lvl
        MAX_LVL = max(MAX_LVL, lvl)

        # helper for children, if any
        if current_node[1]:  # current_node has children
            child_x = spacing
            for i, child in enumerate(current_node[1]):
                helper(child, lvl + 1, child_x)
                # Add a column of space between siblings
                child_x += subtree_width[id(child)] + 1

        # Compute the subtree width for the current current_node
        subtree_width[id(current_node)] = max(
            1,  # Minimum width for a single current_node
            sum(subtree_width[id(child)] + 1 for child in current_node[1]) - 1 if current_node[1] else len(current_node_str)
        )

    # Prepare for rendering
    lvls = []  # Holds strings for each lvl
    positions = []  # Holds positions for each lvl
    subtree_width = {}  # Tracks the width of subtrees
    MAX_LVL = -1

    # Recursive traversal to calculate positions and subtree widths
    helper(tree_list, 0, 0)

    # Render the tree
    result = []
    for lvl_idx in range(MAX_LVL + 1):
        line = []
        current_pos = 0
        for pos, char in zip(positions[lvl_idx], lvls[lvl_idx]):
            # Add spaces to align current_nodes at their positions
            while current_pos < pos:
                line.append(" ")
                current_pos += 1
            line.append(char)
            current_pos += len(char)
        result.append("".join(line).rstrip())

    return "\n".join(result)

tree = read_from_stdin()
print(disp_tree(tree))
