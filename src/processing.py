def filter_by_state(list_of_operations: list[dict[str]], state_value: str = "EXECUTED") -> list[dict[str]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список"""
    modified_list = []
    for i in list_of_operations:
        if i["state"] == state_value:
            modified_list.append(i)
    return modified_list


def sort_by_date(data_list: list[dict[str]], descending: bool = True) -> list:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате"""
    list_sorted = sorted(data_list, key=lambda dict_oper: dict_oper.get("date", 0), reverse=descending)
    return list_sorted
