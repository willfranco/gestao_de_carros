# Car Management System

## Descrição
Este é um projeto fullstack de gestão de carros desenvolvido utilizando Django para o backend e uma interface frontend integrada. O sistema permite o cadastro, edição, remoção e listagem de veículos, além de outras funcionalidades relacionadas à gestão de frota.

## Tecnologias Utilizadas
- **Backend:** Django
- **Banco de Dados:** PostgreSQL (ou SQLite para desenvolvimento)
- **Frontend:** HTML, CSS

## Funcionalidades
- Cadastro de veículos (marca, modelo, ano, placa, status, etc.)
- Atualização e remoção de veículos
- Listagem e busca de carros cadastrados

## Instalação e Execução

### Pré-requisitos
Certifique-se de ter instalado:
- Python 3.9+
- Django 4+
- PostgreSQL (ou SQLite)

### Passos para rodar o projeto
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/gestao_de_carros.git
   cd gestao_de_carros
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente (crie um arquivo `.env` com as credenciais necessárias, se aplicável)
5. Aplique as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```
6. Crie um superusuário (opcional para acesso ao admin):
   ```sh
   python manage.py createsuperuser
   ```
7. Inicie o servidor Django:
   ```sh
   python manage.py runserver
   ```

## Contribuição
Se deseja contribuir com este projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça um push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request



