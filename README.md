# Project Name: Learning Python Package Development

## Learning Objectives

At the completion of this project, you will have gained a solid understanding of various fundamental concepts in Python package development. You will be able to explain these concepts without relying on external sources:

### General Concepts

1. How to create a Python package.
2. Creating a command interpreter in Python using the `cmd` module.
3. Understanding and implementing Unit testing in a larger project.
4. Serialization and deserialization of a Class.
5. Reading and writing JSON files.
6. Managing datetime in Python.
7. Understanding the purpose of UUIDs.
8. Understanding and using `*args` to pass variable-length arguments to functions.
9. Understanding and using `**kwargs` to pass keyword arguments to functions.
10. Handling named arguments effectively in function definitions.

### Copyright and Plagiarism

- Understand the importance of producing original work.
- Avoid plagiarism by solving project tasks independently.
- Abide by the program's rules and regulations regarding plagiarism.

## Requirements

### Python Scripts

- Use editors such as vi, vim, or emacs.
- Code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All code files should end with a new line.
- The first line of all code files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should adhere to the `pycodestyle` (version 2.8.*) style guide.
- All code files must be executable.
- Code file lengths will be evaluated using the `wc` command.
- Modules should have proper documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- Classes should have proper documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- Functions (inside and outside a class) should have proper documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).

### Python Unit Tests

- Use editors such as vi, vim, or emacs.
- All test files should end with a new line.
- Test files should be inside a folder named `tests`.
- The `unittest` module should be used for writing tests.
- Test files should be Python files (extension: `.py`).
- Test file names and folders should start with `test_`.
- Test file organization within the `tests` folder should match the project structure.
  - For example, for `models/base_model.py`, unit tests must be in `tests/test_models/test_base_model.py`.
- Run all tests using `python3 -m unittest discover tests`.
- Modules should have proper documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- Classes should have proper documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- Functions (inside and outside a class) should have proper documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).

### Collaboration

- Collaborate on test cases to ensure edge cases are considered.

**Note:** It's essential to abide by the guidelines and work independently to produce original solutions. Plagiarism is strictly prohibited and will result in removal from the program.

## How to Use This Repository

1. Clone the repository to your local machine.
2. Navigate to the root folder of the project.
3. Review and implement the learning objectives and concepts as outlined in the tasks and requirements.
4. Use the provided `pycodestyle` guidelines for maintaining code style.
5. Create and document tests in the `tests` folder using the `unittest` module.
6. Run all tests using `python3 -m unittest discover tests`.
7. Document your code effectively to explain its purpose and functionality.
8. Ensure your code adheres to the project's requirements and guidelines.

Certainly! Here's a README section that explains how to use the `console.py` command-line tool:

---

## Using the Console.py Command-Line Tool

The `console.py` script is a command-line interface (CLI) that provides an interactive environment to interact with the AirBnB data models. With this tool, you can create, update, delete, and retrieve instances of various classes.

### Getting Started

1. Clone the AirBnB repository:
   ```bash
   git clone https://github.com/kaleabendrias/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Make sure you have Python 3.x installed on your system.

### Launching the Console

To start the console, run the following command in your terminal from the project directory:
```bash
./console.py
```

You will see a prompt `(hbnb)` indicating that the console is active and ready to accept commands.

### Available Commands

The console supports several commands that you can use to manage and interact with the data models. Here are some of the key commands:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <instance_id>`: Display information about a specific instance.
- `destroy <class_name> <instance_id>`: Delete a specific instance.
- `all [class_name]`: Display information about all instances or instances of a specific class.
- `update <class_name> <instance_id> <attribute_name> "<attribute_value>"`: Update an attribute of a specific instance.
- `<class_name>.<command>()`: Execute custom class-specific commands. (e.g., `User.count()`)

### Examples

1. Creating an instance:
   ```bash
   (hbnb) create User
   ```

2. Displaying instance information:
   ```bash
   (hbnb) show User 1234-5678-9012
   ```

3. Deleting an instance:
   ```bash
   (hbnb) destroy User 1234-5678-9012
   ```

4. Displaying all instances of a class:
   ```bash
   (hbnb) all User
   ```

5. Updating an instance's attribute:
   ```bash
   (hbnb) update User 1234-5678-9012 email "new@email.com"
   ```

6. Using custom class-specific commands:
   ```bash
   (hbnb) User.count()
   ```

### Exiting the Console

To exit the console, you can use the `quit` command or press `Ctrl + D`.

---

Sure, here's a "Contact" section that you can add to your README:

---

## Contact

If you have any questions, feedback, or suggestions related to this project, feel free to reach out to us:

- **Kaleab Endrias**
  - GitHub: [kaleabgithub](https://github.com/kaleabendrias)

- **Rafael John**
  - GitHub: [rafaeljohn](https://github.com/RafaelJohn9)

We welcome your input and would be glad to assist you with any queries you may have!

---

This README section provides an overview of how to use the `console.py` tool to manage AirBnB data models. For more details about available commands, you can use the `help` command within the console.

Remember that this tool is intended for development and testing purposes. Be cautious when using sensitive data and always validate your inputs.

Remember that the key to this project is not just achieving the tasks but truly understanding the concepts and gaining hands-on experience with Python package development. Happy coding!

