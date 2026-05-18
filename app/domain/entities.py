class Event:
    def __init__(self, event_id: int, start_timestamp: int, end_timestamp: int, title: str, description: str):
        self.id  = event_id
        self.title = title
        self.start_at = start_timestamp
        self.end_at   = end_timestamp
        self.description = description

    @classmethod
    def create(cls, event_id: int, start_timestamp: int, end_timestamp: int, title: str, description: str):
        return cls(event_id, start_timestamp, end_timestamp, title, description)

    def __str__(self):
        return (f'id: {self.id} \n'
                f'title: {self.title} \n'
                f'start_at: {self.start_at}\n'
                f'end_at: {self.end_at}')
