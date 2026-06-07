from bs4 import BeautifulSoup
import re

filepath = r"c:\Users\gordo\Desktop\teste\teste12\topchoicecorretora\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

replacements = {
    # Services
    r"Para empresas que precisam participar de licitações, assinar contratos ou apresentar garantias com mais agilidade\.?": "Garantia rápida para sua empresa participar de licitações e fechar contratos sem dor de cabeça.",
    r"Planejamento para conquistar patrimônio, investir ou ampliar estrutura sem juros e com estratégia\.?": "Realize o sonho da casa ou carro próprio e expanda seu negócio sem pagar juros absurdos.",
    r"Soluções para empresas, profissionais e famílias que buscam rede adequada e boa relação entre custo e cobertura\.?": "Planos de saúde que cabem no seu bolso, com as melhores redes médicas para você ou sua empresa.",
    r"Proteção para patrimônio, responsabilidade, mobilidade e tranquilidade no dia a dia de pessoas e empresas\.?": "Seguros completos para proteger seu carro, sua casa, sua empresa e a sua vida.",
    
    # Why Us
    r"Experiência que encurta o caminho": "Experiência de verdade",
    r"Mais de 20 anos de atuação em Seguro Garantia e vivência em soluções para pessoas e empresas\.?": "Mais de 20 anos de mercado resolvendo problemas e protegendo o que é seu.",
    r"Agilidade com critério": "Rápido e certeiro",
    r"Velocidade na cotação e no direcionamento, sem perder coerência técnica\.?": "Cotações rápidas e com o melhor custo-benefício do mercado.",
    r"Acompanhamento do início ao fim": "Do seu lado sempre",
    r"Suporte nas etapas mais importantes, da avaliação inicial à contratação\.?": "Ajudamos você desde a primeira cotação até o momento que precisar usar o seguro.",
    
    # CTAs / Forms
    r"Precisa de uma cotação ou quer entender a melhor alternativa para o seu caso\??": "Quer uma cotação rápida ou bater um papo para tirar dúvidas?",
    r"Fale com a Top Choice no WhatsApp e receba direcionamento com agilidade, clareza e atenção ao que realmente faz sentido para você ou para sua empresa\.?": "Chama a gente no WhatsApp! Nossa equipe está pronta para te atender rápido e sem enrolação.",
    r"Peça uma análise personalizada": "Faça uma simulação agora",
    r"Preencha o formulário e a Top Choice entra em contato para entender sua necessidade e indicar a alternativa mais adequada para você ou para sua empresa\.?": "Preencha os dados abaixo e a gente te chama com a melhor solução para o seu bolso.",
    r"Envie sua solicitação": "Mande uma mensagem pra gente",
    r"Você pode pedir uma cotação, tirar dúvidas ou informar o tipo de solução que procura\.?": "Diga o que você precisa e nós cuidamos do resto.",
    
    # Guarantee Insurance Types
    r"Seguro Garantia com leitura técnica, agilidade e segurança na estruturação": "Seguro Garantia sem burocracia e aprovado super rápido",
    r"A Top Choice atua com forte especialização em Seguro Garantia, apoiando empresas em licitações, contratos e garantias judiciais com mais clareza e velocidade\.?": "Especialistas em Seguro Garantia. Ajudamos sua empresa em licitações e contratos judiciais para liberar seu fluxo de caixa rápido.",
    r"Para participação em licitações públicas e privadas com a garantia exigida no edital\.?": "A garantia exata que o seu edital pede.",
    r"Para empresas que precisam garantir a execução de contratos firmados\.?": "Feche seus contratos com total garantia.",
    r"Para garantir valores antecipados previstos em contrato\.?": "Proteja qualquer valor adiantado.",
    r"Alternativa ao depósito recursal, preservando caixa da empresa\.?": "Não trave o dinheiro da sua empresa na justiça. Use seguro.",
    r"Solução para garantir execuções fiscais sem imobilizar recursos em dinheiro\.?": "Garantia fiscal sem bloquear sua conta bancária.",
    r"Falar sobre Seguro Garantia": "Chamar especialista em Garantia",
    
    # Miscellaneous
    r"Soluções organizadas para cada perfil de cliente": "Soluções feitas na medida pra você",
    r"A Top Choice atende necessidades diferentes com o mesmo cuidado na análise, no direcionamento e na contratação\.?": "A gente entende o que você precisa e encontra a opção mais barata e segura.",
    r"Ver soluções para empresas": "Ver opções para Empresas",
    r"Ver soluções para você": "Ver opções para Você",
    r"Trabalhamos com seguradoras, administradoras e operadoras reconhecidas no mercado": "Só trabalhamos com as maiores e melhores seguradoras",
    r"A Top Choice compara opções entre players consolidados para buscar aderência, competitividade e segurança na contratação\.?": "Nós comparamos todas as opções nas melhores empresas do Brasil para te dar o preço mais justo."
}

# Clean strings recursively
for text_node in soup.find_all(string=True):
    # Only process nodes that are actually text (not comments, etc)
    if text_node.parent.name not in ['script', 'style']:
        text = str(text_node)
        modified = False
        for old, new in replacements.items():
            # Use regex for case insensitive and loose spacing matching
            pattern = re.compile(old.replace(' ', r'\s+'), re.IGNORECASE)
            if pattern.search(text):
                text = pattern.sub(new, text)
                modified = True
        
        if modified:
            text_node.replace_with(text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("All texts simplified and humanized.")
