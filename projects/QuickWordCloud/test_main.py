from main import QuickWordCloud
from unittest.mock import patch, mock_open


def test_create_word_and_counts():
    mock_file_content = "hello testing testing"
    mock_file_path = "/data/mock_file"
    with patch(
        "builtins.open", new=mock_open(read_data=mock_file_content)
    ) as mock_file:
        qw = QuickWordCloud(mock_file_path)
        actual_words = qw.extract_words()
        assert actual_words.strip() == mock_file_content.strip()
