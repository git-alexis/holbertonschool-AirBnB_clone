# AirBnB clone - The console

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240308%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240308T120245Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4121b0470eafe8e596bc364cc3db123977ea47a0f71207b94971fe375ffc5684)

Welcome to the AirBnB Clone Console! This console serves as the command-line interface for managing various aspects of our AirBnB clone project.

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240308%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240308T120245Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a34a39c1db3a99095ce0ded57d612e056cf43b4f729b67b6ae3dff7b544ade2)

## Getting Started
To get started, follow these steps:

Run the command interpreter:

```
./console
```

If all goes well, you should see the following prompt:
`(hbtn)`
Now you're ready to use the console. Refer to the list of available commands below for further instructions.

## Command	

Commands can also be used in the following format:

| Command| Description| Usage |
| -------- | -------- | -------- |
| all    | Print all instances of a given class | `all <class_name> `  |
| create  | Create a new instance of a given class   | `create <class_name>`   |
| show    | Print the string representation of an instance	show   | `show <class_name> <id>`  |
| count    | Count the number of instances of a class | `count <class_name> ` |
| update    | Update an instance with new attribute values	update | `update <class name> <id> <attribute name> "<attribute value>" `|
| destroy    | Delete an instance based on ID   | `destroy <class_name> <id>`  |
| quit    | Quit the console   |` quit ` |

## Classes

### BaseModel
The BaseModel class serves as the base class for this project and defines attributes for other classes.

### Other Classes
These classes inherit from BaseModel:

- User
- State
- City
- Amenity
- Place
- Review

### Storage
The FileStorage class is used for saving and loading data from a JSON file, ensuring data persistence. It acts as a bridge between the application's objects and a file.

## Testing

Unit tests for this project are defined in the tests folder. You can run the entire test suite by using the following command:

```
<!-- python3 -m unittest discover tests -->
```

Alternatively, you can run individual test files:

```
python3 -m tests/test_models/test_base_model.py
```
## 👥 Team
🐣Alexis Billemont : [git-alexis](https://github.com/git-alexis)

🦆 Cassandre Pernelle : [Wefixte](https://github.com/wefixte)
