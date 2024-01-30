# Ez GPT
Command line tool that streamlines gpt requests, so you don't have to perform a large curl GET request in the CLI.

### Basic call with default temperature:
Note: You will need a ChatGPT api bearer token and available quota to make requests that provide returns of any value. Also, you may have to use `python3` in place of `python` depending on your configuration.

```
python main.py <BEARER_TOKEN> '<YOUR_TEXT>'
```

### Call with custom temperature:

```
python main.py <BEARER_TOKEN> '<YOUR_TEXT>' <CUSTOM_TEMPERATURE>
```
### Docker
Dockerfile is provided if you prefer to run via Docker.
### Requires the following packages:

```
pip install requests
```
