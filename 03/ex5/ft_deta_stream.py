import typing
import random


def get_event() ->typing.Generator[tuple[str,str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "sleep", "move", "eat", "grab", "release", "climb", "swim", "use"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]]
    ) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.choice(event_list)
        event_list.remove(index)
        yield index

def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = get_event()
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = []
    for _ in range(10):
        event_list.append(next(events))
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")

if __name__ == "__main__":
    main()
