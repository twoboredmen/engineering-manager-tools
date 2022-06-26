# Checkin

## The problem I have

I see everyone during our daily standup. However, we do not actually check in on how one another is doing. It is important to check in on everyone once in awhile and make sure they are doing okay. However, if you run a large enough team, you can't always monitor every Slack conversation and make sure you have 100% checked in on everyone everyday. This becomes a problem for me as I want to make sure everyone is getting attended to even if I have to be reminded.

## How this fixes it

This script allows me to check when was our last message. It will let you know it's time to send a message or send that first hello message for you!

## Pre-requisite

- pipenv

## Getting Started

### Installation

We can use virtual environment to run this by executing using `pipenv`.

```bash
# Visit https://api.slack.com/start to generate the token
$ export SLACK_BOT_TOKEN=...
$ pipenv install
$ pipenv shell
$ python3 main.py
```

### How to use this

#### `main` file

In the `main()` file, there is a couple of parameters that you can set. They are time and list of people you want to check in! Just change that according to your liking and you are set!

#### Message delivery

Currently, we only have the script prints out the list of people you should probably hit up! However, you can tweak the script and use `SlackHelper` to send that first hello message for you!

## Way to run

- Manually
- Github Action running it at specific time
- Background job on your local machine
- and many more ...

## Credit

This was inspired by my beloved Engineering Manager, [Greg](https://github.com/gregorybutron), who cares _deeply_ about me.
