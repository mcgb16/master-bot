# Master Bot 🧙‍♂️

## Como adicionar ao seu servidor 🖥

Olá! Para você adicionar esse bot ao seu servidor do discord, basta clicar neste link: https://discord.com/oauth2/authorize?client_id=1182007158154481784&permissions=Ol%C3%A1!%20Para%20voc%C3%AA%20adicionar%20esse%20bot%20ao%20seu%20servidor%20do%20discord,%20basta%20clicar%20neste%20link:%20Permissions%20Integer%20=%20945161333840&scope=bot

## Comandos 📓

### Rodar Dados 🎲
##### ?roll
Este comando serve para rolar os dados durante o jogo. Ele recebe apenas um argumento que é o: {número}d{número}. Explicando de forma mais aprofundada, o número da esquerda indica a quantidade de dados que serão rodados (caso não seja informado, será considerado o número 1 por padrão). Já o número da direita indica o número de faces do dado.

Exemplos de uso do comando com as respostas do bot:
![Alt text](/photos/roll_cmd.png)

### Players 🕹
Comandos utilizados para configurar os personagens que os jogadores irão utilizar durante o seu jogo. Nada impede de um jogador controlar um NPC, entretanto o recomendado é respeitar a diferenciação entre os dois tipos de personagens.

##### ?cplayer
Este comando é utilizado para efetuar a criação de personagens jogáveis. Para isto, alguns atributos são obrigatórios, como: nome, força, destreza, constituição, sabedoria, inteligência, vida e carisma. Além destes 8 atributos, temos o de ouro, que por sua vez não é obrigatório. O bot aceita algumas formas diferentes de se escrever cada um dos atributos, sendo possível escrever abreviações para facilitar durante a criação. Para saber todas essas formas, dê uma olhadinha no final dessa documentação.

Exemplo de uso do comando com a resposta do bot:

##### ?uplayer
Este comando é utilizado para efetuar atualizações nos personagens jogáveis já criados. Para isto o único atributo obrigatório é o ID, o qual é fornecido logo após efetuar a criação de um personagem jogável (vide documentação do comando anterior de criação). Os IDs são únicos, ou seja, cada personagem tem o seu próprio ID. Assim que você informar o ID do personagem o qual deseja atualizar, insira os atributos os quais deseja atualizar também. Lembre-se: você pode atualizar quantos atributos quiser ao mesmo tempo.

Exemplo de uso do comando com a resposta do bot:

##### ?splayer
Este comando é utilizado para efetuar buscas de personagens jogáveis na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do personagem, o qual é fornecido logo após efetuar a criação de um personagem jogável (vide documentação do comando de criação). Os IDs são únicos, ou seja, cada personagem tem o seu próprio ID.

Exemplo de uso do comando com a resposta do bot:

### NPCs 🤖
Comandos utilizados para configurar os NPCs. Nada impede de um jogador controlar um NPC, entretanto o recomendado é respeitar a diferenciação entre os dois tipos de personagens. Os NPCs também possuem atributos devido a sua possível em combates tanto ao lado, quanto contra, os jogadores.

##### ?cnpc
Este comando é utilizado para efetuar a criação de NPCs. Para isto, alguns atributos são obrigatórios, como: nome, força, destreza, constituição, sabedoria, inteligência, vida e carisma. Além destes 8 atributos, temos o de ouro, que por sua vez não é obrigatório. O bot aceita algumas formas diferentes de se escrever cada um dos atributos, sendo possível escrever abreviações para facilitar durante a criação. Para saber todas essas formas, dê uma olhadinha no final dessa documentação.

Exemplo de uso do comando com a resposta do bot:

##### ?unpc
Este comando é utilizado para efetuar atualizações nos NPCs já criados. Para isto o único atributo obrigatório é o ID, o qual é fornecido logo após efetuar a criação de um NPC (vide documentação do comando anterior de criação). Os IDs são únicos, ou seja, cada NPC tem o seu próprio ID. Assim que você informar o ID do NPC o qual deseja atualizar, insira os atributos os quais deseja atualizar também. Lembre-se: você pode atualizar quantos atributos quiser ao mesmo tempo.

Exemplo de uso do comando com a resposta do bot:

##### ?snpc
Este comando é utilizado para efetuar buscas de NPCs na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do NPC, o qual é fornecido logo após efetuar a criação de um NPC (vide documentação do comando de criação). Os IDs são únicos, ou seja, cada NPC tem o seu próprio ID.

Exemplo de uso do comando com a resposta do bot:

### Itens ⚙
Comandos utilizados para efetuar a configuração de itens a serem utilizados durante o jogo.

