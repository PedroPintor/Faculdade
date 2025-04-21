--
-- File generated with SQLiteStudio v3.4.17 on seg abr 21 17:09:14 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: contribuinte
CREATE TABLE IF NOT EXISTS contribuinte (
    cpf      INT          PRIMARY KEY,
    nome     VARCHAR (20) NOT NULL,
    endereco VARCHAR (60),
    telefone VARCHAR (15) 
);

INSERT INTO contribuinte (
                             cpf,
                             nome,
                             endereco,
                             telefone
                         )
                         VALUES (
                             10020030040,
                             'pedro',
                             'rua artur',
                             '179999999'
                         );

INSERT INTO contribuinte (
                             cpf,
                             nome,
                             endereco,
                             telefone
                         )
                         VALUES (
                             11122233344,
                             'gabriel',
                             'rua pereira',
                             '189999999'
                         );

INSERT INTO contribuinte (
                             cpf,
                             nome,
                             endereco,
                             telefone
                         )
                         VALUES (
                             44433322211,
                             'augusto',
                             'rua menes',
                             '159999999'
                         );

INSERT INTO contribuinte (
                             cpf,
                             nome,
                             endereco,
                             telefone
                         )
                         VALUES (
                             12332122211,
                             'jarvis',
                             'rua tec',
                             '119999999'
                         );

INSERT INTO contribuinte (
                             cpf,
                             nome,
                             endereco,
                             telefone
                         )
                         VALUES (
                             22233311144,
                             'thor',
                             'rua odin',
                             '229999999'
                         );


-- Table: contribuinte_malha_fina
CREATE TABLE IF NOT EXISTS contribuinte_malha_fina (
    valor                 INT     NOT NULL,
    quantidade_prestacoes INT     NOT NULL,
    malha_fina_id         INTEGER,
    cpf_contribuinte      INT,
    FOREIGN KEY (
        malha_fina_id
    )
    REFERENCES malha_fina (id),
    FOREIGN KEY (
        cpf_contribuinte
    )
    REFERENCES contribuinte (cpf) 
);

INSERT INTO contribuinte_malha_fina (
                                        valor,
                                        quantidade_prestacoes,
                                        malha_fina_id,
                                        cpf_contribuinte
                                    )
                                    VALUES (
                                        500,
                                        5,
                                        1,
                                        10020030040
                                    );

INSERT INTO contribuinte_malha_fina (
                                        valor,
                                        quantidade_prestacoes,
                                        malha_fina_id,
                                        cpf_contribuinte
                                    )
                                    VALUES (
                                        700,
                                        7,
                                        2,
                                        11122233344
                                    );

INSERT INTO contribuinte_malha_fina (
                                        valor,
                                        quantidade_prestacoes,
                                        malha_fina_id,
                                        cpf_contribuinte
                                    )
                                    VALUES (
                                        900,
                                        9,
                                        3,
                                        44433322211
                                    );

INSERT INTO contribuinte_malha_fina (
                                        valor,
                                        quantidade_prestacoes,
                                        malha_fina_id,
                                        cpf_contribuinte
                                    )
                                    VALUES (
                                        600,
                                        6,
                                        4,
                                        12332122211
                                    );

INSERT INTO contribuinte_malha_fina (
                                        valor,
                                        quantidade_prestacoes,
                                        malha_fina_id,
                                        cpf_contribuinte
                                    )
                                    VALUES (
                                        750,
                                        10,
                                        5,
                                        22233311144
                                    );


-- Table: declaracao_imposto_renda
CREATE TABLE IF NOT EXISTS declaracao_imposto_renda (
    ano_exercicio    DATE    PRIMARY KEY,
    ano_base         DATE    NOT NULL,
    valor            INT     NOT NULL,
    pagamento        BOOLEAN NOT NULL,
    cpf_contribuinte INT     NOT NULL,
    FOREIGN KEY (
        cpf_contribuinte
    )
    REFERENCES contribuinte (cpf) 
);

INSERT INTO declaracao_imposto_renda (
                                         ano_exercicio,
                                         ano_base,
                                         valor,
                                         pagamento,
                                         cpf_contribuinte
                                     )
                                     VALUES (
                                         '2020-01-10',
                                         2020,
                                         100,
                                         'dinheiro',
                                         10020030040
                                     );

INSERT INTO declaracao_imposto_renda (
                                         ano_exercicio,
                                         ano_base,
                                         valor,
                                         pagamento,
                                         cpf_contribuinte
                                     )
                                     VALUES (
                                         '2021-01-10',
                                         2021,
                                         200,
                                         'cartao',
                                         11122233344
                                     );

INSERT INTO declaracao_imposto_renda (
                                         ano_exercicio,
                                         ano_base,
                                         valor,
                                         pagamento,
                                         cpf_contribuinte
                                     )
                                     VALUES (
                                         '2022-10-01',
                                         2022,
                                         300,
                                         'dinheiro',
                                         44433322211
                                     );

INSERT INTO declaracao_imposto_renda (
                                         ano_exercicio,
                                         ano_base,
                                         valor,
                                         pagamento,
                                         cpf_contribuinte
                                     )
                                     VALUES (
                                         '2023-12-01',
                                         2023,
                                         400,
                                         'dinheiro',
                                         12332122211
                                     );

INSERT INTO declaracao_imposto_renda (
                                         ano_exercicio,
                                         ano_base,
                                         valor,
                                         pagamento,
                                         cpf_contribuinte
                                     )
                                     VALUES (
                                         '2024-05-10',
                                         2024,
                                         500,
                                         'boleto',
                                         22233311144
                                     );


-- Table: malha_fina
CREATE TABLE IF NOT EXISTS malha_fina (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    ano_exercicio DATE    NOT NULL
);

INSERT INTO malha_fina (
                           id,
                           ano_exercicio
                       )
                       VALUES (
                           1,
                           '2025-04-21'
                       );

INSERT INTO malha_fina (
                           id,
                           ano_exercicio
                       )
                       VALUES (
                           2,
                           '2020-10-2'
                       );

INSERT INTO malha_fina (
                           id,
                           ano_exercicio
                       )
                       VALUES (
                           3,
                           '2021-11-2'
                       );

INSERT INTO malha_fina (
                           id,
                           ano_exercicio
                       )
                       VALUES (
                           4,
                           '2022-12-1'
                       );

INSERT INTO malha_fina (
                           id,
                           ano_exercicio
                       )
                       VALUES (
                           5,
                           '2023-01-1'
                       );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
