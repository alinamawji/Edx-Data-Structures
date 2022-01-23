# python3

from collections import namedtuple

Contact = namedtuple("Contact", ["name", "number"])

# TODO: time used is exceeded

class Table:
    def __init__(self, size):
        self.number_of_contacts = 0
        self.size = size
        self.contacts = dict()

    def hash(self, key):
        p = 10000019
        a = 92345
        b = 19993
        m = self.size / 0.7
        return (((a * key) + b) % p) % m

    def find_name(self, number):
        if number in self.contacts.keys():
            return self.contacts[number]

        else:
            return None

    def add_contact(self, pair):
        self.contacts[pair.number] = pair.name
        self.number_of_contacts += 1

    def del_contact(self, number):
        pop = False
        if number in self.contacts.keys():
            pop = True
        if pop:
            self.contacts.pop(number)


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    file = open('2.txt', 'r')
    n = int(file.readline())
    return [Query(file.readline().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    n = len(queries)
    t = Table(n)
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:

        if cur_query.type == 'add':
            contact = Contact(cur_query.name, cur_query.number)
            t.add_contact(contact)

        elif cur_query.type == 'del':
            t.del_contact(cur_query.number)

        else:
            name = t.find_name(cur_query.number)
            if name is None:
                response = 'not found'
            else:
                response = name
            result.append(response)

    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

