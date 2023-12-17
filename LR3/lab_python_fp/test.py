arr = ['прог аа ммм', 'аа кк вв']
print(list(filter(lambda x: x.split()[0] == "аа", arr)))