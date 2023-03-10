import math
import sys
from crossword import *
import copy, queue, random


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        domains_copy = copy.deepcopy(self.domains)
        for var in domains_copy:
            for word in domains_copy[var]:
                if var.length != len(word):
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        domains_copy = copy.deepcopy(self.domains)
        index = self.crossword.overlaps[x, y]
        if index is not None:
            x_index = index[0]
            y_index = index[1]
            for x_word in domains_copy[x]:
                matched = False
                for y_word in domains_copy[y]:
                    if x_word[x_index] == y_word[y_index]:
                        matched = True
                        break
                if not matched:
                    self.domains[x].remove(x_word)
                    revised = True
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # initialize the queue
        que = queue.Queue()
        if not arcs:
            for x in self.domains:
                for y in self.domains:
                    if x != y:
                        que.put((x, y))
        else:
            for x, y in arcs:
                que.put((x, y))

        # enforce the arc consistent
        while not que.empty():
            x, y = que.get()
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x):
                    if y != z:
                        que.put((z, x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.domains:
            if var not in assignment:
                return False
            else:
                if assignment[var] is None:
                    return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # unary constraint satisfaction
        for var in assignment:
            if var.length != len(assignment[var]):
                return False

        # binary constraint satisfaction
        for var in assignment:
            neighbors = self.crossword.neighbors(var)
            for neighbor_var in neighbors:
                if neighbor_var in assignment:
                    index = self.crossword.overlaps[var, neighbor_var]
                    if index is not None:
                        x_index = index[0]
                        y_index = index[1]
                        if assignment[var][x_index] != assignment[neighbor_var][y_index]:
                            return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        words_dict = {}
        neighbors = self.crossword.neighbors(var)
        for word in self.domains[var]:
            ruled_out_word_num = 0
            for neighbor_var in neighbors:
                x_index, y_index = self.crossword.overlaps[var, neighbor_var]
                if neighbor_var not in assignment:
                    for neighbor_value in self.domains[neighbor_var]:
                        if word[x_index] != neighbor_value[y_index]:
                            ruled_out_word_num += 1
            words_dict[word] = ruled_out_word_num
        return sorted(words_dict.keys(), key=lambda key: words_dict[key])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        variable = None
        variables = []
        values_num = math.inf
        for var in self.domains:
            if var not in assignment:
                # choose the one with the minimum number of remaining values in its domain
                if len(self.domains[var]) < values_num:
                    variable = var
                    variables.clear()
                    variables.append(var)
                    values_num = len(self.domains[var])
                elif len(self.domains[var]) == values_num:
                    degree_old = len(self.crossword.neighbors(variable))
                    degree_new = len(self.crossword.neighbors(var))
                    # choose the one with the highest degree
                    if degree_new > degree_old:
                        variable = var
                        variables.clear()
                        variables.append(var)
                    elif degree_new == degree_old:
                        variables.append(var)

        return random.choice(variables)

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.consistent(assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                else:
                    assignment.pop(var)
        return None


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
