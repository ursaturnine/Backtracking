class ColoringProblem:
    def __init__(self, adjacency_matrix, num_of_colors):
        # num of nodes/vertices
        self.n = len(adjacency_matrix)

        self.adjacency_matrix = adjacency_matrix
        self.num_of_colors = num_of_colors

        # as many colors as there are nodes/vertices
        self.colors = [0 for _ in range(self.n)]

    def coloring_problem(self):

        # call self.solve w the 1st vertex, index 0
        if self.solve(0):
            self.show_result()
        else:
            print('There is no feasible solution...')
        
    
    def solve(self, node_index):

        # BASE CASE
        if node_index == self.n:
            return True
        
        # consider the colors
        # assign a color index to a given node -colors are represented by numbers
        for color_index in range(1, self.num_of_colors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                # call self.solve() recursively on the next node
                if self.solve(node_index + 1):
                    return True
                
                # BACKTRACK -check the next color index for the given node
                # in this case, backtracking means 'doing nothing'

        # we tried to assign all color indices to the given node w/ no success
        return False
    
    def is_color_valid(self, node_index, color_index):

        # check that the nodes are connected
        # check that the given color is not shared with these adjacent nodes

        for i in range(self.n):
            # 1 means there is a connection between nodes
            if self.adjacency_matrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False
        
        return True
    

    def show_result(self):
        for v, c in zip(range(self.n), self.colors):
            print('Node %d has color value %d' %(v,c))


if __name__ == '__main__':

    m = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    problem = ColoringProblem(m, 3)
    problem.coloring_problem()





