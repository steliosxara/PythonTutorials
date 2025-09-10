# Ερωτήσεις του κουίζ
questions_testing = [
  {
    "question": "Ποιο είναι το αποτέλεσμα της εντολής print(2 * 3);",
    "options": ["5", "6", "8", "9"],
    "answer": "6",
    "type": "MCS"
  },
  {
    "question": "Συμπληρώστε με 'yes' ή 'no' :<br>___<br>Συμπληρώστε με 'x' ή 'y' :<br>___",
    "answer": [["yes", "no"],["x", "y"]],
    "type": "SA"
  },
  {
    "question": "Ποιο είναι το αποτέλεσμα της εντολής print(2 ** 3);",
    "options": ["5", "6", "8", "9"],
    "answer": "8",
    "type": "MCS"
  }
]

questions = [
  {
    "question": "Ποιο είναι το αποτέλεσμα της εντολής print(2 ** 3);",
    "options": ["5", "6", "8", "9"],
    "answer": "8",
    "type": "MCS"
  },
  {
    "question": "Ποια λέξη-κλειδί χρησιμοποιείται για τον ορισμό συνάρτησης στην Python;",
    "options": ["func", "define", "def", "function"],
    "answer": "def",
    "type": "MCS"
  },
  {
    "question": "Τι κάνει η συνάρτηση len();",
    "options": ["Επιστρέφει το μήκος ενός αντικειμένου", "Προσθέτει δύο αριθμούς", "Εκτυπώνει έξοδο", "Μετατρέπει σε string"],
    "answer": "Επιστρέφει το μήκος ενός αντικειμένου",
    "type": "MCS"
  },
  {
    "question": "Ποιο από τα παρακάτω είναι έγκυρο όνομα μεταβλητής;",
    "options": ["2name", "name_2", "name-2", "name 2"],
    "answer": "name_2",
    "type": "MCS"
  },
  {
    "question": "Ποια είναι η σωστή κατάληξη αρχείου για αρχεία Python;",
    "options": [".pyth", ".pt", ".py", ".pyt"],
    "answer": ".py",
    "type": "MCS"
  }
]

# W3 Pyton Getting Started
questions_get_started = [
  {
    "question": "Ποια είναι η σωστή επέκταση αρχείου για τα αρχεία Python;",
    "options": [".pp", ".pt", ".py"],
    "answer": ".py",
    "type": "MCS"
  },
  {
    "question": "Ποια είναι η σωστή σύνταξη της γραμμής εντολών για να ελέγξετε αν η Python είναι εγκατεστημένη στον υπολογιστή σας; (Και επίσης για να ελέγξετε την έκδοση της Python);",
    "options": ["python --version", "python ##version", "python version"],
    "answer": "python --version",
    "type": "MCS"
  },
  {
    "question": "Ποια είναι η σωστή σύνταξη για την έξοδο από τη διεπαφή γραμμής εντολών της Python;",
    "options": ["stop()", "exit()", "end()"],
    "answer": "exit()",
    "type": "MCS"
  }
]

# W3 Python Syntax
questions_syntax = [
  {
    "question": "Σωστό ή Λάθος: Η εσοχή στην Python είναι μόνο για λόγους αναγνωσιμότητας.",
    "options": ["Σωστό", "Λάθος"],
    "answer": "Λάθος",
    "type": "MCS"
  },
  {
    "question": "Εισάγετε το τμήμα που λείπει από τον παρακάτω κώδικα για την έξοδο 'Hello World'.<br>___(\"Hello World\")",
    "answer": "print",
    "type": "SA"
  },
  {
    "question": "Συμπληρώστε το μπλοκ κώδικα, εκτυπώστε 'yes' εάν το 5 είναι μεγαλύτερο από το 2.<br>if 5 > 2:<br>___",
    "answer": [" print(\"yes\")", "  print(\"yes\")", "   print(\"yes\")", "  print(\"yes\")", " print(\'yes\')", "  print(\'yes\')", "   print(\'yes\')", "  print(\'yes\')"],
    "type": "SA"
  }
]

