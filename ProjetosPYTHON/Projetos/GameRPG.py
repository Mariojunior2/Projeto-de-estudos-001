import random
import math
import time
import sys

class Personagem:
    def __init__(self):
        self.nome = "Netf"
        self.nivel = 1
        self.xp = 0
        self.xp_proximo_nivel = 100
        self.pontos_disponiveis = 0
        self.forca = 10
        self.defesa = 5
        self.magia = 5
        self.agilidade = 5
        self.vida_maxima = 100
        self.vida_atual = 100
        self.mana_maxima = 50
        self.mana_atual = 50
        self.habilidades = {
            'investigar': False,
            'furtividade': False,
            'magia': False
        }
        self.inventario = []
    
    def mostrar_status(self):
        print(f"\n=== Status de {self.nome} ===")
        print(f"Nível: {self.nivel}")
        print(f"XP: {self.xp}/{self.xp_proximo_nivel}")
        print(f"Pontos disponíveis: {self.pontos_disponiveis}")
        print(f"Força: {self.forca} | Magia: {self.magia}")
        print(f"Agilidade: {self.agilidade} | Defesa: {self.defesa}")
        print(f"Vida: {self.vida_atual}/{self.vida_maxima}")
        print(f"Mana: {self.mana_atual}/{self.mana_maxima}")
        print("Habilidades:", ", ".join([k for k, v in self.habilidades.items() if v]))
        print("Inventário:", ", ".join(self.inventario) if self.inventario else "Vazio")

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"\nVocê ganhou {quantidade} XP!")
        while self.xp >= self.xp_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.pontos_disponiveis += 3
        self.xp -= self.xp_proximo_nivel
        self.xp_proximo_nivel = int(self.xp_proximo_nivel * 1.5)
        self.vida_maxima += 20
        self.mana_maxima += 10
        self.vida_atual = self.vida_maxima
        self.mana_atual = self.mana_maxima
        print(f"\n=== PARABÉNS! Você subiu para o nível {self.nivel}! ===")
        self.distribuir_pontos()
        
    def distribuir_pontos(self):
        while self.pontos_disponiveis > 0:
            self.mostrar_status()
            print("\nOnde deseja alocar seus pontos?")
            print("1 - Força (+1 Dano físico)")
            print("2 - Defesa (+1% Redução de dano)")
            print("3 - Magia (+1 Dano mágico e +5 Mana)")
            print("4 - Agilidade (+1% Chance de esquiva)")
            escolha = input("Escolha (1-4) ou 'sair' para depois: ")
            
            if escolha.lower() == 'sair':
                break
            elif escolha == '1':
                self.forca += 1
                self.pontos_disponiveis -= 1
            elif escolha == '2':
                self.defesa += 1
                self.pontos_disponiveis -= 1
            elif escolha == '3':
                self.magia += 1
                self.mana_maxima += 5
                self.pontos_disponiveis -= 1
            elif escolha == '4':
                self.agilidade += 1
                self.pontos_disponiveis -= 1
            else:
                print("Opção inválida!")

    def iniciar_combate(self, inimigo_tipo):
        inimigos = {
            'comum': {'nome': 'Criatura Corrompida', 'xp': 10, 'vida': 30, 'dano': 5},
            'tutorial': {'nome': 'Criatura Enfraquecida', 'xp': 0, 'vida': 15, 'dano': 2},
            'chefe': {'nome': 'Guardião Celestial', 'xp': 100, 'vida': 100, 'dano': 15}
        }
        
        inimigo = inimigos[inimigo_tipo]
        vida_inimigo = inimigo['vida']
        
        print(f"\n⚔️ Combate contra {inimigo['nome']} iniciado! ⚔️")
        
        while self.vida_atual > 0 and vida_inimigo > 0:
            print(f"\nSua Vida: {self.vida_atual} | Vida do Inimigo: {vida_inimigo}")
            print("1 - Ataque Físico")
            print("2 - Tentar Esquiva")
            if self.habilidades['magia']:
                print("3 - Ataque Mágico")
            if 'Adaga do Profeta' in self.inventario:
                print("4 - Usar Adaga Celestial")
            
            escolha = input("Escolha sua ação: ")
            
            # Ação do jogador
            if escolha == '1':
                dano = self.forca + random.randint(1, 5)
                vida_inimigo -= dano
                print(f"Você atacou causando {dano} de dano!")
            elif escolha == '2':
                if random.randint(1, 100) <= self.agilidade:
                    print("Você esquivou habilmente do ataque!")
                    continue
                else:
                    print("Falha na esquiva!")
                    dano = math.floor(inimigo['dano'] * (1 - self.defesa/100))
                    self.vida_atual -= dano
            elif escolha == '3' and self.habilidades['magia']:
                if self.mana_atual >= 10:
                    dano = self.magia + random.randint(3, 8)
                    self.mana_atual -= 10
                    vida_inimigo -= dano
                    print(f"⚡ Você lançou um feitiço causando {dano} de dano mágico!")
                else:
                    print("Mana insuficiente!")
                    continue
            elif escolha == '4' and 'Adaga do Profeta' in self.inventario:
                dano = self.agilidade * 2 + random.randint(2, 6)
                vida_inimigo -= dano
                print(f"🔪 Você lançou a adaga celestial causando {dano} de dano!")
            else:
                print("Ação inválida!")
                continue
            
            # Ação do inimigo
            if vida_inimigo > 0:
                dano_inimigo = inimigo['dano']
                reducao = math.floor(dano_inimigo * (self.defesa/100))
                dano_real = dano_inimigo - reducao
                self.vida_atual -= dano_real
                print(f"O inimigo ataca causando {dano_real} de dano!")
            
            if self.vida_atual <= 0:
                print("\n💀 Você foi derrotado! O mundo mergulha na escuridão...")
                sys.exit()
        
        print(f"\n🎉 {inimigo['nome']} derrotado!")
        if inimigo['xp'] > 0:
            self.ganhar_xp(inimigo['xp'])

