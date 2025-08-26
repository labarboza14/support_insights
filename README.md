# 📊 Case de Estudo: Análise de Atendimentos de Suporte Técnico

Este projeto é um **estudo de caso prático** sobre **análise de dados em suporte técnico**, criado para simular a realidade de uma operação de atendimento.
A ideia é mostrar como transformar uma planilha de tickets em **insights relevantes e recomendações acionáveis** que agreguem valor para a gestão.

---

## 🎯 Objetivo do Projeto

* Demonstrar como **analisar tickets de suporte** de forma estruturada.
* Ir além de métricas básicas, gerando **insights estratégicos** (priorização, eficiência, riscos).
* Criar um **fluxo de ponta a ponta**: dados fictícios → análise → recomendações práticas.
* Ser um **material didático** para iniciantes e um **exemplo de raciocínio analítico** para profissionais.

---

## 🏗️ Construção do Projeto

1. **Criação do Dataset**

   * Uma planilha fictícia (`atendimentos.csv`) com **40 registros simulados**.
   * Colunas:

     * `ticket_id` → Identificação do chamado
     * `status` → Estado atual (resolvido, pendente, etc.)
     * `prioridade` → Baixa, média, alta, urgente
     * `tempo_resolucao_horas` → Tempo gasto até a resolução
     * `sla_compliance` → Se respeitou o SLA (`VERDADEIRO` / `FALSO`)
     * `data_abertura` → Data de abertura do chamado

2. **Processamento dos Dados**

   * Uso do **Pandas** para leitura e manipulação da planilha.
   * Conversão de datas, criação de colunas adicionais (como `dias_abertos`).

3. **Geração de Insights**

   * Métricas de SLA por prioridade.
   * Análise do tempo médio de resolução por status e prioridade.
   * Identificação de backlog crítico.
   * Tendência temporal de cumprimento de SLA.
   * Risco de reincidência em tickets críticos.

4. **Recomendações Estratégicas**

   * Transformar os números em **ações concretas**.
   * Exemplo:

     * “Muitos tickets de prioridade **alta** fora do SLA → Criar squad dedicado a incidentes críticos.”
     * “Backlog com chamados antigos → Criar força-tarefa para limpar pendências.”

---

## 📈 Exemplos de Insights

* **% Tickets fora do SLA por prioridade**
  Se prioridade **alta** apresenta pior índice → risco de churn de clientes estratégicos.

* **Tempo médio por prioridade (checar inversões)**
  Se tickets de **baixa** prioridade são resolvidos mais rápido que **alta** → problema de priorização.

* **Backlog crítico**
  Chamados abertos há mais de 7 dias sem resolução → necessidade de força-tarefa.

* **Evolução mensal de SLA**
  Mostra se a operação está **melhorando ou piorando** ao longo do tempo.

---

## 🔥 Exemplos de Recomendações

* ⚠️ Reforçar a equipe em tickets de **alta prioridade**, que estão estourando SLA.
* 🔄 Revisar **critérios de priorização**, pois chamados de baixa prioridade estão sendo resolvidos mais rápido.
* 📌 Criar **força-tarefa para backlog**, limpando tickets abertos há mais de 7 dias.
* ⏰ Implementar **alertas automáticos de SLA**, prevenindo estouros antes que ocorram.
* 📉 Se o SLA mensal está caindo → revisar processos e carga de trabalho da equipe.

---

## 🛠️ Como Executar o Projeto

### 1. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Instalar dependências

```bash
pip install pandas
```

### 3. Rodar o script

```bash
python main.py
```

### 4. Arquivos do projeto

* `atendimentos.csv` → Base fictícia de tickets.
* `main.py` → Script de análise e recomendações.

---

## 💡 Aprendizados

* Como manipular e analisar dados com **Pandas**.
* Como transformar **métricas em insights estratégicos**.
* Importância de traduzir números em **recomendações acionáveis** para gestão.
* Como estruturar um **projeto de portfólio** que mostra raciocínio técnico e visão de negócios.

---

## 🚀 Próximos Passos

* Adicionar **visualizações gráficas** (Matplotlib/Seaborn).
* Criar um **dashboard interativo** (Streamlit ou Dash).
* Simular integração com ferramentas de suporte reais (Zendesk, Jira).

---

## 🤝 Contribuições

Este repositório é aberto para quem quiser usar como **material de estudo**.
Sinta-se à vontade para sugerir melhorias, adicionar novos insights ou criar variações do projeto!

---
