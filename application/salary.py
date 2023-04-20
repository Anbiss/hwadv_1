def calculate_salary(base_rate, hours_worked):
    """
    Функция для вычисления заработной платы работника на основе его базовой ставки и количества часов,
    отработанных в течение месяца.

    :param base_rate: базовая ставка за час работы
    :param hours_worked: количество отработанных часов
    :return: заработная плата за месяц
    """
    salary = base_rate * hours_worked
    return salary

