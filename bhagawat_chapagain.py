# your_first_name, your_last_name, your_section, your_email_address
# Bhagawat, Chapagain, A (8am), bchapaga@stevens.edu

inputA = ['0']  # Symbols the machine can read
tapeA = ['0', '2', '3', '4' '_']  # Initial tape

    tF = {
    0: {'0': ['0', 'R', 1]},
    1: {'0': ['2', 'R', 1], '_': ['_', 'L', 2]},
    2: {
        '3': ['3', 'L', 2],
        '4': ['4', 'L', 2],
        '2': ['3', 'R', 3],
        '0': ['0', 'R', 4]
    },
    3: {
        '2': ['2', 'R', 3],
        '3': ['3', 'R', 3],
        '4': ['4', 'R', 3],
        '_': ['4', 'L', 2]
    },
    4: {
        '3': ['0', 'R', 4],
        '4': ['0', 'R', 5],
        '_': ['_', 'L', 5]
    },
    5: {
        '4': ['2', 'R', 5],
        '_': ['_', 'L', 2]
    }
}