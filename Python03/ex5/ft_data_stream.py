#! /usr/bin/env python3
# def gen_event() -> typing.Generator[tuple[str, str]]:


import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    names = ["bob", "alice", "dylan", "charlie"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
            ]

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        event_list: list[tuple[str, str]],
    ) -> typing.Generator[
        tuple[tuple[str, str], list[tuple[str, str]]],
        None,
        None,
]:
    while event_list:
        rm = random.randint(0, len(event_list) - 1)
        event_list = event_list[:rm] + event_list[rm + 1:]
        yield event, event_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = []
    for i in range(10):
        event_list += [next(gen)]
    print("Built list of 10 events:", event_list)

    for event, remaining in consume_event(event_list):
        print("Got event from list:", event)
        print("Remains in list:", remaining)
