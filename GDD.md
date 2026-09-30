# Game Design Document (GDD) — Yu-Gi-Oh! Forbidden Memories (Overhaul Mod)

## 1. Visão Geral do Projeto
* **Jogo Base:** *Yu-Gi-Oh! Forbidden Memories* (PlayStation 1 - PT-BR)
* **Objetivo:** Transformar a experiência de *Forbidden Memories* em um jogo mais justo, estratégico, fluido e intuitivo, removendo o *grind* abusivo e frustrações históricas do motor original, respeitando as limitações de hardware do PS1.
* **Filosofia Central (Respeito ao Tempo do Jogador):**
  * O jogador alvo trabalha, tem rotina corrida e busca uma **diversão saudável, inteligente e fluida**.
  * A dificuldade deve existir e ser desafiadora (recompensando estratégia e conhecimento de fusões), mas **nunca punitiva através de horas de repetição forçada**.
  * Cada sessão de jogo (mesmo curta, de 20 a 30 minutos no celular ou PC) deve trazer sensação palpável de progresso e conquista.
* **Plataformas Alvo:** Emuladores de PS1 no Android (ex: DuckStation) e PC.

---

## 2. Pilares de Design

### Pilar I: Fim da Aleatoriedade das Estrelas Guardiãs
* **Problema:** O bônus arbitrário de +500 de ATK/DEF baseado no ciclo planetário (Sol > Lua > Vênus, etc.) invalida o valor real das cartas e cria derrotas injustas.
* **Solução:** Neutralizar o bônus de vantagem planetária (zerar o modificador no cálculo de dano).
* **Impacto:** O combate passa a ser decidido **puramente pelo ATK e DEF reais** e pelo uso inteligente de cartas de equipamento/campo.

### Pilar II: Revolução nas Fusões e Informação Acessível
* **Problema:** O jogo original exige consultar tabelas e guias externos para descobrir fusões, além de possuir dezenas de combinações ilógicas.
* **Soluções:**
  1. **Fórmulas na Descrição da Carta:** Atualizar o texto de biblioteca/inspeção de cada carta chave para exibir suas principais famílias e receitas de fusão diretamente na tela.
  2. **Fusões Lógicas e Intuitivas:** Mapeamento consistente por tipos (ex: *Dragão + Trovão*, *Guerreiro + Zumbi*, *Mago + Trevas*, etc.).
  3. **Aproveitamento do Catálogo (Novas Cartas):** Substituição de cartas repetidas ou inúteis de 722 por cartas icônicas e variantes viáveis.

### Pilar III: Fim do Grind Abusivo (Economia e Recompensas)
* **Problema:** Taxas de drop de 0,02% ou 0% tornavam a progressão impraticável sem emular 500+ duelos repetitivos com os mesmos personagens.
* **Soluções:**
  1. **Tabelas de Drop Balanceadas:**
     * **S/A POW:** Cartas de monstros com progressão linear de poder conforme o duelista enfrentado.
     * **B/C/D TEC:** Cartas mágicas e armadilhas estratégicas (*Raigeki*, *Megamorfo*, *Espadas*, etc.).
  2. **Multiplicador de Drops (Multi-Drop):** Conceder mais cartas por vitória (ex: 3 a 5 cartas por duelo) para valorizar o tempo do jogador.
  3. **Loja de Senhas (Star Chips) Viável:** Redução dos custos astronômicos (de 999.999 para valores alcançáveis entre 30 e 300 Star Chips).

### Pilar IV: Campanha Fluida (Zero Farm Obrigatório)
* **Problema:** Picos abruptos de dificuldade (ex: chefes saltando de 1500 ATK para 3500 ATK) criavam muros artificiais que travavam o progresso.
* **Soluções:**
  1. **Curva em Escada Orgânica:** Progressão contínua de poder nos decks adversários (Egito inicial -> Torneio -> Templos -> Reta final).
  2. **Recompensas como Ferramentas:** Cada chefe derrotado fornece cartas que capacitam o jogador para o desafio seguinte (estilo RPG / Mega Man), permitindo zerar a história sem pausas para *farm*.

### Pilar V: Fator Replay e Desbloqueio Progressivo de Decks
* **Decisão do Deck Inicial:** Manter o espírito clássico de começar com um deck básico e humilde. A graça está em valorizar cada carta conquistada e usar a inteligência em fusões para superar os primeiros oponentes.
* **Sistema de Desbloqueio de Decks (Progressão e Replay):**
  * Conforme o jogador derrota duelistas-chave na campanha (ex: Joey, Mai, Kaiba, Guardiões dos Templos), são liberados conjuntos temáticos ou receitas de decks completos daquele arquétipo.
  * O jogador sente que está conquistando o arsenal dos próprios adversários.
  * Permite alternar estilos de jogo na campanha e no Free Duel sem precisar de *grind*.

---

## 3. Estrutura de Progressão e Desbloqueios

