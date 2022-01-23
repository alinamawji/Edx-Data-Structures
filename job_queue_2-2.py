# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def sift_up(self, pos):
        endpos = len(self.queue)
        startpos = pos
        newitem = self.queue[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2 * pos + 1  # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.queue[childpos] < self.queue[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.queue[pos] = self.queue[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.queue[pos] = newitem
        self.sift_down(startpos, pos)

    def sift_down(self, start, pos):
        newitem = self.queue[pos]
        while pos > start:
            parentpos = (pos - 1) >> 1
            parent = self.queue[parentpos]
            if newitem < parent:
                self.queue[pos] = parent
                pos = parentpos
                continue
            break
        self.queue[pos] = newitem

    def heappush(self, i):
        self.queue.append(i)
        self.sift_down(0, len(self.queue) - 1)

    def heappop(self):
        last = self.queue.pop()
        if self.queue:
            return_node = self.queue[0]
            self.queue[0] = last
            self.sift_up(0)
            return return_node
        return last


class Worker:
    def __init__(self, id, finish_time=0):
        self.id = id
        self.finish_time = finish_time

    def __lt__(self, other):
        if self.finish_time == other.finish_time:
            return self.id < other.id
        return self.finish_time < other.finish_time

    def __gt__(self, other):
        if self.finish_time == other.finish_time:
            return self.id > other.id
        return self.finish_time > other.finish_time


def assign_jobs(n_workers, jobs):
    result = []
    queue = PriorityQueue()
    for worker in range(n_workers):
        queue.heappush(Worker(worker))

    for job in jobs:
        worker = queue.heappop()
        result.append(AssignedJob(worker.id, worker.finish_time))
        worker.finish_time += job
        queue.heappush(worker)

    return result


def main():
    file = open('2.txt', 'r')
    n_workers, n_jobs = map(int, file.readline().split())
    jobs = list(map(int, file.readline().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
