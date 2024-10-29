# PROJETO GYM 

## REQUISITOS DO PROJETO
Requisitos de Negócio e Funcionalidades da Web App MVP (Minimum Viable Product)

   * A Web App deve permitir que a academia crie e edite membros.

   * A Web App deve permitir que a academia crie e edite atividades.

   * A Web App deve permitir que a academia crie e edite instrutores.

   * A Web App deve permitir que a academia agende os membros nas atividades.

   * A Web App deve mostrar uma lista de todas as próximas atividades.

   * A Web App deve mostrar todos os membros que estão agendados para uma determinada atividade.

   ## CASOS DE USO 
   ![CASO DE USO](/Projeto/pic/Casos%20de%20USO.drawio(1).png)

  ## Projeto de Arquitetura do Banco de Dados
  
  ![Modelagem do Banco de Dados](/Projeto/pic/modelagem-banco-dados.png)

**Descrição nos ícones nas tabelas:**

• Os símbolos de chave indicam chaves primárias.

• As setas azuis indicam chaves estrangeiras que estabelecem os relacionamentos.

• As setas amarelas indicam que a chave primária está sendo referenciada por uma
chave estrangeira em outra tabela.


**Descrição das tabelas:**

**Tabela de Planos** – cadastro de planos disponíveis na academia (mensal, semestral e
anual).

**Tabela de Instrutores** – cadastro de instrutores que realizam atividades na
academia.

**Tabela de Membros** – cadastro de membros (clientes). Cada cliente está associado a
um plano.

**Tabela de Atividades** – cadastro de atividades realizadas na academia. Cada
atividade está associada a um instrutor e a um plano.

**Tabela de Agendamentos** – cadastro de reservas dos membros nas atividades.