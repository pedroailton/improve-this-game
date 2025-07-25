from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from personagemnpc import PersonagemNPC

from random import choice

def main():
    # Criando personagens e vilões
    heroi = Heroi('Link', 30, 100)
    npc = PersonagemNPC('Zelda', 28, 80)
    vilao = Vilao('Ganon', 45, 120, 'Alta')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()