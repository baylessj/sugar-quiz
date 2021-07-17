# sugar-quiz

## Installation

```
npm install
poetry install
npm run build
```

## Running

Windows:

```
poetry shell
heroku local -f Procfile.windows
```

*nix:

```
poetry shell
heroku local
```

### Login

You can log in as any one of the residents with the following credentials:

username: Resident email (e.g. annettemoore@dyer-summers.com)
password: Resident First Name + Last Name (e.g. AdamTaylor)

## Debugging

Admin login:

```
user: root
pass: user + 1234
```