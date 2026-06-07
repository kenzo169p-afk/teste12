import re

filepath = r"c:\Users\gordo\Desktop\teste\teste12\topchoicecorretora\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"A\s+<strong>Top Choice Corretora de Seguros</strong>\s+é especializada em Seguro Garantia,[\s\S]*?Planos de Saúde Empresariais\.": 
        r"Na <strong>Top Choice Corretora</strong>, a gente cuida de tudo para você: do Seguro Auto e Residencial, até o plano de saúde da sua empresa e consórcios.",
        
    r"Atendemos pessoas físicas e empresas em todo o Brasil, com foco em consultoria técnica,[\s\S]*?ajudando você a proteger e expandir seu patrimônio com segurança\.":
        r"Atendemos todo o Brasil com total transparência e agilidade. Nossa missão é simplificar o mundo dos seguros e ajudar você a proteger o que mais importa, sem complicação.",
        
    r"Seguros, consórcios e planos de saúde com clareza, agilidade e direção certa":
        r"Seguros, consórcios e planos de saúde sem burocracia e direto ao ponto",
        
    r"A Top Choice ajuda você a comparar opções e contratar com segurança, com forte atuação em Seguro Garantia, consórcios, planos de saúde e proteção patrimonial\.":
        r"A gente te ajuda a comparar as melhores opções do mercado e contratar com segurança. Fale com especialistas que entendem de verdade do assunto.",
        
    r"Decisão mais segura":
        r"Decida com confiança",
        
    r"Leitura técnica, comparação clara e apoio para contratar melhor\.":
        r"Nós traduzimos o 'segurês' para você, comparamos tudo com clareza e te damos todo o apoio.",
        
    r"Soluções para cada momento da sua vida e do seu negócio":
        r"Temos a solução certa para o seu momento de vida e para o seu negócio",
        
    r"Escolha a categoria ideal e encontre a alternativa mais adequada com clareza e agilidade\.":
        r"Escolha o que você precisa abaixo e vamos resolver isso rapidinho e sem dor de cabeça.",
        
    r"Por que clientes e empresas escolhem a Top Choice":
        r"Por que tanta gente confia na Top Choice?",
        
    r"A Top Choice ajuda a entender o cenário, comparar caminhos e direcionar a escolha com mais clareza\.":
        r"A gente te ajuda a entender tudo, compara as opções e te mostra o melhor caminho de forma super clara.",
        
    r"Quem escolhe a Top Choice reconhece a diferença":
        r"Quem escolhe a gente, sente a diferença",
        
    r"Avaliações reais que destacam agilidade, clareza no atendimento e suporte ao longo da contratação\.":
        r"Veja o que nossos clientes falam sobre nossa agilidade e suporte em todas as etapas."
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Text simplified successfully.")
