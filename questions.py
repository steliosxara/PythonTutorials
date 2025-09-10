import ipywidgets as widgets
from IPython.display import display

# Create a radio button for Ε1
question1 = widgets.RadioButtons(
    options=[
        ('.pp', 'A'),
        ('.pt', 'B'),
        ('.py', 'C'),
    ],
    description='Ε1: Ποια είναι η σωστή επέκταση αρχείου για τα αρχεία Python;',
    value=None
)
def show_q1():
    display(question1)
def get_answer_q1():
    return question1.value
def test_answer_q1():
    assert get_answer_q1() == 'C'

# Create a radio button for Ε2
question2 = widgets.RadioButtons(
    options=[
        ('python --version', 'A'),
        ('python ##version', 'B'),
        ('python version', 'C'),
    ],
    description='Ε2: Ποια είναι η σωστή σύνταξη της γραμμής εντολών για να ελέγξετε αν η python είναι εγκατεστημένη στον υπολογιστή σας; (Και επίσης για να ελέγξετε την έκδοση της Python);',
    value=None
)
def show_q2():
    display(question2)
def get_answer_q2():
    return question2.value
def test_answer_q2():
    assert get_answer_q2() == 'A'

# Create a radio button for Ε3
question3 = widgets.RadioButtons(
    options=[
        ('stop()', 'A'),
        ('exit()', 'B'),
        ('end()', 'C'),
    ],
    description='Ε3: Ποια είναι η σωστή σύνταξη για την έξοδο από τη διεπαφή γραμμής εντολών της Python;',
    value=None
)
def show_q3():
    display(question3)
def get_answer_q3():
    return question3.value
def test_answer_q3():
    assert get_answer_q3() == 'B'
