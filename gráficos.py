import matplotlib.pyplot as plt

grupos = ['Aluno', 'Professor', 'Outros']
uso_2fa = [65, 9, 2]  # Valores absolutos
total_por_grupo = [100, 15, 5]  # Valores absolutos

percentual_uso = [65, 60, 40]  # Percentual aproximado

plt.bar(grupos, percentual_uso, color=['blue', 'green', 'orange'])
plt.title('Percentual de Uso de 2FA por Grupo')
plt.ylabel('Percentual (%)')
plt.xlabel('Grupo')
plt.ylim(0, 100)
plt.show()

motivos = [
    'Medo de perder acesso',
    'Não sabe ativar',
    'Acha complicado',
    'Não é necessário',
    'Outro'
]

contagem = [26, 20, 12, 10, 22]  # Valores absolutos

plt.pie(contagem, labels=motivos, autopct='%1.1f%%', startangle=90, colors=['red', 'orange', 'yellow', 'green', 'gray'])
plt.title('Principais Motivos para Não Usar 2FA')
plt.axis('equal')

