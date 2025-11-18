#Tem que instalar a biblioteca pandas, para isso, abra o prompt de comando e digite: pip install pandas
import pandas as pd

codigos = [295,317,558,702,983]
sequencias = []

# Realiza o rodízio x vezes
for i in range(70):
    # Faz uma cópia da lista original para evitar modificar os códigos originais
    codigo_copia = codigos.copy()

    num_rotacoes = i % len(codigos)
    codigo_copia = codigo_copia[num_rotacoes:] + codigo_copia[:num_rotacoes]
    sequencias.append(codigo_copia)

df = pd.DataFrame(sequencias, columns=[f'Código_{i + 1}' for i in range(len(codigos))])
df.insert(0, 'ID', range(1, len(df) + 1))
df.to_excel('rodizio.xlsx', index=False)
