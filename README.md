# General

Simple CLI game about warriors and monsters :)


## Scenario JSON structure

| Attribute name   | Type           | Description                                                                |
|------------------|----------------|----------------------------------------------------------------------------|
| `input_required` | boolean        | This step will required some user input                                    |
| `message`        | string         | Message that should be displayed to user in CLI                            |
| `validators`     | list[string]   | List of `Validator` function names that should be called to validate input |
| `post_process`   | list[string]   | List of `Game` functions that should be executed after main action         |
| `params`         | list[string]   | List of parameter names that should be passed to display message           |
| `attribute`      | string         | Where system should save inputted value.                                   |