import pytest
from src.project import analyze_text


@pytest.fixture
def file_path(tmp_path):
    def create_file(content, file_name="test.txt"):
        file_path = tmp_path / file_name
        file_path.write_text(content, encoding="utf-8")
        return file_path
    return create_file


# ✅ @pytest.mark.parametrize — тільки на тестовій функції, НЕ на фікстурі
# ✅ Перший аргумент — рядок з іменами через кому
@pytest.mark.parametrize(
    "content, words_count, sentences_count",
    [
        ("This is a test data. We are testing, you know that, right?", 12, 2),
        ("Hi, just, checking, marks. Yeah? Ofc! Oh no...", 8, 4),
        ("This is a simple , puncuation position ,test", 7, 0),
        ("Okay, lets test something normal? I guess it should work, please?", 11, 2),
        ("I'm tired of writing these, not even joking here.", 9, 1),
    ],
)
def test_text_analyzer(file_path, content, words_count, sentences_count):
    # ✅ Передаємо content у фікстуру
    file = file_path(content)
    words, sentences = analyze_text(file)
    assert words == words_count
    assert sentences == sentences_count
