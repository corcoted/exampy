# Exampy
python script for generating randomized exams with output to LaTeX

(c) 2023 Ted Corcovilos

## Contents
- `exampy.py` - The python script itself (see below)
- `header1.tex` - Preamble for the output `.tex` files.  Put packages, formatting, etc. here.
- `header2.tex` - Opening pages of the exam (cover sheet, etc.)
- `footer.tex` - Closing pages of the exam (reference material etc.)
- `figs/` - folder for storing figures
- `environment.yml` - conda python environment file containing suggested packages
  - Use these steps to create and activate the environment:
    - `conda env create -f environment.yml -p ./env`
    - `conda activate ./env`
    - optional: register the kernel
- `.latexmkrc` - suggested `latexmk` configuration

## To use
- Customize the provided `.tex` file: `header1.tex`, `header2.tex`, and `footer.tex`.
- Configure `exampy.py`
  - `fileprefix` is a string for the output filename prefix
  - `examlist` is a list of exam version.  Each element of the list is pair containing a string for the version name and an integer for the random seed for that version (to ensure the same results if the script is re-run).
  - Various strings that need to be defined are included as "XXX".  Search for that string to find and update these. These are things like the course name and exam date.  Many of these are in `headertext`.
  - `question_groups` is a nested list of groups of questions to keep together during randomization (e.g. all of the questions on a single topic).
- The exam questions are in `exampy.py`, starting around line 105.  Each question consists of the following strings:
  - `qtext` - the text of the question
  - `thisalist` - a list of strings containing the answer choices.  *The first list item is the correct answer* and the other items are the distractors.
  - These strings are raw LaTeX text.  The may include calculated values using python formatted strings.
  - Each question block in the code should end with `addquestion(qtext,thisalist)`.