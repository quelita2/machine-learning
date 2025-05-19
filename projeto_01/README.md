# 💓 Predição de Doença Cardíaca com Regressão Logística em PyTorch

Este projeto tem como objetivo aplicar técnicas de Aprendizado de Máquina para prever a presença de doenças cardíacas com base em atributos clínicos dos pacientes. O estudo envolve desde a análise exploratória dos dados até a construção, treinamento e avaliação de um modelo de Regressão Logística implementado manualmente com PyTorch.

- 🔎 Encontre o dataset [aqui](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset/data)

---

## 🧪 Etapas do Projeto

### 1. 🔍 Análise Exploratória dos Dados

Nesta etapa inicial, foi realizada a leitura do conjunto de dados seguido de:

* Verificação de valores ausentes e registros incompletos.
* Gráficos e estatísticas descritivas para entender correlações entre variáveis.

### 2. 🧼 Preparação e Engenharia de Atributos

* Limpeza dos dados: remoção de registros com valores inválidos como `'?'`.
* Conversão de tipos: transformação de atributos categóricos em variáveis numéricas com `OneHotEncoder` e `OrdinalEncoder`.
* Padronização: uso de `StandardScaler` para normalizar os atributos contínuos.
* Encapsulamento em um pipeline completo (`ColumnTransformer`), garantindo reprodutibilidade e organização.

### 3. 🧠 Implementação do Modelo em PyTorch

* A regressão logística foi implementada manualmente, utilizando as operações vetoriais do PyTorch.
* A estrutura do modelo segue a definição tradicional:

  $$
  \hat{y} = \sigma(XW + b)
  $$
* Utilizando BCELoss (Binary Cross Entropy) como função de perda, e o otimizador SGD (Stochastic Gradient Descent).

### 4. 🏋️ Treinamento do Modelo

* O dataset foi dividido em conjuntos de treino e teste (validação).
* O treinamento foi realizado por 100 épocas, onde a perda (loss) foi monitorada e decresceu gradualmente.
* Foram utilizados gradientes manuais com `loss.backward()` e `optimizer.step()` para atualizar os pesos.

### 5. 📊 Avaliação e Documentação dos Resultados

* O modelo foi avaliado com:

  * **Acurácia**
  * **Precisão**
  * **Recall**
  * **F1-score**
* Uma matriz de confusão foi gerada para visualizar os erros do classificador.

#### 🎯 Resultados:

(projeto_01\assets\metrics.png)

O modelo de predição de doenças cardíacas obteve uma acurácia de 64%, ou seja, **acertou 64% dos diagnósticos**. A matriz de confusão mostra que ele acertou 109 casos em que a pessoa não tinha a doença e 64 casos em que a pessoa realmente tinha. Por outro lado, errou 41 vezes ao indicar doença em quem não tinha e 55 vezes ao não detectar a doença em quem tinha. A precisão foi de 66% para pessoas sem a doença e 61% para quem tinha. O recall foi de 73% para casos negativos e 54% para positivos. O F1-score, que equilibra precisão e recall, foi de 69% para quem não tinha a doença e 57% para quem tinha. Esses números mostram que **o modelo tem desempenho razoável**, mas ainda pode ser melhorado, principalmente na detecção de casos positivos.


#### 🧾 Interpretação:

* O modelo apresenta desempenho moderado, com maior eficácia para prever pacientes saudáveis.
* A presença de falsos negativos (doente classificado como saudável) pode ser crítica em aplicações reais.
* Há espaço para melhorias com:

  * Técnicas de balanceamento de classes
  * Modelos mais complexos como Random Forest ou Redes Neurais

---

## 📉 Visualizações

(projeto_01\assets\matrix_confusion.png)
|                   | **Predito Saudável** | **Predito Doente** |
| ----------------- | -------------------- | ------------------ |
| **Real Saudável** | 109 (Verdadeiro Positivo)       | 41 (Falso Negativo)        |
| **Real Doente**   | 55 (Falso Positivo)          | 64 (Verdadeiro Negativo)        |

---

## 📁 Estrutura do Projeto

```text
📂 Projeto_01/
├── 📜 README.md
├── 📁 src         # Códigos com todas as etapas
├── 📁 assets/                 # Docs e Imagens
└── 📁 data/       # dasets
```

---

<div align="center">
  📚 PPGEEC2318 - Aprendizado de Máquina🎓 <br/>
  Universidade Federal do Rio Grande do Norte - Departamento de Computação Aplicada (DCA). 🏛️
</div>