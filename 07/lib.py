class Program:
    'I fight for the users'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.programs_held = []
        self.holding_programs = False
        self.is_base = True
        self.held_by = ""
    
    def give_program_to_hold(self, program_name):
        self.programs_held.append(program_name)
        self.holding_programs = True
    
    def set_held_by(self, program_name):
        self.held_by = program_name
        self.is_base = False

    def is_holding_programs(self):
        return self.holding_programs
    
    def is_base_case(self):
        return self.is_base
    
    def get_programs_held(self):
        return self.programs_held
    
    def get_weight(self):
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
                "\n\tHolding: {}"
                "\n\tHeld By: {}").format(self.name, self.weight, self.programs_held, self.held_by)

def build_program_tower(dataset):
    tower = {}
    prog_heldby_pairs = []
    for data in dataset:
        newprogram = Program(data[0], data[1])
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
    return tower

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