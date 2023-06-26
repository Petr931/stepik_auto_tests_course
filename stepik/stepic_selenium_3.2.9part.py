

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, \
        f"expected '{str(substring)}', to be substring of '{str(full_string)}'"
