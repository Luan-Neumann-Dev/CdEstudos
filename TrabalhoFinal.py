import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = './StudentPerformanceFactors.csv'
df = pd.read_csv(file_path)

df = df.drop_duplicates()
df = df.head(5000)

# Configurações gerais para os gráficos
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Análise 1: Impacto de Estudos e Sono no Desempenho Acadêmico
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Hours_Studied', y='Exam_Score')
plt.title('Relação entre Horas de Estudo e Nota do Exame')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Sleep_Hours', y='Exam_Score')
plt.title('Relação entre Horas de Sono e Nota do Exame')
plt.show()

# Análise 2: Influência da Presença e Motivação
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Attendance', y='Exam_Score', hue='Motivation_Level', palette='viridis')
plt.title('Relação entre Frequência, Motivação e Nota do Exame')
plt.show()

# Análise 3: Recursos e Suporte Familiar
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Parental_Involvement', y='Exam_Score', hue='Access_to_Resources')
plt.title('Influência do Envolvimento Parental e Recursos Educacionais no Desempenho')
plt.show()

# Análise 4: Atividades Extracurriculares e Físicas
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Extracurricular_Activities', y='Exam_Score')
plt.title('Participação em Atividades Extracurriculares e Nota do Exame')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Physical_Activity', y='Exam_Score')
plt.title('Atividade Física Semanal e Nota do Exame')
plt.show()

# Análise 5: Tipo de Escola e Qualidade do Ensino
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='School_Type', y='Exam_Score', hue='Teacher_Quality')
plt.title('Impacto do Tipo de Escola e Qualidade do Ensino no Desempenho')
plt.show()

# Análise 6: Disponibilidade de Internet e Acesso a Recursos
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Internet_Access', y='Exam_Score', hue='Access_to_Resources')
plt.title('Influência do Acesso à Internet e Recursos no Desempenho')
plt.show()

# Análise 7: Renda Familiar e Distância da Escola
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Family_Income', y='Exam_Score', hue='Distance_from_Home')
plt.title('Impacto da Renda Familiar e Distância da Escola no Desempenho')
plt.show()

# Análise 8: Diferença de Desempenho entre Gêneros
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='Exam_Score')
plt.title('Diferença de Desempenho entre Gêneros')
plt.show()

# Análise 9: Motivação e Influência dos Colegas
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Peer_Influence', y='Exam_Score', hue='Motivation_Level')
plt.title('Influência da Motivação e do Ambiente Social no Desempenho')
plt.show()

# Análise 10: Necessidade de Apoio Extra e Dificuldades de Aprendizado
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Tutoring_Sessions', y='Exam_Score')
plt.title('Impacto das Aulas de Reforço no Desempenho')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='Learning_Disabilities', y='Exam_Score')
plt.title('Impacto das Dificuldades de Aprendizado no Desempenho')
plt.show()