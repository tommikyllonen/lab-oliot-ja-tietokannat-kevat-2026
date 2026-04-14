from model_note import NoteDAO


def test_addNote():
    NoteDAO.addNote("title_here", "content_here")
    NoteDAO.addNote("TestTitle", "test_content")
    notes = NoteDAO.getNotes()
    for note in notes:
        print(note)

test_addNote()