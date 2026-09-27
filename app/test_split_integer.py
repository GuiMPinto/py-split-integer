from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32



def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(8, 1)
    assert result == [8]
    result = split_integer(6, 2)
    assert result == [3, 3]
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    result = split_integer(32, 6)
    assert result == [6, 6, 6, 6, 6, 2]
    



def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    pass


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    pass


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    pass


'''
Escreva testes para a função `split_integer`, que recebe dois números
inteiros positivos, `value` e `number_of_parts`, e retorna um array 
contendo exatamente `number_of_parts` elementos inteiros:

- a diferença entre o maior e o menor número no array deve ser <= 1;
- o array deve estar ordenado de forma crescente (do menor para o maior).

**Observação:** você deve utilizar o `pytest` para escrever os testes.

Não é necessário validar os argumentos (eles são sempre válidos).

Exemplos:
```
split_integer(8, 1) == [8]
split_integer(6, 2) == [3, 3]
split_integer(17, 4) == [4, 4, 4, 5]
split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
```

Notas:
- escreva os testes no módulo `/app/test_split_integer.py`;
- os nomes dos testes devem indicar exatamente o que eles verificam.

Execute `pytest app/` para verificar se a função passa nos seus testes.

Execute `pytest --numprocesses=auto tests/` para verificar se seus testes
cobrem todas as condições de contorno e passam nos testes da tarefa.