| Fase / Ato | Duelistas Chave | Faixa de ATK Inimigo | Recompensas / Desbloqueios |
| :--- | :--- | :--- | :--- |
| **Ato 1: Egito Antigo (Início)** | Simon Muran, Teana, Jono, Seto 1st | 400 – 1200 | Primeiras fusões básicas, cartas de suporte iniciais |
| **Ato 2: Torneio no Japão** | Rex, Weevil, Mai, Bandit Keith, Shadi, Yami Bakura | 1200 – 2000 | Desbloqueio dos Arquétipos: Dinossauros, Insetos, Guerreiros/Harpia, Máquinas |
| **Ato 3: Retorno e os Templos** | Guardiões (Oceano, Deserto, Prado, Montanha, Floresta) | 2000 – 2600 | Desbloqueio das cartas de Campo elementais e monstros de topo de cada elemento |
| **Ato 4: O Clímax** | Labyrinth Mage, Sebek, Neku, Heishin, Seto 3rd, DarkNite | 2600 – 3500 | Monstros supremos, magias lendárias (*Raigeki*, *Megamorfo*) sem depender de sorte absurda |

---

## 4. Árvore de Famílias de Fusão (Escadas de Poder Balanceadas)

Cada família possui uma escada de poder coerente (Básico -> Avançado -> Mestre), permitindo que qualquer combinação de arquétipo chegue ao nível de competição dos chefes:

1. **Guerreiros & Ciborgues:**
   * `Guerreiro + Zumbi` -> Guerreiro Zumbi (1200) -> Zumbi Blindado (1500) -> Cavaleiro Cadáver Maldito (2300+)
   * `Guerreiro + Máquina` -> Soldado Cibernético (1500) -> Giga-Tech Wolf (2000) -> Cavaleiro Mecânico Supremo (2600+)
2. **Magos & Ocultismo:**
   * `Mago + Trevas/Zumbi` -> Fantasma Mágico (1300) -> Mago Negro (2500)
   * `Mago + Fogo` -> Guerreiro da Chama (1800) -> Mago de Fogo Solar (2400)
3. **Mares & Oceanos:**
   * `Peixe/Água + Dragão` -> Serpente Marinha (1800) -> Dragão dos Picos Aquáticos (2250) -> Levia-Dragon (2700+)
4. **Natureza & Insetos:**
   * `Inseto + Máquina` -> Besouro Canhão (2100) -> Hércules Blindado (2650+)
   * `Planta + Fera` -> Quimeras Silvestres (2000 – 2400)
5. **Dragões & Trovão:**
   * Mantidos como uma das rotas viáveis, mas agora em paridade com as outras famílias.

---

## 5. Registro de Decisões Técnicas e Mapeamento da ROM

### Estrutura do Disco (ISO9660 / Mode 2 Form 1)
* **Tamanho do Arquivo BIN:** 517.872.768 bytes (~493.88 MB).
* **Estrutura de Setores:** RAW 2352 bytes por setor (24 bytes de cabeçalho Sync/Subheader + 2048 bytes de dados úteis por setor).
* **Arquivos Chave Mapeados:**
  * `SLUS_014.11`: LBA 25 (1.902.592 bytes) — Executável PS-X MIPS R3000A (Endereço de Carga RAM: `0x80010000`).
  * `DATA/WA_MRG.MRG`: LBA 10102 (37.748.736 bytes) — Arquivo mestre contendo o banco de dados de cartas, senhas, custos, fusões e drops.

### Offsets Críticos Mapeados em `WA_MRG.MRG`:
1. **Tabela de Senhas e Custos de Cartas (Star Chips):**
   * **Offset em WA_MRG:** `0xFB9800`
   * **Formato:** Registro de 8 bytes por carta (4 bytes de Custo + 4 bytes de Senha codificada em BCD/Hex).
   * **Exemplos Confirmados:**
     * Carta #001 (Dragão Branco de Olhos Azuis): Custo `999.999` (0x000F423F) | Senha `89631139`
     * Carta #002 (Elfa Mística): Custo `160` (0x000000A0) | Senha `15025844`
     * Carta #004 (Dragão Bebê): Custo `999.999` (0x000F423F) | Senha `88819587`
2. **Tabela de Fusões:**
   * **Offset em WA_MRG:** `0xF8F802`
   * **Formato:** Matriz/listas com flags de tipo e ID de carta terminadas por delimitadores `0xFFFE`.
3. **Decks e Drops dos Duelistas:**
   * Localizados na faixa entre `0xF80000` e `0xF8E000` de `WA_MRG.MRG`.

