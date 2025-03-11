class Inventario:
    def __init__(self):
        self.itens = []  # Lista para armazenar os itens do inventário

    def adicionar_item(self, item):
        if item not in self.itens:
            self.itens.append(item)
            print(f"\n{item} adicionado ao seu inventário.")
        else:
            print(f"\nVocê já possui {item} no inventário.")

    def exibir_inventario(self):
        if not self.itens:
            print("\nSeu inventário está vazio.")
        else:
            print("\nSeu Inventário:")
            for item in self.itens:
                print(f"- {item}")
