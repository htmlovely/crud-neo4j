from py2neo import Graph, Node, Relationship

# Conectando ao banco de dados Neo4j
graph = Graph("bolt://localhost:7687", auth=("vitoria", "vitoria10"))

# Função para criar um nó no banco de dados
def create_node(label, properties):
    node = Node(label, **properties)
    graph.create(node)
    return node

# Função para criar um relacionamento entre dois nós
def create_relationship(node1, relationship_type, node2):
    relationship = Relationship(node1, relationship_type, node2)
    graph.create(relationship)
    return relationship

# Função para atualizar as propriedades de um nó
def update_node(node, properties):
    for key, value in properties.items():
        node[key] = value
    graph.push(node)

# Função para excluir um nó do banco de dados
def delete_node(node):
    graph.delete(node)

# Exemplo de uso
# Criando um nó
person = create_node("Person", {"name": "John Doe", "age": 30})

# Atualizando as propriedades de um nó
update_node(person, {"age": 31})

# Criando outro nó
company = create_node("Company", {"name": "Acme Corporation"})

# Criando um relacionamento entre os nós
create_relationship(person, "WORKS_FOR", company)

# Excluindo um nó
delete_node(person)
