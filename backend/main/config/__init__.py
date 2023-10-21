import os

submodules = os.listdir(os.path.dirname(__file__))


def filter_submod(mod):
    if mod == "__init__.py" or mod == "__pycache__":
        return False
    return True


submodules = filter(filter_submod, submodules)

for mod_name in submodules:
    mod_name = mod_name.replace(".py", "")
    import_str = f"from .{mod_name} import *"
    exec(import_str)
