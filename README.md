# Exam_Aviad
# Exam Project

This project includes modules for working with numbers and collections.

## Modules

### `numbers/simp.py`

This module provides simple functions for adding and subtracting two numbers.

- **add(x, y):** Returns the sum of two numbers.
- **subtract(x, y):** Returns the result of subtracting y from x.

### `numbers/comp.py`

This module includes functions for calculating the sum of digits and checking if a number is a palindrome.

- **sum_of_digits(num):** Returns the sum of the digits of a given number.
- **is_palindrome(num):** Returns `True` if the number is a palindrome; otherwise, returns `False`.

### `col.py`

Implements a custom `myzip` function for zipping two collections.

- **myzip(it1, it2):** Implements the zip function for two collections.

## How to Run

1. Activate the virtual environment: `venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on macOS/Linux).
2. Run the test script: `python test_script.py`.

## Usage

- Call functions in `numbers/simp.py` before using functions in `numbers/comp.py` to avoid exceptions.
- Explore the functionality of each module by referring to the respective module descriptions above.

## Contributing

Feel free to contribute to this project by reporting issues, suggesting enhancements, or submitting pull requests. Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -m "Your descriptive message here"`.
4. Push your changes to your fork: `git push origin feature/new-feature`.
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
