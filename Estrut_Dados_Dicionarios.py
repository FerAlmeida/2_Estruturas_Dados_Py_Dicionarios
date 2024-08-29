usuario = {"nome": "Fernando", 
           "Tipo de acesso":"Adminstrador",
            "nivel de acesso" : 1 }   

print(usuario["nome"]) 
print(usuario["Tipo de acesso"])
print(usuario["nivel de acesso"])  

print(usuario.keys())

print(usuario.values())

usuario = {"nome": "Fernando", 
           "Tipo de acesso":"Adminstrador",
            "nivel de acesso" : 1 } 
print(usuario)
usuario.update({"ultimo acesso":"2024-08-20"})
print(usuario)

usuario.pop("Tipo de acesso")
print(usuario)

usuario["nome"] = "Aristoteles"
print(usuario)
