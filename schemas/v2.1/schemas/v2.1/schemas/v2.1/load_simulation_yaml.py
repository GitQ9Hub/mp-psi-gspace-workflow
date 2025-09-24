import yaml
import os

class LoaderWithInclude(yaml.SafeLoader):
    def __init__(self, stream):
        super().__init__(stream)

def include_constructor(loader, node):
    filename = loader.construct_scalar(node)
    base_path = os.path.dirname(loader.name)
    full_path = os.path.join(base_path, filename)
    with open(full_path, 'r') as f:
        return yaml.load(f, LoaderWithInclude)

LoaderWithInclude.add_constructor('!include', include_constructor)

with open("simulation.yaml", 'r') as f:
    LoaderWithInclude.name = f.name  # Pass filename to constructor
    data = yaml.load(f, LoaderWithInclude)

print(data)
