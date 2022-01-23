# python3


class DisjointSet:
    def __init__(self, nodes, parents, ranks):
        self.nodes = nodes
        self.parents = parents
        self.ranks = ranks

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j, max_count):
        i_id = self.find(i - 1)
        j_id = self.find(j - 1)
        if i_id == j_id:
            return self.nodes, max_count
        while self.nodes[i_id] == -1:
            i_id = self.parents[i_id]
        while self.nodes[j_id] == -1:
            j_id = self.parents[j_id]
        if self.ranks[i_id] > self.ranks[j_id]:
            self.parents[j_id] = i_id
            sum_nodes = self.nodes[i_id] + self.nodes[j_id]
            self.nodes[i_id] = sum_nodes
            self.nodes[j_id] = -1
            if sum_nodes > max_count:
                max_count = sum_nodes
        else:
            self.parents[i_id] = j_id
            sum_nodes = self.nodes[i_id] + self.nodes[j_id]
            self.nodes[i_id] = -1
            self.nodes[j_id] = sum_nodes
            if sum_nodes > max_count:
                max_count = sum_nodes
            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1
        return self.nodes, max_count


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))
        self.ds = DisjointSet(self.row_counts, self.parents, self.ranks)

    def merge(self, src, dst):
        self.row_counts, max_count = self.ds.union(dst, src, self.max_row_count)
        self.max_row_count = max_count


def main():
    file = open('1.txt', 'r')
    n_tables, n_queries = map(int, file.readline().split())
    counts = list(map(int, file.readline().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, file.readline().split())
        db.merge(dst, src)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
