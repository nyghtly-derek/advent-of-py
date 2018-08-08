class Program:
    'I fight for the users'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.programs_held = []
        self.holding_programs = False
        self.is_base = True
        self.held_by = ""
        self.true_weight = 0
    
    def give_program_to_hold(self, program_name):
        self.programs_held.append(program_name)
        self.holding_programs = True
    
    def set_held_by(self, program_name):
        self.held_by = program_name
        self.is_base = False
    
    def set_true_weight(self, true_weight):
        self.true_weight = true_weight

    def is_holding_programs(self):
        return self.holding_programs
    
    def is_base_case(self):
        return self.is_base
    
    def get_programs_held(self):
        return self.programs_held
    
    def get_weight(self, get_true=False):
        if get_true == True:
            return self.true_weight
        else:
            return self.weight
    
    def get_name(self):
        return self.name
    
    def get_held_by(self):
        if not self.is_base:
            return self.held_by
        else:
            return "is base"

    def __str__(self):
        return ("\tProgram: {}"
                "\n\tWeight: {}"
                "\n\tTrue Weight: {}"
                "\n\tHolding: {}"
                "\n\tHeld By: {}").format(self.name, self.weight, self.true_weight, self.programs_held, self.held_by)

def build_program_tower(dataset):
    tower = {}
    prog_heldby_pairs = []
    for data in dataset:
        name = data[0]
        weight = int(data[1])
        newprogram = Program(name, weight)
        if '->' in data:
            i = 3
            while i < len(data):
                newprogram.give_program_to_hold(data[i])
                if data[i] in tower:
                    tower[data[i]].set_held_by(newprogram.get_name())
                else:
                    prog_heldby_pairs.append([data[i], newprogram.get_name()])
                i += 1
        tower[newprogram.get_name()] = newprogram
    for pair in prog_heldby_pairs:
        tower[pair[0]].set_held_by(pair[1])
    calc_total_weight(tower) # recursively sets true weight value for all programs in tower
    return tower

def calc_total_weight(tower):
    base = find_base(tower)
    return find_true_weight(base.get_name(), tower)

def find_true_weight(name, tower):
    if tower[name].get_weight(True) != 0:
        return tower[name].get_weight(True)
    elif not tower[name].is_holding_programs():
        tower[name].set_true_weight(tower[name].get_weight())
        return tower[name].get_weight(True)
    else:
        t_weight = 0
        for held_name in tower[name].get_programs_held():
            t_weight += find_true_weight(held_name, tower)
        tower[name].set_true_weight(t_weight + tower[name].get_weight())
        return tower[name].get_weight(True)

def is_imbalanced(name, tower):
    """ 
    checks if program with `name` in a `tower` is imbalanced 
    returns the difference between the programs weight and what it should weigh
    (i.e. return value will be 0 if program is balanced)
    """
    if tower[name].is_base_case():
        return 0
    held_by = tower[name].get_held_by()
    neighbors = tower[held_by].get_programs_held()
    true_weights = []
    weights = {}
    count = {}
    for program in neighbors:
        weight = tower[program].get_weight()
        weights[program] = weight
        true_weight = tower[program].get_weight(True)
        true_weights.append(true_weight)
        if true_weight in count:
            count[true_weight] += 1
        else:
            count[true_weight] = 1
    most_common_weight = 0
    frequency = 0
    for true_weight in count:
        if count[true_weight] > frequency:
            most_common_weight = true_weight
            frequency = count[true_weight]
    return most_common_weight - tower[name].get_weight(True)

def print_tower(tower):
    print("Program Tower:")
    print("--------------")
    for program in tower:
        print(program)
        print(tower[program])

def find_base(tower):
    for program in tower:
        if tower[program].is_base_case():
            return tower[program]