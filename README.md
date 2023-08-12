## Project Name
A brief overview of the project, its purpose, and what it aims to achieve.
# overview
this project's goal  is to make a clone of the airbnb website; fullstack both frontend and backend.
# purpose
This project's purpose is to familiarise with the concepts of webstack development.
they are:
1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. A website (the front-end) that shows the final product to everybody: static and dynamic
3. A database or files that store data (data = objects)
4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
# objective
this project's objective is to help to create a strong foundation in fullstack engineering.




## Learning Objectives

At the end of this project, you are expected to be able to explain the following topics to anyone without the help of Google:

General:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. Copying and pasting someone else's work or any form of plagiarism is strictly forbidden.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it's a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- Your file organization in the tests folder should be the same as your project (e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py)
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

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

This README section provides an overview of how to use the `console.py` tool to manage AirBnB data models. For more details about available commands, you can use the `help` command within the console.

Remember that this tool is intended for development and testing purposes. Be cautious when using sensitive data and always validate your inputs.

## Contributing

If you wish to contribute to the project, explain the process for contributing, guidelines for code formatting, and how to submit pull requests.

Sure, here's a "Contact" section that you can add to your README:

---

## Contact

If you have any questions, feedback, or suggestions related to this project, feel free to reach out to us:

- **Kaleab Endrias**
  - GitHub: [kaleabgithub][(https://github.com/kaleabendriasgithub)]

- **Rafael John**
  - GitHub: [rafaeljohn][(https://github.com/rafaeljohn)]

We welcome your input and would be glad to assist you with any queries you may have!

---