### Executável Nativo de PC (Yu-Gi-Oh! Recompiled)
* **Localização:** [`pc_game/yfm-redecomp-v0.1.2/memories-pc.exe`](file:///c:/Users/Gustavo/Documents/Projetos%20Antigravity/Yu-Gi-Oh!%20Forbidden%20Memories/pc_game/yfm-redecomp-v0.1.2/memories-pc.exe)
* **Atalho Rápido:** [`JOGAR_PC.bat`](file:///c:/Users/Gustavo/Documents/Projetos%20Antigravity/Yu-Gi-Oh!%20Forbidden%20Memories/JOGAR_PC.bat) na raiz do projeto (abre o jogo nativo diretamente com 2 cliques).
* **Vínculo com a ROM:** O arquivo [`rom/Yu-Gi-Oh! Forbidden Memories (Mod).bin`](file:///c:/Users/Gustavo/Documents/Projetos%20Antigravity/Yu-Gi-Oh!%20Forbidden%20Memories/rom/Yu-Gi-Oh!%20Forbidden%20Memories%20(Mod).bin) está vinculado dinamicamente na pasta `game/` do executável. Qualquer patch aplicado na ROM reflete instantaneamente no jogo de PC!

### Offsets de Batalha (Estrelas Guardiãs) Neutralizados:
* **Executável PC (`memories-pc.exe`):**
  * `Duel_CalcGuardianStarBonus`: Offset `0x00240216` (`xor eax, eax; ret`).
  * `Duel_CalcGuardianStarMatchup`: Offset `0x00240576` (`xor eax, eax; ret`).
* **PS1 ROM (`SLUS_014.11` no `.bin`):**
  * `Duel_CalcGuardianStarMatchup`: SLUS `0x1D380` / BIN `0x0002FE28` (`jr ra; move v0, zero`).
  * `Duel_CalcGuardianStarBonus`: SLUS `0x1D3F4` / BIN `0x0002FE9C` (`jr ra; move v0, zero`).
* **Resultado:** O bônus de ±500 de Estrelas Guardiãs foi 100% extinto em ambas as plataformas. Monstros vencem puramente por ATK/DEF, equipamentos e campos.

---

## 6. Backlog de Sugestões e Próximos Passos (Roadmap)

Este painel centraliza todas as sugestões aprovadas para manter a conversa ágil e limpa:

- [x] **Mapeamento completo da imagem ISO/BIN do PS1** (arquivos, LBAs e setores Mode 2 Form 1).
- [x] **Mapeamento dos offsets de cartas, custos, senhas e fusões** em `WA_MRG.MRG`.
- [x] **Primeiro teste de patch bem-sucedido:** Rebalanceamento de Star Chips para cartas icônicas (`patch_star_chips.py`).
- [x] **Configuração do Executável Nativo de PC** ([`JOGAR_PC.bat`](file:///c:/Users/Gustavo/Documents/Projetos%20Antigravity/Yu-Gi-Oh!%20Forbidden%20Memories/JOGAR_PC.bat) com suporte a Widescreen, controles e modelos 3D).
- [x] **Reaproveitamento de Save (.srm):** Conversão do arquivo `.srm` para o `slot01.sav` nativo.
- [x] **Ativação do Multi-Drop:** 5 cartas por vitória configuradas (`card_drops = 5`).
- [x] **Ativação do Indicador de Fusões na Tela:** Assistente nativo ativado (`fusion_helper = 1`).
- [x] **Rebalanceamento de Drops do Ato 1:** Drops justos configurados para Simon Muran, Teana, Jono 1st (*Baby Dragon*, *Time Wizard*) e Seto 1st.
- [x] **Criação do Catálogo de Famílias de Fusão** ([`FUSOES.md`](file:///c:/Users/Gustavo/Documents/Projetos%20Antigravity/Yu-Gi-Oh!%20Forbidden%20Memories/FUSOES.md)).
- [x] **Mapeamento e Injeção das Novas Famílias de Fusão:** 39 novas fusões balanceadas injetadas e ativas no motor do jogo (`inject_fusions.py`).
- [x] **Neutralização do Bônus Planetário (+500 das Estrelas Guardiãs):** Patch aplicado e verificado tanto no executável PC quanto na ROM PS1 (`patch_guardian_stars.py`).
- [x] **Rebalanceamento de Drops do Ato 2 (Torneio):** Rex, Weevil, Mai, Keith, Shadi, Bakura e Kaiba 1st com tabelas de arquétipos justas.
- [x] **Injeção de Receitas na Descrição das Cartas:** 25 cartas-chave atualizadas com fórmulas de fusão legíveis e formatadas (`text.txt` e `generate_card_descriptions.py`).
- [x] **Rebalanceamento de Drops do Ato 3 (Templos e Guardiões):** Ocean Mage, Forest Mage, Mountain Mage, Desert Mage, Meadow Mage, High Mages (Secmeton, Anubisius, Atenza, Martis, Kepura) e Jono/Teana 2nd.
- [ ] **Rebalanceamento de Drops do Ato 4 (A Reta Final):** Labyrinth Mage, Sebek, Neku, Heishin 1st/2nd, Seto 2nd/3rd, DarkNite e Nitemare.



