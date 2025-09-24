import yaml
import os
import sys

def get_loader_with_include(base_path):
    class LoaderWithInclude(yaml.SafeLoader):
        pass

    def include_constructor(loader, node):
        filename = loader.construct_scalar(node)
        full_path = os.path.join(base_path, filename)
        with open(full_path, 'r') as f:
            return yaml.load(f, Loader=get_loader_with_include(os.path.dirname(full_path)))

    LoaderWithInclude.add_constructor('!include', include_constructor)
    return LoaderWithInclude

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load_simulation_yaml.py <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    base_path = os.path.dirname(yaml_file)

    with open(yaml_file, 'r') as f:
        data = yaml.load(f, Loader=get_loader_with_include(base_path))
        print("✅ Loaded successfully:", yaml_file)
