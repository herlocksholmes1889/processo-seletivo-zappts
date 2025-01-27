dic_sugestoes = {
    "ele": "esta pessoa",
    "um": "uma",
    "desenvolvedor": "pessoa desenvolvedora",
    "estagiário": "pessoa estagiária",
    "ninja": "pessoa habilidosa",
    "fera": "experiente"
}

def detectar_termos(desc_vaga):
    termos_detectados = []

    desc_vaga = desc_vaga.lower().split()

    for palavra in desc_vaga:
        if palavra in dic_sugestoes:
            termos_detectados.append(palavra)
    
    return termos_detectados

def vaga_corrigida_exemplo(desc_vaga):
    palavras = desc_vaga.split()

    for i, palavra in enumerate(palavras):
        palavra_lower = palavra.lower()  
        if palavra_lower in dic_sugestoes:
            sugestao = dic_sugestoes[palavra_lower]
            if palavra[0].isupper():  
                sugestao = sugestao.capitalize()
            palavras[i] = sugestao
    
    return " ".join(palavras)

def relatorio(desc_vaga):
    termos_detectados = detectar_termos(desc_vaga)

    if len(termos_detectados) > 0:  
        print("Foi detectado os seguintes termos preferencialmente masculinos na descrição da vaga: ")
        for termo in termos_detectados:
            print(f"{termo} - Sugestão de mudança: {dic_sugestoes[termo]}")
    else:
        print("Nenhum termo preferencialmente masculino foi detectado.")

desc_vaga = "Estamos procurando um desenvolvedor fera para uma vaga de estágio. Ele deve ser ninja em Python e Django."

print("Relatório: ", relatorio(desc_vaga))
print("-------")
print("Vaga corrigida: ", vaga_corrigida_exemplo(desc_vaga))
