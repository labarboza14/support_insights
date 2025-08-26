import pandas as pd
from datetime import datetime

# -----------------------------
# 1. Carregar a planilha
# -----------------------------
df = pd.read_csv("atendimentos.csv", sep=";")  

# Converter datas
df["data_abertura"] = pd.to_datetime(df["data_abertura"], errors="coerce")

# Garantir colunas numéricas
df["tempo_resolucao_horas"] = pd.to_numeric(df["tempo_resolucao_horas"], errors="coerce")

# -----------------------------
# 2. Insights estratégicos
# -----------------------------

insights = {}

# 2.1. SLA: proporção de tickets fora do SLA por prioridade
sla_por_prioridade = (
    df.groupby("prioridade")["sla_compliance"]
    .apply(lambda x: (x == "FALSO").mean())
    .sort_values(ascending=False)
)
insights["% Tickets fora do SLA por prioridade"] = sla_por_prioridade

# 2.2. Desvio de resolução: quanto tempo, em média, os tickets fora do SLA estouram
desvio_sla = df[df["sla_compliance"] == "FALSO"]["tempo_resolucao_horas"].mean()
insights["Média de horas acima do SLA"] = desvio_sla

# 2.3. Tempo médio de resolução por status
tempo_por_status = df.groupby("status")["tempo_resolucao_horas"].mean().sort_values()
insights["Tempo médio de resolução por status"] = tempo_por_status

# 2.4. Priorização ineficiente: quando tickets de prioridade baixa foram resolvidos mais rápido que os de alta
ineficiencia = (
    df.groupby("prioridade")["tempo_resolucao_horas"].mean().sort_values()
)
insights["Tempo médio por prioridade (checar inversões)"] = ineficiencia

# 2.5. Identificar backlog oculto (tickets abertos há mais de X dias sem resolução)
hoje = datetime.now()
df["dias_abertos"] = (hoje - df["data_abertura"]).dt.days
backlog = df[(df["status"] != "resolvido") & (df["dias_abertos"] > 7)]
insights["Backlog crítico (abertos >7 dias)"] = backlog[["ticket_id","prioridade","dias_abertos"]]

# 2.6. Risco de reincidência: % de tickets de prioridade alta que ficaram fora do SLA
reincidencia_risco = (
    df[df["prioridade"] == "alta"]["sla_compliance"].value_counts(normalize=True)
)
insights["% de tickets alta prioridade fora do SLA"] = reincidencia_risco.get("FALSO", 0)

# 2.7. Tendência temporal: evolução de SLA por mês
df["mes"] = df["data_abertura"].dt.to_period("M")
sla_mes = (
    df.groupby("mes")["sla_compliance"]
    .apply(lambda x: (x == "VERDADEIRO").mean())
)
insights["Evolução mensal de cumprimento SLA"] = sla_mes

# -----------------------------
# 3. Recomendações práticas
# -----------------------------
def gerar_recomendacoes(insights):
    recomendacoes = []

    # SLA por prioridade
    sla_prioridade = insights["% Tickets fora do SLA por prioridade"]
    pior_prioridade = sla_prioridade.idxmax()
    if sla_prioridade.max() > 0.3:  
        recomendacoes.append(
            f"⚠️ Muitos tickets de prioridade '{pior_prioridade}' estão fora do SLA. "
            f"Reforce a equipe ou revise o fluxo de triagem para esse nível."
        )

    # Desvio de SLA
    if insights["Média de horas acima do SLA"] > 20:
        recomendacoes.append(
            "⏰ O estouro médio de SLA é alto. Sugestão: implementar alertas automáticos "
            "quando o ticket se aproximar do prazo limite."
        )

    # Priorização ineficiente
    tempos_prioridade = insights["Tempo médio por prioridade (checar inversões)"]
    if "alta" in tempos_prioridade.index and "baixa" in tempos_prioridade.index:
        if tempos_prioridade["alta"] > tempos_prioridade["baixa"]:
            recomendacoes.append(
                "🔄 Tickets de prioridade baixa estão sendo resolvidos mais rápido que os de alta. "
                "Revise critérios de priorização ou sobrecarga da equipe de alta prioridade."
            )

    # Backlog crítico
    backlog = insights["Backlog crítico (abertos >7 dias)"]
    if len(backlog) > 0:
        recomendacoes.append(
            f"📌 Existem {len(backlog)} tickets abertos há mais de 7 dias. "
            "Crie uma força-tarefa para revisar pendências antigas e evitar clientes insatisfeitos."
        )

    # Alta prioridade fora do SLA
    perc_alta_fora = insights["% de tickets alta prioridade fora do SLA"]
    if perc_alta_fora > 0.2:
        recomendacoes.append(
            "🔥 Mais de 20% dos tickets de alta prioridade estouram SLA. "
            "Sugestão: implementar atendimento dedicado (squad de incidentes críticos)."
        )

    # Tendência temporal
    tendencia_sla = insights["Evolução mensal de cumprimento SLA"]
    if len(tendencia_sla) > 1 and tendencia_sla.iloc[-1] < tendencia_sla.iloc[0]:
        recomendacoes.append(
            "📉 A taxa de cumprimento de SLA está caindo ao longo dos meses. "
            "Reveja processos, treinamentos e carga de trabalho para estancar a deterioração."
        )

    return recomendacoes


# -----------------------------
# 4. Exibir resultados
# -----------------------------
for titulo, valor in insights.items():
    print(f"\n### {titulo} ###")
    print(valor)

print("\n### Recomendações Estratégicas ###")
for rec in gerar_recomendacoes(insights):
    print(rec)

