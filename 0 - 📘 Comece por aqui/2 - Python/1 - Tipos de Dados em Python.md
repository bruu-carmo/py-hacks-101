![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)
# 🔤 Tipos de Dados em Python

Em Python, os **tipos de dados** são categorias que determinam o tipo de valor que uma variável pode armazenar e como esse valor pode ser manipulado. Eles são fundamentais para o funcionamento de qualquer programa.


## 📌 O que é uma variável?

Uma variável é um nome que armazena dados na memória. Você pode imaginar como uma etiqueta colada em uma caixa que contém um valor.

```python
nome = "Oswaldo"
idade = 27
```

## 🔢 Tipos de Dados Primitivos

### 📌 Numéricos
| Tipo     | Descrição                       | Exemplo      |
|----------|----------------------------------|--------------|
| `int`    | Números inteiros                 | `10`, `-5`, `0` |
| `float`  | Números de ponto flutuante       | `3.14`, `-2.71` |
| `complex`| Números complexos                | `1+2j` |

## **1. Tipo Inteiro (int)**

É um tipo usado para um **número** que pode ser escrito **sem um componente decimal**, podendo ser **positivo ou negativo**

No código abaixo, por exemplo, vemos as variáveis, idade e ano, com os valores 20 e 2010 atribuídos a elas; se pedirmos que o programa imprima o tipo das variáveis, teremos como retorno que elas são do tipo inteiro:

- `idade = 20`
- `ano = 2010`
- `print(type(idade))`
- `print(type(ano))`
- `<class ‘int’>`
- `<class ‘int’>`

## **2. Ponto Flutuante ou Decimal (float)**

É um tipo composto por **números decimais**. O **float** é usado para números racionais (que podem ser representados por uma fração), informalmente conhecidos como “números quebrados”.

No código abaixo, por exemplo, vemos as variáveis altura e peso com os valores 1.73 e 78.500 atribuídos a elas.

Se pedirmos que o programa imprima o tipo das variáveis, teremos como retorno que elas são do tipo float:

- `altura = 1.73`
- `peso = 78.500`
- `print(type(peso))`
- `print(type(altura))`
- `<class ‘float’>`
- `<class ‘float’>`

## **3. Complexo (complex)**

Tipo de dado usado para representar **números complexos**, normalmente em **cálculos geométricos e científicos**.

Um tipo complexo contém **duas partes**: a parte **real** e a parte **imaginária**, sendo que a imaginária contém um j no sufixo.

Com a função **complex()** podemos **converter** reais em números complexos. Ela traz dois argumentos, sendo o primeiro deles um número real, correspondente à parte real do número complexo, e o outro, um argumento opcional, que representa a parte imaginária. Por exemplo: z = complex(x,y).

No exemplo abaixo, vemos as variáveis, a e b, com os valores 10+16j e 3+80j atribuídos a elas.

Se pedirmos que o programa imprima o tipo das variáveis, vamos ter como retorno que elas são do tipo complex:

- `a = 10+16j`
- `b = 3+80j`
- `print(type(a))`
- `print(type(b))`
- `<class ‘complex’>`
- `<class ‘complex’>`


### 📌 Sequências
| Tipo     | Descrição                                        | Exemplo                     |
|----------|--------------------------------------------------|-----------------------------|
| `str`    | Texto (string)                                   | `"Olá, mundo!"`             |
| `list`   | Lista (ordem importa, mutável)                   | `[1, 2, "a"]`               |
| `tuple`  | Tupla (ordem importa, imutável)                  | `(1, 2, "a")`               |
| `range`  | Gera uma sequência de números                    | `range(5)`                  |

## **4. String (str)**

É um **conjunto de caracteres** geralmente utilizados para representar palavras, frases ou textos.

Temos como exemplo as variáveis nome e profissão, com os dados Guilherme e Engenheiro de Software atribuídos a elas.

Pedindo para o programa imprimir o tipo dessas variáveis, teremos como retorno que elas são strings:

- `nome = ‘Guilherme’`
- `profissao = ‘Engenheiro de Software’`
- `print(type(profissao ))`
- `print(type(nome))`
- `<class ‘str’>`
- `<class ‘str’>`


## **5. Boolean (bool)**

Tipo de dado **lógico** que pode representar apenas **dois** valores: **falso ou verdadeiro** (False ou True, em Python).

Na lógica computacional, podem ser considerados como **0** ou **1**. Como exemplo, temos as variáveis: sexta_feira e feriado, com os dados True e False atribuídos a elas.

