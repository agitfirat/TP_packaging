from __future__ import annotations

import tempfile

import pytest
from hypothesis import given, strategies as st

from ng20lda.core.utils import count_lines_from_file, count_lines_from_string


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("hello", 1),
        ("hello\nworld", 2),
        ("hello\nworld\n", 2),
    ],
)
def test_count_lines_from_string(text: str, expected: int) -> None:
    assert count_lines_from_string(text) == expected


#@given(
    #lines=st.lists(st.text(min_size=0, max_size=10), max_size=10),
    #add_trailing_newline=st.booleans(),
#)
#def test_count_lines_from_file_hypothesis(lines: list[str], add_trailing_newline: bool) -> None:
#    text = "\n".join(lines)
#   if add_trailing_newline and lines:
#        text = f"{text}\n"
#    elif add_trailing_newline and not lines:
#        text = "\n"

#    expected = len(text.splitlines())

#    with tempfile.NamedTemporaryFile(mode="w", delete=True, suffix=".txt", encoding = "utf-8") as tmp:
#        tmp.write(text)
#        tmp.flush()
#        assert count_lines_from_file(tmp.name) == expected
