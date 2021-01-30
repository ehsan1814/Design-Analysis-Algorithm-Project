import fileinput

class Test:
    def __init__(self,N,M,edges,treasure_no,treasures_in_cage,power):
        self.N = N
        self.M = M
        self.edges = edges
        self.treasure_no = treasure_no
        self.treasures_in_cage = treasures_in_cage
        self.power = power

    def __str__(self):
        return str("{} | {} | {} | {} | {} | {}\n".format(self.N,self.M,self.edges,self.treasure_no,self.treasures_in_cage,self.power))


def get_each_test(ls):
    N = 0
    M = 0 
    edges = []
    treasure_no = 0
    treasures_in_cage = []
    power = 0

    N, M = ls[0].split()
    N, M = int(N), int(M)

    for i in range(1,M + 1):
        edge = ls[i].split()
        for counter in range(3):
            edge[counter] = int(edge[counter])
        edges.append(edge)
    
    treasure_no = ls[M+1].split()
    treasure_no = int(treasure_no[0])

    treasure_ls = ls[M+2].split()
    for a in treasure_ls:
        treasures_in_cage.append(int(a))

    power = ls[M+3].split()
    power = int(power[0])


    return Test(N=N,M=M,edges=edges,treasure_no=treasure_no,treasures_in_cage=treasures_in_cage,power=power)

def get_all_tests(file_content):
    i = 1 
    tests = []
    inp = file_content

    while(i < len(inp)):
        data = inp[i].split()
        length_test = int(data[1])

        tests.append(get_each_test(inp[i:i + length_test + 4]))
        i = i + length_test + 4
    
    return tests


if __name__ == "__main__":

    file_content = []
    for f in fileinput.input():
        file_content.append(f)
    
    all_tests = get_all_tests(file_content)

