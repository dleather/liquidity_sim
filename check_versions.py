import pkg_resources
import sys

def get_installed_version(package_name):
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return "Not installed"

def main():
    print(f"Python version: {sys.version}\n")
    print("Package Version Check:")
    print("-" * 50)
    
    # Read requirements.txt
    with open('requirements.txt', 'r') as f:
        requirements = f.readlines()
    
    # Process each requirement
    for req in requirements:
        req = req.strip()
        if not req:  # Skip empty lines
            continue
            
        # Parse package name and required version
        if '>=' in req:
            package_name, required_version = req.split('>=')
            package_name = package_name.strip()
            required_version = required_version.strip()
        else:
            package_name = req.strip()
            required_version = "N/A"
        
        # Get installed version
        installed_version = get_installed_version(package_name)
        
        # Print results
        print(f"Package: {package_name}")
        print(f"Required: {required_version}")
        print(f"Installed: {installed_version}")
        print("-" * 50)

if __name__ == "__main__":
    main() 