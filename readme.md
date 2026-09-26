\# Scientific *Calculator*



\## 1. Project Title



\*\*Scientific Calculator using Python\*\*



\## 2. Project Overview



This project is a simple scientific calculator made using Python. The calculator works in the command prompt and allows the user to perform different mathematical operations.



The program has a menu where the user can select the operation they want to perform. It uses different functions for different calculations.



The calculator can perform arithmetic operations as well as scientific calculations such as logarithm, trigonometric functions, power, root, factorial, and percentage.



\## 3. Features



\- Addition

\- Subtraction

\- Multiplication

\- Division

\- Power

\- Root

\- Logarithm

\- Sine

\- Cosine

\- Tangent

\- Factorial

\- Percentage

\- Basic error handling for division by zero and invalid logarithm input



\## 4. Technologies Used



\- Python 3

\- Python `math` module

\- Command Line / Terminal



No additional Python packages are required.



\## 5. Requirements



\- Python 3.x

\- Command Prompt or Terminal



\## 6. How to Run the Project



1\. Install Python 3 if it is not already installed.

2\. Save the program as `calculator.py`.

3\. Open Command Prompt or Terminal in the project folder.

4\. Run:



```bash

python calculator.py

```



5\. Enter `y` to continue and select an operation.

6\. Enter `n` to close the calculator.



\## 7. Working of the Project



When the program starts, it displays a list of available operations. The user selects an operation by entering its number. The program then asks for the required input values and calls the corresponding function.



For trigonometric calculations, the entered angle is converted from degrees to radians before using the `math` functions.



The program continues until the user chooses to close it.



\## 8. Testing



| Operation | Input | Expected Result |

|---|---|---|

| Addition | 10, 5 | 15 |

| Subtraction | 10, 5 | 5 |

| Multiplication | 10, 5 | 50 |

| Division | 10, 5 | 2 |

| Power | 2, 3 | 8 |

| Root | 16, 2 | 4 |

| Logarithm | 100 | 2 |

| Sine | 90 | 1 |

| Cosine | 0 | 1 |

| Tangent | 45 | 1 |

| Factorial | 5 | 120 |

| Percentage | 200, 10 | 20 |



\## 9. Error Handling



\- Division by zero displays an error.

\- Logarithm is calculated only for positive numbers.

\- Negative factorial input displays an error.

\- An invalid menu choice displays an error.

\- An input other than `y` or `n` at the continue prompt displays an error and stops the program.



\## 10. Project Structure



```text

Scientific-Calculator/

├── calculator.py

└── README.md

```



\## 11. Conclusion



The Scientific Calculator demonstrates Python functions, loops, conditional statements, user input, mathematical operators, and the `math` module. It is a simple menu-driven project for performing common and scientific calculations.



\## 12. Future Improvements



\- Add a graphical user interface.

\- Add calculation history.

\- Add more mathematical operations.

\- Improve input validation.

\- Add automated test cases.

\- Divide the program into multiple Python modules.



