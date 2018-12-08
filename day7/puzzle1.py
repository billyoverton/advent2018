#!/usr/bin/env python3

import sys
import re

class Step:
    def __init__(self, label):
        self.label = label
        self.depends_on = set()
        self.dependency_for = set()

    def add_substep(self, step):
        if step not in self.dependency_for:
            self.dependency_for.add(step)
            step.add_dependency(self)

    def add_dependency(self, step):
        if step not in self.depends_on:
            self.depends_on.add(step)
            step.add_substep(self)

class SleighInstructions:
    __message_pattern = re.compile("^Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

    def __init__(self):
        self.steps = {}

    def add_step(self, step_message):
        m = self.__message_pattern.match(step_message)

        if m is None:
            print("ERROR: Not a valid step")
            print(step_message)
            sys.exit(1)

        dependency = m.group(1)
        step = m.group(2)

        if dependency not in self.steps:
            self.steps[dependency] = Step(dependency)
        if step not in self.steps:
            self.steps[step] = Step(step)

        self.steps[step].add_dependency(self.steps[dependency])

    def get_processing_order(self):
        # I don't like this because it destorys the instructions
        order = []

        while len(self.steps) > 0:
            ready_steps = {}

            # Get all instructions with no dependencies
            for label, step in self.steps.items():
                if len(step.depends_on) == 0:
                    ready_steps[label] = step

            chosen = min(ready_steps.keys())

            order.append(chosen)

            # remove the processed step from the substeps
            for substep in self.steps[chosen].dependency_for:
                substep.depends_on.remove(self.steps[chosen])

            del(self.steps[chosen]) # remove the processed item

        return order

def main(input_file):
    instructions = SleighInstructions()
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            instructions.add_step(line)

    order = instructions.get_processing_order()
    print("".join(order))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
