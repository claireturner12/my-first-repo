# My First Repo!

Learning and practicing version control!

## Setup

Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line.

```sh
cd ~/Desktop/my-first-repo
```

Create a virtual environment:

```sh
conda create -n my-first-env python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_____________"
```

## Usage

Example script:

```sh
python app/my_script.py
```

Game of rock, paper, scissors:

```sh
python app/rps.py

# alternative "modular style" command:
# python -m app.rps
```

Stocks dashboard:
```sh
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```