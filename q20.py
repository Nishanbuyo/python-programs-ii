class Triplet:
    def __init__(self, array):
        self.array = array

    def find_triplet(self):
        a = self.array
        out = []
        for i in range(len(a)-1):
            s =set()
            for j in range(i+1, len(a)):
                x= -(a[i] + a[j])
                if x in s:
                    out.append([x, a[i], a[j]])
                else:
                    s.add(a[j])
        if len(out) !=0:
            print(out)
        else:
            print("No Triplet Found")

arr = Triplet([-25, -10, -7, -3, 2, 4, 8, 10])
arr.find_triplet()
