from app.domain.entities import Event

def test_event_creation_valid_data():
    event_id = 10
    start_at = 1718895600
    end_at = 1718899200
    title = 'test_title'
    description = 'test_description'

    event = Event.create(event_id = event_id, start_timestamp = start_at, end_timestamp = end_at, title = title, description = description)
    assert event.id == event_id
    assert event.start_at == start_at
    assert event.end_at == end_at
    assert title == title
    assert description == description

