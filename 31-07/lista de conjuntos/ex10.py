def obter_conjunto(nome):
    while True:
        try:
            conjunto = input(f"📝 Digite os elementos do conjunto {nome} separados por vírgula: ")
            return set(map(int, conjunto.split(',')))
        except ValueError:
            print("❌ Entrada inválida! Certifique-se de digitar números inteiros separados por vírgula.")

def uniao(A, B):
    print("🌐 A ∪ B =", A | B)

def intersecao(A, B):
    print("🔗 A ∩ B =", A & B)

def diferenca(A, B):
    print("➖ A - B =", A - B)
    print("➖ B - A =", B - A)

def produto_cartesiano(A, B):
    produto_cartesiano = {(a, b) for a in A for b in B}
    print("✖️ A × B =", produto_cartesiano)

def verificar_subconjunto_A_B(A, B):
    if A.issubset(B):
        print("📑 A é subconjunto de B")
        if A != B:
            print("📄 A é subconjunto próprio de B")
    else:
        print("❌ A não é subconjunto de B")

def verificar_subconjunto_B_A(B, A):
    if B.issubset(A):
        print("📑 B é subconjunto de A")
        if B != A:
            print("📄 B é subconjunto próprio de A")
    else:
        print("❌ B não é subconjunto de A")

def alterar_conjuntos():
    global A, B
    A = obter_conjunto('A')
    B = obter_conjunto('B')

def sair():
    print("🚪 Encerrando o programa...")
    return True

def menu_principal():
    switch = {
        '1': lambda: uniao(A, B),
        '2': lambda: intersecao(A, B),
        '3': lambda: diferenca(A, B),
        '4': lambda: produto_cartesiano(A, B),
        '5': lambda: verificar_subconjunto_A_B(A, B),
        '6': lambda: verificar_subconjunto_B_A(B, A),
        '7': alterar_conjuntos,
        '0': sair
    }
    
    while True:
        print("\n===========================================")
        print("            📊 MENU DE OPERAÇÕES 📊         ")
        print("===========================================")
        print("🔢 Escolha uma das opções abaixo:")
        print(" 1️⃣  União (A ∪ B) 🌐")
        print(" 2️⃣  Intersecção (A ∩ B) 🔗")
        print(" 3️⃣  Diferença (A - B ou B - A) ➖")
        print(" 4️⃣  Produto Cartesiano (A × B) ✖️")
        print(" 5️⃣  Verificar se A é subconjunto de B 📑")
        print(" 6️⃣  Verificar se B é subconjunto de A 📄")
        print(" 7️⃣  Alterar conjuntos A e B 🔄")
        print(" 0️⃣  Sair do programa 🚪")
        print("===========================================")
        
        opcao = input("👉 Digite a sua escolha: ")

        if opcao in switch:
            if opcao == '0' and switch[opcao]():
                break
            else:
                switch[opcao]()
        else:
            print("❌ Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    A = obter_conjunto('A')
    B = obter_conjunto('B')
    menu_principal()
