import subprocess

locations = ["sugar",
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
    subprocess.run(["pytest", "--cov", "-s", "-vvv", "--ignore=docs"])