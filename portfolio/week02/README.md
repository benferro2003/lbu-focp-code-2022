# Programming Portfolio: Week 2

This folder contains *suggested solutions* to the programming exercises for this week. There are always many ways
to solve a problem, so many other correct solutions exist. There may well be others in the folders for individual
labs.

* `hello_name.py` is the canonical second program.
* `c_to_f.py` converts a temperature in Celsius to Fahrenheit.
* `lab_divider.py` calculates the number of lab groups needed for a group of students.
* `sweet_splitter.py` divides a tub of sweets between pupils (and is in fact exactly the same program as above!).


These programs are limited to using the programming ideas included
so far in the lectures and practicals, so in many cases more elegant
or maintainable solutions also exist.

The code is provided "as is", with no warranty, implied or otherwise.

## Advanced Corner

These programs mostly ignore some obvious and basic error conditions. First, the user might enter a value that is not
the expected type - something that cannot be converted to an integer for the number of students, for example. Second,
a value might be the correct type, but out of the valid range - obvious examples are a negative number of students (or 
sweets), or zero for the number of students (zero for the sweets would be OK, but disappointing).

This is fixed in `zz_lab_divider.py`. This program uses some new techniques with conditionals, loops, and some
exception handling. It just reports how many labs are needed (and gets the grammar right).

*A possibly interesting side-issue here is how we would validate that the answer in the first program really is
a name. (This is a well known interview questions for software developers!).*