Se pedirmos que o programa imprima o tipo das variáveis, vamos ter como retorno que elas são do tipo boolean:

- `sexta_feira = True`
- `feriado = False`
- `print(type(sexta_feira))`
- `print(type(feriado))`
- `<class ‘bool’>`
- `<class ‘bool’>`

## **6. Listas (list)**

As **listas** agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.

Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos. Já existe um [artigo sobre listas em Python: operações básicas na plataforma Alura](https://www.alura.com.br/artigos/listas-no-python), caso você queira se aprofundar no tema.

No código abaixo, por exemplo, vemos as variáveis alunos e notas, com os dados: ’Mônica’, ’Ana’, ’Bruno’, ’Alice’ e 10, 8.5, 7.8, 8.0 atribuídos a elas.

Pedindo para o programa imprimir o tipo das variáveis, vamos ter como retorno que elas são do tipo **lista**:

- `alunos = [‘Mônica’, ‘Ana’, ‘Bruno’, ‘Alice’]`
- `notas = [10, 8.5, 7.8, 8.0]`
- `print(type(alunos))`
- `<class ‘list’>`
- `<class ‘list’>`

## **7. Tuplas (tuple)**

Assim como as listas, a **tupla** é um tipo que **agrupa um conjunto de elementos**.

Porém, sua forma de definição é diferente, já que utilizamos parênteses e as informações são separadas por vírgula.

Mas a *principal diferença das listas é que as **tuplas são imutáveis**, ou seja, após sua definição, não podem ser modificadas.

Para saber mais a respeito desse tipo, confira o artigo “Conhecendo as tuplas no Python”.

No exemplo abaixo, há as variáveis valores e pontos, com conjuntos de dados atribuídos a elas.

Pedindo para o programa imprimir o tipo das variáveis, temos como retorno que elas são do tipo tuple.

- `valores = (80, 29, 45, 91, 23)`
- `pontos = (10, 29.05, 66.8, 72)`
- `print(type(valores)`
- `print(type(pontos))`
- `<class ‘tuple’>`
- `<class ‘tuple’>`

> Obs: **Se tentarmos modificar uma tupla, receberemos a seguinte mensagem de erro:**

![alt text](image.png)


## **8. Range (range)**

A função **`range()`** gera uma **sequência de números inteiros**, usada frequentemente em repetições com `for`.

É muito útil quando queremos percorrer um intervalo de valores sem precisar criar listas manualmente.

Por exemplo, ao criar uma sequência de 0 a 4 com `range(5)`, o Python entende que deve gerar os números `0, 1, 2, 3, 4`:

- `sequencia = range(5)`

Para verificar o tipo da variável `sequencia`, usamos:

- `print(type(sequencia))`
- `<class 'range'>`

Se quisermos ver os números gerados, basta converter para uma lista:

- `print(list(sequencia))`
- `[0, 1, 2, 3, 4]`


---

### 📌 Mapeamentos
| Tipo     | Descrição                      | Exemplo                          |
|----------|-------------------------------|----------------------------------|
| `dict`   | Dicionário (chave: valor)      | `{"nome": "João", "idade": 30}` |


## **9. Dicionários (dict)**

Os dicionários são normalmente utilizados para agrupar elementos através da estrutura de chave e valor, de forma que a chave é o primeiro elemento, seguido por dois pontos e pelo valor.

Vemos abaixo um exemplo de seu uso, por meio de variáveis de altura e idade, com dados de pessoas como primeiro elemento e os respectivos dados referentes às alturas e idades como valores.

- `altura={‘Sandra’:1.65, ‘Elizabeth’: 1.60, ‘Roberto’: 1.70}`
- `idade = {‘Sandra’:35, ‘Elizabeth’:58, ‘Roberto’:68}”`
- `print(type(altura)`
- `print(type(idade))`
- `<class ‘dict’>`
   - `<class ‘dict’>`


### 📌 Conjuntos
| Tipo        | Descrição                                   | Exemplo                     |
|-------------|----------------------------------------------|-----------------------------|
| `set`       | Conjunto (sem duplicatas, sem ordem fixa)    | `{1, 2, 3}`                 |
| `frozenset` | Conjunto imutável                            | `frozenset({1, 2, 3})`      |

## **10. Conjunto (set)**

Um **set** é uma **coleção de elementos únicos**, ou seja, **não permite duplicatas**. Além disso, os itens **não têm uma ordem fixa**.

Exemplo:

- `numeros = {1, 2, 3, 3, 2}`

Mesmo com números repetidos, o conjunto ignora duplicatas:

- `print(numeros)`
- `{1, 2, 3}`

Verificando o tipo:

- `print(type(numeros))`
- `<class 'set'>`

É útil para operações matemáticas como união, interseção, diferença, etc.:

- `a = {1, 2, 3}`
- `b = {3, 4, 5}`
- `print(a & b)` → interseção
- `{3}`

## **11. Conjunto Imutável (frozenset)**

O **frozenset** é como um set, **mas não pode ser alterado depois de criado**. É imutável e seguro para ser usado como chave de dicionário ou elemento de outro conjunto.

Exemplo:

- `conjunto_fixo = frozenset({1, 2, 3})`

Verificando o tipo:

- `print(type(conjunto_fixo))`
- `<class 'frozenset'>`

Tentativa de alterar:

- `conjunto_fixo.add(4)` → ❌ `AttributeError: 'frozenset' object has no attribute 'add'`


### 📌 Outros
| Tipo        | Descrição                                  | Exemplo                    |
|-------------|---------------------------------------------|----------------------------|
| `bool`      | Booleano (Verdadeiro ou Falso)              | `True`, `False`            |
| `bytes`     | Dados binários imutáveis                    | `b'abc'`                   |
| `bytearray` | Dados binários mutáveis                     | `bytearray(b'abc')`        |
| `NoneType`  | Representa ausência de valor                | `None`                     |

## **13. Booleano (bool)**

O tipo **booleano** representa valores **lógicos**: `True` (verdadeiro) ou `False` (falso). Muito usado em comparações e estruturas de decisão.

Exemplos:

- `maioridade = 18`
- `idade = 20`
- `print(idade >= maioridade)` → `True`

Verificando o tipo:

- `print(type(True))`
- `<class 'bool'>`

## **14. Bytes (bytes)**

O tipo **bytes** representa **dados binários imutáveis**, útil pra manipular arquivos, redes e codificação.

Exemplo:

- `dados = b'abc'`

Verificando o tipo:

- `print(type(dados))`
- `<class 'bytes'>`

Cada letra vira um byte:

- `print(list(dados))`
- `[97, 98, 99]` (valores ASCII)

## **15. Bytearray (bytearray)**

Parecido com `bytes`, mas o **`bytearray` é mutável**. Permite alterar os valores binários depois de criado.

Exemplo:

- `dados = bytearray(b'abc')`
- `dados[0] = 100`

Verificando o tipo:

- `print(type(dados))`
- `<class 'bytearray'>`

Resultado:

- `print(dados)` → `bytearray(b'dbc')`

## **16. NoneType**

O tipo **`NoneType`** só tem um valor: **`None`**. Ele representa **ausência de valor** ou "nada".

Exemplo:

- `resultado = None`

Verificando o tipo:

- `print(type(resultado))`
- `<class 'NoneType'>`

Muito usado como valor padrão de variáveis ou retornos "vazios" de funções.


## 🧬 Tipos de Dados Compostos

- `list`, `tuple`, `dict`, `set`, `frozenset` podem conter outros tipos, inclusive compostos:
```python
exemplo = [1, "texto", [2, 3], {"a": 1}]
```

- `str`, `bytes`, `bytearray` são sequências que também podem armazenar dados compostos (como inteiros para bytes).

---

## 🎯 Importância dos Tipos de Dados

- **Armazenamento**: determinam o que uma variável pode guardar.  
- **Operações**: influenciam como o código se comporta ao somar, comparar, etc.  
- **Manipulação**: definem quais métodos e funções podem ser aplicados.

## ✅ Exemplo prático

```python
nome = "Maria"
idade = 25
altura = 1.65
ativo = True
dados = {"nome": nome, "idade": idade, "altura": altura, "ativo": ativo}
print(dados)
```
 
> ## **Compreender os tipos de dados é essencial para programar com clareza, eficiência e sem bugs.** 🧠🔥

## 📘 Referência Final

Este guia é um compilado dos principais **tipos de dados em Python**, com exemplos simples e explicações diretas para facilitar o aprendizado.

Dominar esses conceitos é fundamental para escrever códigos robustos, seguros e performáticos — seja em projetos simples ou aplicações complexas.

Se quiser explorar mais, vale consultar:
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/library/stdtypes.html)
- [Guia completo de tipos de dados no Python - Alura](https://www.alura.com.br)

---

## 🧠 **Dica de ouro:** 
Sempre que estiver em dúvida sobre o tipo de uma variável, use:

 ```python
 print(type(sua_variavel)) 
  ```
Isso salva debug e ajuda a evitar muitos bugs bobos.