# W3 Python Comments
questions_comments = [
  {
    "question": "Ποιος χαρακτήρας χρησιμοποιείται για τον ορισμό ενός σχολίου Python:",
    "options": ["'", "//", "#", "/*"],
    "answer": "#",
    "type": "MCS"
  },
  {
    "question": "Τα σχόλια στην Python γράφονται με έναν ειδικό χαρακτήρα, ποιον;<br>___Αυτό είναι ένα σχόλιο",
    "answer": "#",
    "type": "SA"
  },
  {
    "question": "Χρησιμοποιήστε μια συμβολοσειρά πολλών γραμμών για να κάνετε ένα σχόλιο πολλών γραμμών:<br>___<br>Αυτό είναι ένα σχόλιο<br>γραμμένο σε<br>περισσότερες από μία γραμμές<br>___",
    "answer": [["'''", '"""'],["'''", '"""']],
    "type": "SA"
  }
]

# W3 Python Variables: Python Variables
questions_variables = [
  {
    "question": "Ποιος είναι ο σωστός τρόπος δήλωσης μιας μεταβλητής της Python;",
    "options": ["var x = 5", "#x = 5", "$x = 5", "x = 5"],
    "answer": "x = 5",
    "type": "MCS"
  },
  {
    "question": "Σωστό ή Λάθος:<br>Μπορείτε να δηλώσετε μεταβλητές συμβολοσειράς με απλά ή διπλά εισαγωγικά.<br><pre>x = \"John\"<br># είναι το ίδιο με<br>x = 'John'</pre>",
    "options": ["Σωστό", "Λάθος"],
    "answer": "Σωστό",
    "type": "MCS"
  },
  {
    "question": "<b>Σωστό ή Λάθος</b>:<br>Τα ονόματα των μεταβλητών δεν είναι ευαίσθητα σε πεζά και κεφαλαία.<br><pre>a = 5<br># είναι το ίδιο με<br>A = 5</pre>",
    "options": ["Σωστό", "Λάθος"],
    "answer": "Λάθος",
    "type": "MCS"
  },
  {
    "question": "Συμπληρώστε με τις σωστές συναρτήσεις (από τις πιο κάτω) για να εκτυπώσετε τον τύπο δεδομένων μιας μεταβλητής:<br><pre>___(___(myvar))<br></pre><br>ΕΠΙΛΟΓΕΣ: <code>print</code> <code>typ</code> <code>type</code> <code>var</code> <code>echo</code>",
    "answer": ["print", "type"],
    "type": "SA"
  },
]

# W3 Python Variables: Variable Names
questions_variable_names = [
  {
    "question": "Ποιο από τα παρακάτω ΔΕΝ είναι επιτρεπτό όνομα μεταβλητής;",
    "options": ["my-var = 20", "my_var = 20", "Myvar = 20", "_myvar = 20"],
    "answer": "my-var = 20",
    "type": "MCS"
  },
  {
    "question": 'Δημιουργήστε μια μεταβλητή με όνομα carname και εκχωρήστε της την τιμή Volvo.<br><pre>___ = ___<br></pre>',
    "answer": [["carname","carname "], ['"Volvo"',"'Volvo'"]],
    "type": "SA"
  },
  {
    "question": 'Δημιουργήστε μια μεταβλητή με όνομα x και εκχωρήστε της την τιμή 50.<br><pre>___ = ___<br></pre>',
    "answer": ["x", "50"],
    "type": "SA"
  },
]

# W3 Python Variables: Assign Multiple Values
questions_assign_multiple_values = [
  {
    "question": "Ποια είναι η σωστή σύνταξη για να προσθέσετε την τιμή 'Hello World', σε 3 μεταβλητές σε μία εντολή;",
    "options": ["x, y, z = 'Hello World'", "x = y = z = 'Hello World'", "x|y|z = 'Hello World'"],
    "answer": "x = y = z = 'Hello World'",
    "type": "MCS"
  },
  {
    "question": 'Εισάγετε τη σωστή σύνταξη για να εκχωρήσετε τιμές σε πολλαπλές μεταβλητές σε μία γραμμή:<br><pre>x___y___z = "Orange", "Banana", "Cherry"<br></pre>',
    "answer": [",", ","],
    "type": "SA"
  },
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<br><pre>fruits = ['apple', 'banana', 'cherry']<br>a, b, c = fruits<br>print(a):<br></pre>Ποιο θα είναι το αποτέλεσμα:",
    "options": ["apple", "banana", "cherry"],
    "answer": "apple",
    "type": "MCS"
  },
]

