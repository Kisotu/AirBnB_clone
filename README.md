## Concepts

For this project, we expect you to look at these concepts:

[Python packages](https://intranet.alxswe.com/concepts/66)

[AirBnB clone](https://intranet.alxswe.com/concepts/74)

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9dc5be172b9194da97d15f5db1bb226b6b0e9a20f24f2e758cfd43118685e23)

## Background Context
Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    create the first abstracted storage engine of the project: File storage.
    create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    *Create a new object (ex: a new User or a new Place)
    *Retrieve an object from a file, a database etc…
    *Do operations on objects (count, compute stats, etc…)
    *Update attributes of an object
    *Destroy an object

## Resources

Read or watch:

[cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)

[cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)

packages concept page

[uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)

[datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)

[unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)

[args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)

[Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)

[cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)

[python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    How to create a Python package
    How to create a command interpreter in Python using the cmd module
    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    How to manage datetime
    What is an UUID
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function

Copyright - Plagiarism

    You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
    You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
    You are not allowed to publish any content of this project.
    Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start by test_
    Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case

GitHub

There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.
More Info
Execution

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![structure of arbnb system](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=80bcc89f74b60f41cb5ec58f735035971e56a61a00d7f0dc399d928707809705)

[Video library(8 total)](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=264746d4e83bd32c283e94c2cf7997e5583e19601b0fbcb490c76fb14c5c1479)

[HBNB project overview](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=53fd22029ae89909c3ba4fd9533c0495985987cd44d38000facd90c9b8602a75)

[HBNB - the console](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d61d93be32862fa0818bd7854793bf3630a546a83bfb9294e9c3c30aa2d32a6)

[Python: Unique Identifier](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=120ece645df997499339d110fafdbc5bd4286d3143752519fd3d49d71bc4215b)

[Python: Unittests](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=99777dc85d0aad899ccbf5b30521644dae6ef096304b44d850b89d671e70434d)

[Python: BaseModel and inheritance](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=9c7fc4119b01234576c53adc25dd39bf6c19cac0be037b1df65e78b4c396a287)

[Code consistency](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=116a7d6bbb5008fdf80c64f7d69c813400bcb58600403c262ed367083b9e4dbd)

[Python: Modules and Packages](https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd.jpg?response-content-disposition=attachment%3B&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T170219Z&X-Amz-Expires=14400&X-Amz-SignedHeaders=host&X-Amz-Signature=d8d0a05be2d44340029af183ab7fddee14de0baacc075f333c68ae13ed5b11de)

