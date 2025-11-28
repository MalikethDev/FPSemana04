import json

def load_data(filename):
    try:
        with open(filename, "rt", encoding="utf-8") as file:
            content = file.read().strip()   # lê e remove espaços em branco

    # Ficheiro não encontrado
    except FileNotFoundError:
        print("Erro: Ficheiro Não Encontrado!")
        return None

    # Ficheiro vazio
    if content == "":
        print("Erro: Ficheiro Vazio!")
        return None
    
    # Json inválido
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        print("Erro: Ficheiro Não Contém JSON Válido!")
        return None
    
    # Mandatory fields
    mandatory_keys = ["nome", "idade", "localização"]

    # Print if there are missing fieldss
    for key in mandatory_keys:
        if key not in data:
            print("Erro: Campos Obrigatórios em Falta!")
            return None
    
    # If correct
    return data

# Usage with the required check
data = load_data("data.json")

if data is not None: # only print if JSON loaded correctly
    print(data)

# Final message
print("Processo Concluido!")
