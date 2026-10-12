# Data structure exercises – Software Engineering 1

Solutions to two exercises from
[python-data-structure-exercises](https://github.com/unigib/python-data-structure-exercises).

## exam_results.py

Asks for the mark of each subject and shows the matching grade.

- The marks are stored in a dictionary (`subject → mark`).
- For each mark, the program loops through `grade_boundaries` and finds the
  range where `minimum <= mark <= maximum`.

Run:

```
python exam_results.py
```

## radio_freq.py

Asks for the name of a radio station and shows its frequency.

- `fm_frequencies` maps `frequency → station name`, so the program loops
  through `.items()` and compares each value with the name entered.
- Done in two ways: directly with a loop, and with a function `getradio()`
  that returns the frequency.

Run:

```
python radio_freq.py
```
