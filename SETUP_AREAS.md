# Configuração das Áreas de Atuação

## Problema Resolvido
As "Áreas de Atuação" não apareciam no formulário de signup porque a tabela `AreaOfExpertise` estava vazia.

## Solução

### 1. Adicionar áreas via Management Command (Recomendado)
```bash
python manage.py populate_areas
```

### 2. Adicionar com opção de limpar
Se você quer remover áreas antigas e adicionar novas:
```bash
python manage.py populate_areas --clear
```

### 3. Script direto (alternativa)
```bash
python setup_areas.py
```

## Áreas Disponíveis
As seguintes áreas de atuação estão configuradas em `medicoes/category_config.py`:

- **Geociências** - Ciências da Terra, geologia, sismologia
- **Metrologia** - Medição, padrões, instrumentação
- **Física** - Física fundamental, gravitação, astrofísica
- **Defesa** - Aplicações de defesa civil, segurança nacional
- **Divulgação Científica** - Educação e comunicação científica

## Primeira Execução do Projeto

Para configurar o projeto completo, execute:

```bash
cd Gravimeasure-main
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou no Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py populate_areas
python manage.py runserver
```

## Verificar se está funcionando

Abra o formulário de signup em http://localhost:8000/signup e verifique se as opções de "Áreas de Atuação" aparecem como checkboxes.
