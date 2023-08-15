from collections import deque


def person_is_seller(person):
    print(person)
    return person[-1] == 'm'


def search(name: str):
    graph = {}
    graph['you'] = ['alice', 'bob', 'clarie']
    graph['bob'] = ['peggy', 'anuj']
    graph['alice'] = ['peggy']
    graph['clarie'] = ['jonny', 'thom']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['jonny'] = []
    graph['thom'] = []

    search_queue = deque()
    search_queue += graph[name]

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
        
        print("No mango seller found!")
    return False
    

if __name__ == "__main__":
    search('you')