# W3 Python Variables: Output Variables
questions_output_variables = [
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<br><pre>print('Hello', 'World')<br></pre>Ποιο θα είναι το αποτέλεσμα που θα εκτυπωθεί;",
    "options": ["Hello, World", "Hello World", "HelloWorld"],
    "answer": "Hello World",
    "type": "MCS"
  },
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<br><pre>a = 'Hello'<br>b = 'World'<br>print(a + b)<br></pre>Ποιο θα είναι το αποτέλεσμα:",
    "options": ["a + b",  "Hello World", "HelloWorld"],
    "answer": "HelloWorld",
    "type": "MCS"
  },
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<br><pre>a = 4<br>b = 5<br>print(a + b)<br></pre>Ποιο θα είναι το αποτέλεσμα:",
    "options": ["45",  "9", "4+5"],
    "answer": "9",
    "type": "MCS"
  },
]

# W3 Python Variables: Global Variables
questions_global_variables = [
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<pre>x = 'awesome'<br>def myfunc():<br>&#9;x = 'fantastic'<br>myfunc()<br>print('Python is ' + x)</pre>Ποιο θα είναι το αποτέλεσμα που θα εκτυπωθεί;",
    "options": ["Python is awesome", "Python is fantastic"],
    "answer": "Python is awesome",
    "type": "MCS"
  },
  {
    "question": "Εισάγετε τη σωστή λέξη-κλειδί για να κάνετε τη μεταβλητή <code>x</code> να ανήκει στην καθολική εμβέλεια.<br><pre>def myfunc():<br>&#9;___ x<br>&#9;x = 'fantastic'</pre>",
    "answer": "global",
    "type": "SA"
  },
  {
    "question": "Εξετάστε τον ακόλουθο κώδικα:<pre>x = 'awesome'<br>def myfunc():<br>&#9;global x<br>&#9;x = 'fantastic'<br>myfunc()<br>print('Python is ' + x)</pre>Ποιο θα είναι το αποτέλεσμα που θα εκτυπωθεί;",
    "options": ["Python is awesome", "Python is fantastic"],
    "answer": "Python is fantastic",
    "type": "MCS"
  },
]

# W3 Python Data Types
questions_data_types = [
  {
    "question": "Αν x = 5, ποια είναι η σωστή σύνταξη για την εκτύπωση του τύπου δεδομένων της μεταβλητής x;",
    "options": ["print(dtype(x))", "print(type(x))", "print(x.dtype())"],
    "answer": "print(type(x))",
    "type": "MCS"
  },
  {
    "question": "Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = 5<br>print(type(x))<br>___",
    "answer": ["<class 'int'>", "int"],
    "type": "SA"
  },
  {
    "question": 'Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = "Hello World"<br>print(type(x))<br>___',
    "answer": ["<class 'str'>", "str"],
    "type": "SA"
  },
  {
    "question": "Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = 20.5<br>print(type(x))<br>___",
    "answer": ["<class 'float'>", "float"],
    "type": "SA"
  },
  {
    "question": 'Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = ["apple", "banana", "cherry"]<br>print(type(x))<br>___',
    "answer": ["<class 'list'>", "list"],
    "type": "SA"
  },
  {
    "question": 'Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = ("apple", "banana", "cherry")<br>print(type(x))<br>___',
    "answer": ["<class 'tuple'>", "tuple"],
    "type": "SA"
  },
  {
    "question": 'Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = {"apple", "banana", "cherry"}<br>print(type(x)<br>___',
    "answer": ["<class 'dict'>", "dict"],
    "type": "SA"
  },
  {
    "question": 'Το ακόλουθο παράδειγμα κώδικα θα εκτύπωνε τον τύπο δεδομένων του x, ποιος τύπος δεδομένων θα ήταν αυτός;<br>x = True<br>print(type(x))<br>___',
    "answer": ["<class 'bool'>", "bool"],
    "type": "SA"
  },
]

# W3 Python Numbers
questions_numbers = [
  {
    "question": "Ο οποίος ΔΕΝ είναι νόμιμος αριθμητικός τύπος δεδομένων στην Python:",
    "options": ["int", "long", "float"],
    "answer": "long",
    "type": "MCS"
  },
  {
    "question": "Εισάγετε τη σωστή σύνταξη για τη μετατροπή του x σε αριθμό κινητής υποδιαστολής.<br>x  = 5<br>x = ___(x)",
    "answer": ["float"],
    "type": "SA"
  },
  {
    "question": "Εισάγετε τη σωστή σύνταξη για τη μετατροπή του x σε ακέραιο.<br>x  = 5.5<br>x = ___(x)",
    "answer": ["int"],
    "type": "SA"
  },
  {
    "question": "Εισάγετε τη σωστή σύνταξη για τη μετατροπή του x σε μιγαδικό.<br>x  = 5<br>x = ___(x)",
    "answer": ["complex"],
    "type": "SA"
  },
]

