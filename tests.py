import pytest
@pytest.fixture
def question_with_choices():
    question = Question(title='Python', max_selections=2)

    question.add_choice('Python é uma linguagem', True)
    question.add_choice('Python é compilada exclusivamente', False)
    question.add_choice('Python suporta orientação a objetos', True)

    return question

from model import Question

def test_correct_selected_choices_with_fixture(question_with_choices):
    result = question_with_choices.correct_selected_choices([1, 2])
    assert result == [1]


def test_remove_choice_with_fixture(question_with_choices):
    question_with_choices.remove_choice_by_id(2)
    assert len(question_with_choices.choices) == 2




def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

 
def test_add_choice_returns_created_choice():
    question = Question(title='q1')

    choice = question.add_choice('Alternative A', True)

    assert choice.text == 'Alternative A'
    assert choice.is_correct
    assert choice.id == 1


def test_add_multiple_choices_assigns_different_ids():
    question = Question(title='q1')

    choice1 = question.add_choice('Alternative A')
    choice2 = question.add_choice('Alternative B')

    assert choice1.id != choice2.id
    assert choice2.id == choice1.id + 1


def test_remove_choice_by_id():
    question = Question(title='q1')
    choice1 = question.add_choice('Alternative A')
    question.add_choice('Alternative B')

    question.remove_choice_by_id(choice1.id)

    assert len(question.choices) == 1
    assert question.choices[0].text == 'Alternative B'


def test_remove_choice_with_invalid_id():
    question = Question(title='q1')
    question.add_choice('Alternative A')

    with pytest.raises(Exception):
        question.remove_choice_by_id(99)


def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('Alternative A')
    question.add_choice('Alternative B')

    question.remove_all_choices()

    assert question.choices == []


def test_set_correct_choices():
    question = Question(title='q1')
    choice1 = question.add_choice('Alternative A')
    choice2 = question.add_choice('Alternative B')
    choice3 = question.add_choice('Alternative C')

    question.set_correct_choices([choice2.id])

    assert not choice1.is_correct
    assert choice2.is_correct
    assert not choice3.is_correct


def test_correct_selected_choices_returns_correct_answers():
    question = Question(title='q1', max_selections=2)
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', True)

    assert question.correct_selected_choices([1, 2]) == [2]


def test_correct_selected_choices_with_no_correct_answers():
    question = Question(title='q1')
    choice1 = question.add_choice('Alternative A', False)

    result = question.correct_selected_choices([choice1.id])

    assert result == []


def test_correct_selected_choices_exceeds_max_selections():
    question = Question(title='q1', max_selections=1)
    choice1 = question.add_choice('Alternative A')
    choice2 = question.add_choice('Alternative B')

    with pytest.raises(Exception):
        question.correct_selected_choices([choice1.id, choice2.id])


def test_create_choice_with_invalid_text():
    question = Question(title='q1')

    with pytest.raises(Exception):
        question.add_choice('')

    with pytest.raises(Exception):
        question.add_choice('a' * 101)
 
 