##### ?citem
Este comando é utilizado para efetuar a criação de itens. Para isto, a única informação necessária é o nome dele.

Exemplo de uso do comando com a resposta do bot:

##### ?uitem
Este comando é utilizado para efetuar atualizações nos itens já criados. Para isto, o único atributo obrigatório é o ID, o qual é fornecido logo após efetuar a criação de um item (vide documentação do comando de criação de itens). Os IDs são únicos, ou seja, cada item tem o seu próprio ID. Como os itens possuem apenas o atributo de nome, após informar o ID basta informar o nome que estará tudo correto.

Exemplo de uso do comando com a resposta do bot:

##### ?sitem
Este comando é utilizado para efetuar buscas de itens na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do item, o qual é fornecido logo após efetuar a criação de um item (vide documentação do comando de criação de itens). Os IDs são únicos, ou seja, cada item tem o seu próprio ID.

Exemplo de uso do comando com a resposta do bot:

##### ?bitem
Este comando é utilizado para efetuar a vinculação de itens aos personagens (seja ele jogável ou NPC). Para efetuar essa vinculação, é necessário informar tanto o ID do item, quanto o ID do NPC e/ou player. Lembre-se, é possível que itens estejam vinculados tanto a NPCs quanto a players, entretanto ele pode estar vinculado a somente um de cada.

Exemplo de uso do comando com a resposta do bot:

### Armas 🏹
Comandos utilizados para efetuar a configuração de armas a serem utilizadas durante o jogo.

##### ?cweapon
Este comando é utilizado para efetuar a criação de armas. Para isto, as informações necessárias são: nome, dano e tipo de dano.

Exemplo de uso do comando com a resposta do bot:

##### ?uweapon
Este comando é utilizado para efetuar atualizações nas armas já criadas. Para isto, o único atributo obrigatório é o ID, o qual é fornecido logo após efetuar a criação de uma arma (vide documentação do comando de criação de armas). Os IDs são únicos, ou seja, cada arma tem o seu próprio ID. Assim como os outros comandos de atualização, é possível atualizar quantos atributos quiser de uma vez.

Exemplo de uso do comando com a resposta do bot:

##### ?sweapon
Este comando é utilizado para efetuar buscas de armas na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do arma, o qual é fornecido logo após efetuar a criação de um arma (vide documentação do comando de criação de armas). Os IDs são únicos, ou seja, cada arma tem o seu próprio ID.

Exemplo de uso do comando com a resposta do bot:

##### ?bweapon
Este comando é utilizado para efetuar a vinculação de armas aos personagens (seja ele jogável ou NPC). Para efetuar essa vinculação, é necessário informar tanto o ID da arma, quanto o ID do NPC e/ou player. Lembre-se, é possível que armas estejam vinculadas tanto a NPCs quanto a players, entretanto ela pode estar vinculado a somente um de cada.

Exemplo de uso do comando com a resposta do bot:

### Ajuda ⁉
Alguns comandos específicos que podem ser utilizados diretamente no bot para uma ajuda rápida referente aos comandos. Lembrando, essa ajuda não será tão aprofundada quanto a presente nesta documentação.

##### ?h
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos de uma vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:

##### ?h player
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos relacionados aos players de uma vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:

##### ?h npc
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos relacionados aos NPCs de uma vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:

##### ?h item
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos relacionados aos itens de uma vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:

##### ?h weapon
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos relacionados às armas de uma vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:

##### ?h dice
Este comando é utilizado para trazer uma ajuda geral referente a todos os comandos relacionados aos dados vez. Lembre-se: todos os comandos de ajuda possuirão o link desta documentação em seu rodapé.

Exemplo de uso do comando com a resposta do bot:


## Atributos
Formas que o bot aceita de os atributos serem escritos. Não se preocupe com letras maiúsculas e minúsculas, isso é irrelevante ao bot.

### Nome
- Nome
- Name

### Força
- Força
- Strength
- Str
- For

### Destreza
- Destreza
- Dexterity
- Dex
- Des

### Constituição
- Constituição
- Constitution
- Cons
- Const
- Con

### Inteligência
- Inteligência
- Intelligence
- Int

### Sabedoria
- Sabedoria
- Wisdom
- Sab
- Wis

### Carisma
- Carisma
- Charisma
- Car
- Char

### HP
- Vida
- HP
- Health

### Ouro
- Ouro
- Gold
- G

### Dano
- Dano
- Damage
- Dmg

### Tipo de Dano
- Tipo
- Type

### Player
- Player
- Pl

### NPC
- Npc

### ID
- Id