# W3 Python Casting
questions_casting = [
  {
    "question": "Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:<br>print(int(35.88))",
    "options": ["35", "35.88", "36"],
    "answer": "35",
    "type": "MCS"
  },
  {
    "question": "Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:<br>print(float(35))",
    "options": ["35", "35.0", "0.35"],
    "answer": "35.0",
    "type": "MCS"
  },
  {
    "question": "Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:<br>print(str(35.82))",
    "options": ["35", "35.8", "35.82"],
    "answer": "35.82",
    "type": "MCS"
  },
]

# W3 Python Strings: Python Strings
questions_strings = [
  {
    "question": "Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:<pre>x = 'Welcome'<br>print(x[3])</pre>",
    "options": ["Wel", "c", "Welcome Welcome Welcome"],
    "answer": "c",
    "type": "MCS"
  },
  {
    "question": '''Χρησιμοποιήστε τη συνάρτηση <code>len</code> για να εκτυπώσετε το μήκος της συμβολοσειράς.
<pre>
x = "Hello World"
print(___)
</pre>''',
    "answer": ["len(x)"],
    "type": "SA"
  },
  {
    "question": 'Λάβετε τον πρώτο χαρακτήρα της συμβολοσειράς txt.<br><pre>txt = "Hello World"<br>x = ___</pre>',
    "answer": ["txt[0]"],
    "type": "SA"
  },
  {
    "question": '''Εισάγετε τη σωστή λέξη-κλειδί για να ελέγξετε αν η λέξη «free» υπάρχει στο κείμενο:
<pre>
txt = 'The best things in life are free!'
if 'free' ___ txt:
    print('Yes, free is present in the text.')
</pre>
<b>ΕΠΙΛΟΓΕΣ:</b> <code>contains</code> <code>present</code> <code>in</code> <code>match</code>''',
    "answer": ["in"],
    "type": "SA"
  },
]

# W3 Python Strings: Slicing Strings
questions_slicing_strings = [
  {
    "question": '''Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:
<pre>
x = 'Welcome'
print(x[3:5])
</pre>
''',
    "options": ["lcome", "come", "com", "co"],
    "answer": "co",
    "type": "MCS"
  },
  {
    "question": '''Get the characters from index 2 to index 4 (llo).
<pre>
txt = "Hello World"
x = ___
</pre>
''',
    "answer": ["txt[2:5]", "txt[2:-6]", "txt[-9:5]", "txt[-9:-6]"],
    "type": "SA"
  },
  {
    "question": '''Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:
<pre>
x = 'Welcome'
print(x[3:])
</pre>
''',
    "options": ["lcome", "come", "com", "co"],
    "answer": "come",
    "type": "MCS"
  },
]

# W3 Python Strings: Python Strings: Modify Strings
questions_modify_strings = [
  {
    "question": "Ποια είναι η σωστή σύνταξη για την εκτύπωση μιας συμβολοσειράς με κεφαλαία γράμματα;",
    "options": ["'Welcome'.upper()", "'Welcome'.toUpper()", "'Welcome'.toUpper()"],
    "answer": "'Welcome'.upper()",
    "type": "MCS"
  },
  {
    "question": 'Να συμπληρωθεί ο κώδικας ώστε το <code>x</code> να περιέχει τη συμβολοσειρά <code>txt</code> χωρίς κενά στο αρχή ή στο τέλος:<br><pre>txt = " Hello World "<br>x = ___</pre>',
    "answer": "txt.strip()",
    "type": "SA"
  },
  {
    "question": 'Μετατρέψτε την τιμή του <code>txt</code> σε κεφαλαία γράμματα.<br><pre>txt = "Hello World"<br>txt = ___</pre>',
    "answer": "txt.upper()",
    "type": "SA"
  },
  {
    "question": 'Μετατρέψτε την τιμή του <code>txt</code> σε πεζά γράμματα.<br><pre>txt = "Hello World"<br>txt = ___</pre>',
    "answer": "txt.lower()",
    "type": "SA"
  },
  {
    "question": 'Αντικαταστήστε τον χαρακτήρα <code>H</code> με ένα <code>J</code>.<br><pre>txt = "Hello World"<br>txt = txt.___(___, ___)</pre>',
    "answer": [["replace"], ['"H"', "'H'"], ['"J"', "'J'"]],
    "type": "SA"
  },
]

