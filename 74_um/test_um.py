from um import count


def test_count_word():
    assert count("") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um um um") == 3

def test_count_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2