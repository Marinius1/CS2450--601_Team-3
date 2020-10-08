import ast
import glob

my_path = './view/*/*.py'

files = glob.glob(my_path)

for i in files:
    with open(i) as f:
        code = ast.parse(f.read())

    for node in ast.walk(code):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            docstring = ast.get_docstring(node)
            if docstring:
                print(repr(docstring))

                with open("view_docstrings.txt", "a+") as f:
                    f.write("\n\n")
                    f.write(i + "\n")
                    f.write(docstring)



