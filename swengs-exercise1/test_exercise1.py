import pytest
import traceback
import exercises as ex

movie_title = "Blade runner 2049"

def test_count_characters():  
    assert ex.count_characters(movie_title) == 17

def test_first_three_letters():
    assert ex.first_three_letters(movie_title) == "Bla"

def test_last_three_letters():
    assert ex.last_three_letters(movie_title) == "049"

def test_split_words():
    assert ex.split_words(movie_title) == ["Blade", "runner", "2049"]

def test_replace():
    assert ex.replace(movie_title, "2049", "2051") == "Blade runner 2051"

def test_normalize_1():
    assert ex.normalize(movie_title, 1) == "blade runner 2049"

def test_normalize_2():
    assert ex.normalize(movie_title, 2) == "BLADE RUNNER 2049"

def test_normalize_3():
    assert ex.normalize(movie_title, 3) == "Blade runner 2049"

def test_normalize_4():
    with pytest.raises(ValueError, match='Invalid mode'):
        ex.normalize(movie_title, 4)

def test_find_title_1(): 
    assert ex.find_title(["Blade runner", "Star trek", "staR wars"], "Star") == ["Star trek", "staR wars"]

def test_find_title_2():
    assert ex.find_title(["Blade runner", "Star trek", "staR wars"], "test") == []

def test_calculate_mean_1():
    assert ex.calculate_mean([8, 4, 10, 2]) == 6.0

def test_calculate_mean_2():
    assert ex.calculate_mean([]) == None

def test_min_mean_max_1():
    assert ex.min_mean_max([8, 4, 10, 2]) == (2, 6.0, 10)

def test_min_mean_max_2():
    assert ex.min_mean_max([]) == None

avg_temperatures = [
        (1, 12),
        (2, 10),
        (3, 14),
        (4, 16),
        (5, 17),
        (6, 20),
        (7, 29),
        (8, 30),
        (9, 22),
        (10, 18),
        (11, 14),
        (12, 10)
    ]

def test_mean_temperature_1():
    assert ex.mean_temperature(avg_temperatures) == 17.7

def test_mean_temperature_2():
    assert ex.mean_temperature([]) ==  None

string1 = "Los Angeles is bigger than Berlin but Berlin is older than Los Angeles ."

wc_count = {
    'Los': 2,
    'Angeles': 2,
    'is': 2,
    'bigger': 1,
    'than': 2,
    'Berlin': 2,
    'but': 1,
    'older': 1,
    '.': 1
    }

most_common_words = ["Los","Angeles","is","than","Berlin"]

def test_word_count():
    assert ex.word_count(string1) ==  wc_count

def test_common_words():
    assert ex.common_words(string1) == most_common_words