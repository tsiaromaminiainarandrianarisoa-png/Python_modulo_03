import random
from typing import Generator


def gen_event() -> Generator:
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'run', 'move', 'climb', 'swim', 'release']
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player,action)


def consume_event(events: list) -> Generator:
    while len(events) > 0:
        loc = random.randint(0, len(events)-1)
        event = events.pop(loc)
        yield event


if __name__ == "__main__":
    event = gen_event()
    for c in range(1000):
        result = next(event)
        print(f"Event {c}: {result[0]} did {result[1]}")
    events = [0,1,2,3,4,5,6,7,8,9]
    for t in range(10):
        events[t] = result = next(event)
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {(event)}")
        print(f"Remains in list: {events}")
