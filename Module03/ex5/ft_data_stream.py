
from random import choice, randrange
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        player = choice(players)
        action = choice(actions)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = randrange(len(events))
        yield events.pop(index)


if __name__ == "__main__":

    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    # Parte 1: gerar 1000 eventos
    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    # Parte 2: criar lista com 10 eventos
    event_list = [next(stream) for _ in range(10)]

    print(f"\nBuilt list of 10 events: {event_list}\n")

    # Parte 3: consumir a lista
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
