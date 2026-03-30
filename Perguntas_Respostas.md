## QUESTÃO 3 — Matriz de decisão

1. Por que Plotly e não Matplotlib?
   Porque o Plotly permite interatividade (zoom, hover, filtros), facilitando a exploração dos dados em tempo real.

2. Quando usar gráfico estático?
   Quando o objetivo é apresentação em PDF ou relatório fixo, sem necessidade de interação.

3. Destino da análise?
   Mais voltado para dashboard/web, não PDF.

---

## QUESTÃO 4 — Insight (Barras)

O canal com maior receita lidera claramente as vendas, enquanto os demais ficam atrás com diferença significativa. Um gestor poderia investigar quais estratégias fizeram esse canal performar melhor.

---

## QUESTÃO 5 — Perguntas (Linha)

Existe tendência?
Sim, há variações ao longo do tempo.

Novembro e dezembro se destacam?
Sim, geralmente apresentam picos por sazonalidade (ex: fim de ano).

---

## QUESTÃO 5 — Insight

Há picos claros em determinados meses, indicando sazonalidade. Isso pode estar ligado a datas comerciais como Black Friday e Natal.

---

## QUESTÃO 6 — Perguntas (Scatter)

Existe correlação?
Sim, quanto maior a receita, maior tende a ser o lucro.

Existem outliers?
Sim, alguns pontos fogem do padrão.

---

## QUESTÃO 6 — Insight

A correlação é positiva entre receita e lucro. Outliers podem indicar problemas ou oportunidades específicas.

---

## QUESTÃO 7 — Mapa

Onde há maior concentração?
Regiões mais populosas tendem a concentrar mais vendas.

---

## QUESTÃO 8 — Tríade

Hover: mostra detalhes sem poluir o gráfico
Zoom: permite analisar períodos específicos
Legenda: ajuda a filtrar categorias

---

## QUESTÃO 9 — Plotly Express

1. O que é declarativo?
   Você diz o que quer mostrar, não como desenhar.

2. Facilita como?
   Menos código e mais produtividade.

3. Relação com dashboard?
   Facilita integração com ferramentas como Streamlit.

---

## QUESTÃO 10 — Clareza

O que foi melhorado?
Título, eixos e organização visual.

Ficou mais claro?
Sim, facilita o entendimento.

---

## QUESTÃO 11 — Interpretação

Gráfico 1:
Insight: canal dominante
Decisão: investir mais nele
Pergunta: por que performa melhor?

Gráfico 2:
Insight: sazonalidade
Decisão: planejar campanhas
Pergunta: quais eventos influenciam?

---

## QUESTÃO 13 — Mindset

1. Nome dos gráficos:
   fig_bar, fig_line, fig_scatter

2. Reaproveitamento:
   funções e estrutura de agregação

3. Padronização:
   nomes, layout e organização do código
