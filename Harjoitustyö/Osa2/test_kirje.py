from kirje import Kirje, KirjeDetails

print("Show mock list of messages in streamlined style:")
mock_list_details = KirjeDetails(
    content="1 - example\n2 - tomorrow",
    header_separation=" - ",
    headers={
        'ID': 'Title',
        'Title': ' notes '
    }
)
mock_list = Kirje(mock_list_details)
mock_list.display("streamlined")
print("")

#############################
from kirje import Kirje, KirjeDetails

print("Show mock note in default style:")
mock_list_details = KirjeDetails(
    content="eat\nstudy\nsleep",
    header_separation=" - ",
    headers={
        'ID': 2,
        'Title': ' tomorrow '
    }
)
mock_list = Kirje(mock_list_details)
mock_list.display("default")