import subprocess

locations = ["ragus",
#  "tests", 
# "docs/conf.py"
]
def lint():
    subprocess.run(["flake8"] + locations)
    subprocess.run(["mypy"] + locations)

def format():
    subprocess.run(["black"] + locations)

# def docs():
#     subprocess.run(["sphinx-build", "docs", "docs/_build"])

def test():
    subprocess.run(["python", "manage.py", "test"])
