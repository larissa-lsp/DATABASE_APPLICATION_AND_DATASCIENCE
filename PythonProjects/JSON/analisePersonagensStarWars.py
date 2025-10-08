import json


def analisar_personagens_sw(caminho_arquivo):
    """
    Lê um arquivo JSON de um caminho especificado, analisa os personagens
    da chave 'people' e conta a quantidade por gênero.
    """
    contador_masculino = 0
    contador_feminino = 0
    contador_outros = 0

    try:
        # Abre e carrega o arquivo JSON usando o caminho passado como parâmetro
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        # CORREÇÃO PRINCIPAL: Os personagens estão na lista da chave 'people'.
        # O método .get() é seguro: se a chave 'people' não existir, ele usa uma lista vazia.
        lista_personagens = dados.get('people', [])

        # Verificação para o caso de a lista de personagens estar vazia
        if not lista_personagens:
            print("A chave 'people' não foi encontrada ou a lista de personagens está vazia no arquivo JSON.")
            return

        print("--- Personagens de Star Wars ---")
        # Itera através da lista de personagens extraída
        for personagem in lista_personagens:
            nome = personagem.get('name', 'Desconhecido')
            genero = personagem.get('gender', 'n/a')

            print(f"Nome: {nome}, Gênero: {genero}")

            # Incrementa o contador de gênero apropriado
            if genero.lower() == 'male':
                contador_masculino += 1
            elif genero.lower() == 'female':
                contador_feminino += 1
            else:
                # Contabiliza 'n/a', 'none', 'hermaphrodite', etc. como 'Outros'
                contador_outros += 1

        print("\n--- Resumo de Gênero dos Personagens ---")
        print(f"Personagens Masculinos: {contador_masculino}")
        print(f"Personagens Femininos: {contador_feminino}")
        print(f"Gênero Não Indicado/Outros: {contador_outros}")

    except FileNotFoundError:
        print(f"Erro: O arquivo em {caminho_arquivo} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo em {caminho_arquivo} não é um arquivo JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# --- Seção Principal do Script ---
if __name__ == '__main__':
    # Cole o caminho do seu arquivo aqui
    arquivo_star_wars = r"star_wars.json"

    # Chama a função e passa o caminho do arquivo como argumento
    analisar_personagens_sw(arquivo_star_wars)