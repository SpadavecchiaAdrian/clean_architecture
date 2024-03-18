from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data) -> None:
        self.data = data

    def list(self):
        return [Room.model_validate(room) for room in self.data]
