import pytest

test_data_set = [[1], {1, 2, 3}, {1: "Математика", 2: "Информатика"}]
test_data_tuple = [[1, "str", -1, 1.5], [[1, 2, 3], 0, 5], [{1: 2, 2: 5, 3: 7}, "str", 10]]


@pytest.mark.set
def test_set_can_only_store_one_instance_of_an_element():
    data_for_set = [1, 1, -100, 100, 0, 0]
    test_set = set(data_for_set)
    assert len(data_for_set) != len(test_set), "Множество иммеет повторяющиеся элементы"


@pytest.mark.set
@pytest.mark.parametrize("data_for_set", test_data_set)
def test_set_can_only_contain_elements_of_immutable_types(data_for_set):
    check = False
    try:
        test_set = {0, 1, 2, data_for_set}
    except TypeError:
        check = True
    assert check, f"В множество были добавлены изменяемые элементы: {type(data_for_set)}"


@pytest.mark.set
def test_tuple_can_contain_objects_of_different_types():
    data_for_set = [1, "str", 1.5, True]
    check = False
    try:
        test_set = set(data_for_set)
        check = True
    except Exception as e:
        print(f"Ошибка: {e}")
    assert check, "Невозможно добавить в кортеж данные разных типов"


@pytest.mark.tuple
def test_tuple_not_changeable():
    a = (1, 2, 3, 4, 5, 6, 7)
    check = False
    try:
        a.append(5)
    except AttributeError as e:
        check = True
    assert check, "Удалось добавить элемент в кортеж"


@pytest.mark.tuple
@pytest.mark.parametrize("data_for_tuple", test_data_tuple)
def test_tuple_can_contain_objects_of_different_types(data_for_tuple):
    check = False
    try:
        test_tuple = tuple(data_for_tuple)
        check = True
    except Exception as e:
        print(f"Ошибка: {e}")
    assert check, "Невозможно добавить в кортеж данные разных типов"


@pytest.mark.tuple
def test_tuple_can_be_measured():
    data_for_tuple = [1, 2, 3, 4, 5, 6, 7]
    test_tuple = tuple(data_for_tuple)
    assert len(test_tuple) == 7, "Размер кортежа был измерен неправильно"
