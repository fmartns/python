# Cronograma Intensivo de Django – 10 Dias Úteis

Este cronograma foi elaborado para profissionais com formação em Análise e Desenvolvimento de Sistemas que precisam apenas relembrar os conceitos principais de Python e aprender Django. Cada dia corresponde a **1 hora de conteúdo teórico** seguida de **30 minutos de exercício prático**, totalizando **1 h 30 min** diários.

---

## Visão Geral
- **Carga total:** 15 horas distribuídas em 10 dias úteis.
- **Formato:** exposição teórica (60 min) + exercício guiado (30 min).
- **Objetivo:** ao final, o participante será capaz de construir, publicar e manter uma aplicação completa em Django com API REST.

---

## Dia 1 — Revisão de Python Essencial
### Conteúdo Teórico (1 h)
- Tipos primitivos, listas e dicionários
- Funções, parâmetros e escopo
- Estruturas de controle (`if`, `for`, `while`)
- Módulos e importações

### Exercício Prático (30 min)
Implementar funções que recebam listas e dicionários, realizem transformações (ordenar, filtrar, mapear) e retornem resultados consolidados.

---

## Dia 2 — Introdução ao Django e POO
### Conteúdo Teórico (1 h)
- Instalação do Django, criação de projeto e aplicativo
- Estrutura de pastas e arquivos
- Primeiras views com `HttpResponse`
- Revisão de POO aplicada a `models`

### Exercício Prático (30 min)
Criar uma view que renderize um template e exiba dados fornecidos pela camada de modelo.

---

## Dia 3 — Templates e Rotas Dinâmicas
### Conteúdo Teórico (1 h)
- Variáveis, laços e condicionais em templates
- Herança de templates (`base.html`)
- Rotas com parâmetros dinâmicos

### Exercício Prático (30 min)
Desenvolver uma página que liste livros a partir de dados dinâmicos, usando parâmetros na URL para filtrar resultados.

---

## Dia 4 — Models, Migrations e Admin
### Conteúdo Teórico (1 h)
- Definição de `models`
- Processo de `migrations` e criação do banco
- Registro e configuração de modelos no Django Admin

### Exercício Prático (30 min)
Criar os modelos `Livro` e `Autor`, aplicar migrações e inserir registros via Django Admin.

---

## Dia 5 — Views com QuerySets e Formulários
### Conteúdo Teórico (1 h)
- Uso de QuerySets em views
- `ModelForm` e validação de dados
- Criação de objetos via requisição `POST`

### Exercício Prático (30 min)
Adicionar livros através de formulário e exibir a listagem atualizada na mesma página.

---

## Dia 6 — Atualização e Exclusão (CRUD Completo)
### Conteúdo Teórico (1 h)
- Views de edição e exclusão
- Utilização de `get_object_or_404` e `redirect`

### Exercício Prático (30 min)
Completar o CRUD manualmente adicionando páginas de update e delete para livros.

---

## Dia 7 — Views Baseadas em Classe (CBVs)
### Conteúdo Teórico (1 h)
- `ListView`, `CreateView`, `UpdateView`, `DeleteView`
- Mapeamento de URLs para CBVs

### Exercício Prático (30 min)
Refatorar as views do CRUD para CBVs mantendo o comportamento existente.

---

## Dia 8 — Autenticação e Permissões
### Conteúdo Teórico (1 h)
- Fluxo de login e logout com o sistema de autenticação padrão
- Decorador `@login_required` e mixin `LoginRequiredMixin`
- Controle de acesso em views e templates

### Exercício Prático (30 min)
Proteger rotas do CRUD exigindo autenticação para acesso.

---

## Dia 9 — Django REST Framework
### Conteúdo Teórico (1 h)
- Instalação e configuração inicial
- Criação de `Serializers`
- Implementação de `APIView` ou `ViewSet`

### Exercício Prático (30 min)
Implementar endpoints `GET` e `POST` para o recurso livros.

---

## Dia 10 — Deploy e Git
### Conteúdo Teórico (1 h)
- Uso básico do Git (`init`, `add`, `commit`, `push`)
- Deploy no PythonAnywhere (ou serviço similar)
- Configurações de produção: `DEBUG`, `ALLOWED_HOSTS`, arquivos estáticos

### Exercício Prático (30 min)
Publicar o projeto completo em ambiente de produção e disponibilizar a URL.

---

## Próximos Passos Sugeridos
1. Cobertura de testes automatizados com `pytest` e integração contínua (CI).
2. Contêinerização com Docker e orquestração básica com Docker Compose.
3. Autenticação via JWT utilizando `djangorestframework-simplejwt`.
4. Tarefas assíncronas com Celery e Redis para processamento em segundo plano.
5. Monitoramento e logging avançado em produção.
