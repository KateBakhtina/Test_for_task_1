from test_for_task_1 import get_barcode

if __name__ == '__main__':

    assert get_barcode(input()).isdigit(), "Штрих-код не получен"
    print("Штрих-код сохранен в базе данных")