# W3 Python Strings: String Concatenation
questions_string_concatenation = [
  {
    "question": "Ποια είναι η σωστή σύνταξη για να συγχωνεύσετε τις μεταβλητές <code>x</code> και <code>y</code> στη μεταβλητή <code>z</code>;",
    "options": ["<code>z = x, y</code>", "<code>z = x = y</code>", "<code>z = x + y</code>"],
    "answer": "<code>z = x + y</code>",
    "type": "MCS"
  },
  {
    "question": '''Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:
<pre>
x = 'Welcome'
y = 'Coders'
print(x + y)
</pre>''',
    "options": ["Welcome Coders", "WelcomeCoders", "Welcome<br>Coders"],
    "answer": "WelcomeCoders",
    "type": "MCS"
  },
  {
    "question": '''Εξετάστε τον παρακάτω κώδικα:
<pre>
a = 'Join'
b = 'the'
c = 'party'
</pre>
Ποια είναι η σωστή σύνταξη για την εκτύπωση του 'Join the party';''',
    "options": ["<code>print(a + b + c)</code>", "<code>print(a + ' ' + b + ' ' + c)</code>", "<code>print(a b c)</code>"],
    "answer": "<code>print(a + ' ' + b + ' ' + c)</code>",
    "type": "MCS"
  },
]

# W3 Python Strings: Format Strings
questions_format_strings = [
  {
    "question": "Αν <code>x = 9</code>, ποια είναι η σωστή σύνταξη για να εκτυπωθεί «Η τιμή είναι 9.00 δολάρια»;",
    "options": ["<code>print(f'Η τιμή είναι {x:.2f} δολάρια')</code>", "<code>print(f'Η τιμή είναι {x:2} δολάρια')</code>", "<code>print(f'Η τιμή είναι {x:format(2)} δολάρια')</code>"],
    "answer": "<code>print(f'Η τιμή είναι {x:.2f} δολάρια')</code>",
    "type": "MCS"
  },
  {
    "question": '''Εισάγετε τη σωστή σύνταξη για να προσθέσετε ένα τοποτηρητή για την παράμετρο age:
<pre>
age = 36
txt = f"My name is John, and I am ___"
print(txt)
</pre>''',
    "answer": "{age}",
    "type": "SA"
  },
  {
    "question": """Ποιο θα είναι το αποτέλεσμα του ακόλουθου κώδικα:<pre>
print(f'Η τιμή είναι {2 + 3} δολάρια'):</pre>""",
    "options": ["Η τιμή είναι 23 δολάρια", "Η τιμή είναι 5 δολάρια", "Η τιμή είναι {2 + 3} δολάρια", "Η τιμή είναι 6 δολάρια"],
    "answer": "Η τιμή είναι 5 δολάρια",
    "type": "MCS"
  },
]

# W3 Python Strings: Escape Characters
questions_escape_characters  = [
  {
    "question": "Ερώτηση πολλαπλών απαντήσεων:",
    "options": ["επιλογή1", "επιλογή2", "επιλογή3", "επιλογή4"],
    "answer": "επιλογή2",
    "type": "MCS"
  },
  {
    "question": "Ερώτηση συμπλήρωσης κενού: ___",
    "answer": "απάντηση",
    "type": "SA"
  },
]

# W3 Python Strings: String Methods
# W3 Python Strings: String Exercises

# W3 Python TEMPLATE
questions_section = [
  {
    "question": "Ερώτηση πολλαπλών απαντήσεων:",
    "options": ["επιλογή1", "επιλογή2", "επιλογή3", "επιλογή4"],
    "answer": "επιλογή2",
    "type": "MCS"
  },
  {
    "question": "Ερώτηση συμπλήρωσης κενού: ___",
    "answer": "απάντηση",
    "type": "SA"
  },
  {
    "question": "Συμπλήρωση κενού (με εναλλακτική απαν): ___",
    "answer": ["απάντηση", "εναλλακτική"],
    "type": "SA"
  },
  {
    "question": "Συμπλήρωση δύο κενών: ένα ___ άλλο ___",
    "answer": ["απάντηση1", "απάντηση2"],
    "type": "SA"
  },
  {
    "question": "Συμπλήρωση κενών (εναλ απα): ένα ___ άλλο ___",
    "answer": [["απάντηση1", "εναλ1"], ["απάντηση2", "εναλ2"]],
    "type": "SA"
  },
]