# Yu-Gi-Oh! Forbidden Memories — Overhaul Mod

Projeto completo de modernização e rebalanceamento de **Yu-Gi-Oh! Forbidden Memories** (PS1 / PC), focado em **estratégia, respeito ao tempo do jogador e zero grind obrigatório**.

---

## 🌟 Principais Recursos do Mod

1. **Combate Justo (Estrelas Guardiãs Neutralizadas):**
   * O bônus aleatório de $\pm500$ das Estrelas Guardiãs foi completamente desativado no PC e no PS1.
   * O combate agora é vencido puramente por **ATK/DEF real**, cartas de **Equipamento** e efeitos de **Campo**.
2. **Revolução nas Fusões (39 Novas Fusões Lógicas):**
   * Árvores de fusão balanceadas para todas as famílias (Guerreiros/Ciborgues, Magos, Mares/Oceanos, Insetos/Plantas e Dragões).
   * Chega de depender apenas do Dragão Trovão de Duas Cabeças: qualquer arquétipo agora possui rotas viáveis para zerar a campanha.
3. **Receitas de Fusão na Descrição das Cartas:**
   * Aperte **Quadrado ($\square$)** no Baú ou no duelo para ler as combinações de fusão diretamente na tela do jogo!
4. **Fim do Grind Abusivo:**
   * **Multi-Drop:** 5 cartas concedidas por vitória em vez de 1.
   * **Loja de Senhas (Star Chips) Justa:** Custos absurdos de 999.999 reduzidos para 30 a 200 Star Chips.
   * **Drops Balanceados por Arquétipos:** Duelistas dos Atos 1 e 2 dropam as ferramentas temáticas de seus próprios baralhos.
5. **Auxiliar de Fusão na Tela (PC):**
   * Indicador nativo em tempo real avisando quando duas cartas da mão fundem.
6. **Versão Nativa de PC com Widescreen & 3D:**
   * Executável de PC sem necessidade de emuladores terceiros, com modelos 3D nos monstros e suporte nativo a controles.
   * Compatibilidade total com emuladores de PS1 no Android (DuckStation, RetroArch).

---

## 📂 Documentação Completa do Projeto

* 📖 [**Game Design Document (GDD.md)**](GDD.md): Visão geral de design, pilares, fórmulas, offsets mapeados na ROM e roadmap de desenvolvimento.
* 🔮 [**Catálogo de Fusões (FUSOES.md)**](FUSOES.md): Lista completa de todas as novas famílias, escadas de poder e receitas especiais.
* 📜 [**Lista Oficial de Senhas e Custos (LISTA_SENHAS.md)**](LISTA_SENHAS.md): Catálogo de todas as 722 cartas com senhas de 8 dígitos extraídas da ROM e seus respectivos custos em Star Chips.

---

## 🎮 Como Jogar

### No PC (Executável Nativo):
1. Coloque a sua imagem do jogo (`.bin`) na pasta `rom/` com o nome `Yu-Gi-Oh! Forbidden Memories (Mod).bin`.
2. Dê dois cliques no arquivo [`JOGAR_PC.bat`](JOGAR_PC.bat) na raiz do projeto.
3. O jogo iniciará diretamente em tela cheia/janela com Multi-Drop, Widescreen e modelos 3D ativos!

### No Android (DuckStation / RetroArch):
1. Copie os arquivos da pasta `rom/`:
   * `Yu-Gi-Oh! Forbidden Memories (Mod).bin`
   * `Yu-Gi-Oh! Forbidden Memories (Mod).cue`
2. No seu emulador de preferência no celular, selecione o arquivo `.cue` para carregar a versão modificada.

---

## 🛠️ Ferramentas & Scripts (`tools/`)

* `patch_guardian_stars.py`: Aplica a neutralização de $\pm500$ no executável PC e na ROM PS1.
* `inject_fusions.py`: Injeta as 39 novas fusões balanceadas diretamente na ROM.
* `patch_star_chips.py`: Rebalanceia os preços de Star Chips para cartas icônicas.
* `generate_card_descriptions.py`: Gera as descrições formatadas com as receitas de fusão.
* `setup_pc_game.py`: Vincula a ROM ao motor de PC e configura o save `.sav` / `.srm`.

---

## ⚖️ Licença e Direitos

Projeto desenvolvido para fins educacionais e de preservação histórica. Não distribuímos arquivos de imagem protegidos por direitos autorais (`.bin`/`.iso`). O mod aplica patches diretamente sobre a cópia legal do usuário.
