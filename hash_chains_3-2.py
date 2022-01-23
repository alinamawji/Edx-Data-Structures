# python3


file = open('5.txt', 'r')


class Block:
    def __init__(self, string):
        self.value = string
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_block(self, string):
        if self.find_string(string) == 'yes':
            return
        block = Block(string)
        block.next = self.head
        self.head = block

    def del_block(self, string):
        curr_block = self.head
        if curr_block is None:
            return
        elif curr_block.next is None:
            if curr_block.value == string:
                self.head = None
        else:
            prev_block = self.head
            while curr_block.next is not None:
                if curr_block.value == string:
                    if curr_block.value == prev_block.value:
                        self.head = curr_block.next
                        return
                    else:
                        prev_block.next = curr_block.next
                        return
                else:
                    prev_block = curr_block
                    curr_block = curr_block.next
            if curr_block.value == string:
                prev_block.next = curr_block.next

    def find_string(self, string):
        curr_block = self.head
        if curr_block is None:
            return 'no'
        elif curr_block.next is None:
            if curr_block.value == string:
                return 'yes'
            else:
                return 'no'
        else:
            while curr_block.next is not None:
                if curr_block.value == string:
                    return 'yes'
                curr_block = curr_block.next
            if curr_block.value == string:
                return 'yes'
            return 'no'

    def check_hash(self):
        return_str = ''
        curr_block = self.head
        if curr_block is None:
            return return_str
        elif curr_block.next is None:
            return_str += curr_block.value + ' '
            return return_str
        else:
            while curr_block.next is not None:
                return_str += curr_block.value + ' '
                curr_block = curr_block.next
            return_str += curr_block.value + ' '
            return return_str


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = list()
        self.result = ''

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(file.readline().split())

    def process_query(self, query):
        if query.type != 'check':
            hash_num = self._hash_func(query.s)
            if query.type == 'add':
                self.elems[hash_num].add_block(query.s)
            elif query.type == 'del':
                self.elems[hash_num].del_block(query.s)
            elif query.type == 'find':
                str = self.elems[hash_num].find_string(query.s)
                self.result += str + '\n'

        else:
            linked_list = self.elems[query.ind]
            str = linked_list.check_hash()
            self.result += str + '\n'

    def process_queries(self):
        for i in range(self.bucket_count):
            self.elems.append(SinglyLinkedList())

        n = int(file.readline())
        for i in range(n):
            self.process_query(self.read_query())
        return self.result


if __name__ == '__main__':
    bucket_count = int(file.readline())
    proc = QueryProcessor(bucket_count)
    final_str = proc.process_queries()
    print(final_str)
