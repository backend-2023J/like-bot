# like-bot

## Create vertual environment

```bash
python -m venv venv
```

## Environment activate

### For Mac or Linux

```bash

source venv/bin/activate
```

### For Windows

```bash

source venv/Scripts/activate
```

## Install required libraries

```bash
pip install -r requirements.txt
```

## python-telegram-bot Documentation

[python-telegram-bot==13.15](https://docs.python-telegram-bot.org/en/v13.15/)

## Result Database

```json

{
    "message_id1": {
        "user1": {
            "like": 0,
            "dislike": 0
        },
        "user1": {
            "like": 1,
            "dislike": 0
        },
    },
    "message_id2": {
        "user1": {
            "like": 0,
            "dislike": 0
        },
        "user1": {
            "like": 1,
            "dislike": 0
        },
    },
}
```
