# Generated migration to fix CASCADE constraint in SQLite

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicoes', '0009_alter_medicaogravimetrica_usuario'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE medicoes_medicaogravimetrica_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_estacao VARCHAR(200) NOT NULL,
                codigo_estacao VARCHAR(50) NOT NULL,
                latitude DECIMAL NOT NULL,
                longitude DECIMAL NOT NULL,
                altitude DECIMAL,
                incerteza DECIMAL,
                data_medicao DATE NOT NULL,
                operador VARCHAR(100),
                instrumento VARCHAR(100),
                observacoes TEXT,
                data_cadastro DATETIME NOT NULL,
                data_atualizacao DATETIME NOT NULL,
                ativo BOOLEAN NOT NULL,
                anomalia_bouguer DECIMAL,
                densidade_referencia DECIMAL NOT NULL,
                valor_gravidade DECIMAL NOT NULL,
                usuario_id BIGINT,
                croqui VARCHAR(100),
                foto_estacao VARCHAR(100),
                FOREIGN KEY (usuario_id) REFERENCES medicoes_customuser(id) ON DELETE CASCADE
            );
            
            INSERT INTO medicoes_medicaogravimetrica_new
            SELECT id, nome_estacao, codigo_estacao, latitude, longitude, altitude, incerteza,
                   data_medicao, operador, instrumento, observacoes, data_cadastro, data_atualizacao,
                   ativo, anomalia_bouguer, densidade_referencia, valor_gravidade, usuario_id,
                   croqui, foto_estacao
            FROM medicoes_medicaogravimetrica;
            
            DROP TABLE medicoes_medicaogravimetrica;
            
            ALTER TABLE medicoes_medicaogravimetrica_new RENAME TO medicoes_medicaogravimetrica;
            """,
            """
            CREATE TABLE medicoes_medicaogravimetrica_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_estacao VARCHAR(200) NOT NULL,
                codigo_estacao VARCHAR(50) NOT NULL,
                latitude DECIMAL NOT NULL,
                longitude DECIMAL NOT NULL,
                altitude DECIMAL,
                incerteza DECIMAL,
                data_medicao DATE NOT NULL,
                operador VARCHAR(100),
                instrumento VARCHAR(100),
                observacoes TEXT,
                data_cadastro DATETIME NOT NULL,
                data_atualizacao DATETIME NOT NULL,
                ativo BOOLEAN NOT NULL,
                anomalia_bouguer DECIMAL,
                densidade_referencia DECIMAL NOT NULL,
                valor_gravidade DECIMAL NOT NULL,
                usuario_id BIGINT,
                croqui VARCHAR(100),
                foto_estacao VARCHAR(100),
                FOREIGN KEY (usuario_id) REFERENCES medicoes_customuser(id) ON DELETE NO ACTION
            );
            
            INSERT INTO medicoes_medicaogravimetrica_new
            SELECT id, nome_estacao, codigo_estacao, latitude, longitude, altitude, incerteza,
                   data_medicao, operador, instrumento, observacoes, data_cadastro, data_atualizacao,
                   ativo, anomalia_bouguer, densidade_referencia, valor_gravidade, usuario_id,
                   croqui, foto_estacao
            FROM medicoes_medicaogravimetrica;
            
            DROP TABLE medicoes_medicaogravimetrica;
            
            ALTER TABLE medicoes_medicaogravimetrica_new RENAME TO medicoes_medicaogravimetrica;
            """
        ),
    ]