def tutorial_masmorra(jogador):
    print("\n" + "="*50)
    print("🏰 Tutorial: A Masmorra Esquecida 🏰")
    print("="*50)
    time.sleep(2)
    
    # Parte inicial do tutorial
    print("\nVocê acorda com uma dor latejante na cabeça. O chão frio de pedra")
    print("treme com um rugido distante. Duas passagens se apresentam:")
    print("1 - Passagem à esquerda com luz fraca")
    print("2 - Corredor à direita com sons de água")
    
    escolha = input("\nPara onde ir? (1/2): ")
    
    # Primeira escolha do jogador
    if escolha == '1':
        print("\nVocê segue pela passagem iluminada...")
        print("Encontra uma parede com símbolos antigos!")
        if jogador.magia >= 5:
            print("Seu conhecimento mágico revela uma mensagem oculta:")
            print("⚠️ 'Cuidado com os que jazem nas sombras' ⚠️")
            jogador.habilidades['investigar'] = True
        else:
            print("Os símbolos são incompreensíveis para você...")
    else:
        print("\nÁgua gelada escorre pelo corredor...")
        print("Você escorrega e cai em uma poça!")
        if jogador.agilidade >= 5:
            print("💨 Você se recupera graciosamente!")
            jogador.habilidades['furtividade'] = True
        else:
            print("Você se machuca levemente! (-5 HP)")
            jogador.vida_atual -= 5
    
    # Evento principal
    print("\n" + "-"*50)
    print("Um grito agonizante ecoa à frente! Você corre em direção ao som...")
    time.sleep(2)
    
    print("\n💀 Cena Horripilante:")
    print("Um ancião vestindo trajes de mago está sendo atacado por")
    print("uma criatura celestial deformada, com membros alongados e")
    print("olhos brilhando em vermelho sanguinolento!")
    
    input("\nPressione Enter para intervir...")
    
    # Diálogo dramático
    print("\nMago Moribundo: (gritando) Você... o Escolhido... (cospe sangue)")
    time.sleep(1)
    print("Mago: Destrua o... núcleo... antes que... consuma... tudo...")
    time.sleep(2)
    print("A criatura emite um rugido ensurdecedor e avança em sua direção!")
    
    # Sequência de ação rápida
    print("\n⚡ Reação Rápida:")
    print("1 - Empurrar a criatura")
    print("2 - Pegar uma adaga no chão")
    print("3 - Usar magia instintiva")
    
    escolha = input("O que faz? (1-3): ")
    
    # Consequências da escolha
    if escolha == '1':
        if jogador.forca >= 5:
            print("\n💪 Você empurra a criatura com força surpreendente!")
        else:
            print("\nA criatura é muito forte! Você é arremessado contra a parede! (-10 HP)")
            jogador.vida_atual -= 10
    elif escolha == '2':
        print("\n🔪 Você pega a adaga e a lança contra a criatura!")
        if jogador.agilidade >= 5:
            print("A adaga atinge o olho da criatura! Ela recua uivando!")
        else:
            print("A adaga erra o alvo e quebra na parede!")
    elif escolha == '3':
        print("\n🌀 Energia mágica flui através de você!")
        jogador.habilidades['magia'] = True
        print("Você desencadeia um feitiço instintivo!")
    else:
        print("\nHesitação fatal! A criatura ataca impiedosamente!")
        jogador.vida_atual -= 15
    
    # Combate tutorial
    print("\n" + "⚔️"*20)
    print("A criatura enfraquecida inicia o combate!")
    jogador.iniciar_combate('tutorial')
    
    # Epílogo do tutorial
    print("\n" + "🌌"*20)
    print("O mago, em seus últimos suspiros, toca sua testa:")
    print("Mago: Veja... a verdade... por trás... das...")
    time.sleep(2)
    
    # Visão profética
    print("\n💫 Uma visão ardente invade sua mente:")
    print("- Cidades em chamas sob céus sangrentos")
    print("- Criaturas cósmicas devorando continentes")
    print("- Um portal distorcido no centro do mundo")
    time.sleep(3)
    
    print("\nO mago morre e seu corpo dissolve-se em partículas de luz.")
    print("Você encontra um pergaminho antigo e uma adaga celestial.")
    jogador.inventario.extend(['Pergaminho Antigo', 'Adaga do Profeta'])
    print("🔮 Habilidade Desbloqueada: Sentido Místico")
    print("🗡️ Item Obtido: Adaga do Profeta")
    
    # Decisão final do tutorial
    print("\n" + "🚪"*20)
    print("Duas saídas se revelam:")
    print("1 - Escadaria para a superfície (luz do sol)")
    print("2 - Túnel profundo (sussurros sombrios)")
    
    escolha = input("Qual caminho seguir? (1/2): ")
    
    if escolha == '1':
        print("\nVocê emerge em um mundo devastado pela guerra...")
        print("Criaturas celestiais dominam a paisagem enquanto cidades queimam ao longe.")
    else:
        print("\nVocê desce para as profundezas da terra...")
        print("Uma energia maligna pulsante guia seus passos nas trevas...")
    
    print("\n=== TUTORIAL COMPLETO ===")
    print("Agora sua verdadeira jornada começa...")

def main():
    jogador = Personagem()
    print("\nBem-vindo ao Mundo das Sombras Celestiais")
    print("Sua jornada começa nas profundezas da Masmorra Esquecida...")
    time.sleep(2)
    
    tutorial_masmorra(jogador)
    
    # Continuação do jogo após o tutorial
    print("\n\n=== CAPÍTULO 1: O DESPERTAR ===")
    print("Você agora deve explorar o mundo e descobrir a verdade por trás da profecia!")
    while True:
        print("\nO que deseja fazer?")
        print("1 - Explorar adiante")
        print("2 - Ver status")
        print("3 - Sair do jogo")
        escolha = input("Escolha: ")
        
        if escolha == '1':
            print("\nVocê avança pela paisagem devastada...")
            # Adicionar sistema de exploração aqui
        elif escolha == '2':
            jogador.mostrar_status()
        elif escolha == '3':
            print("\nAté a próxima, guerreiro!")
            sys.exit()
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    if input('Deseja jogar? (sim/não) >> ').lower() in ['sim', 's', 'yes']:
        main()
    else:
        print('Até mais!')