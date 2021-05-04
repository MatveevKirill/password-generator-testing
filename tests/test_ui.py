import re
import pytest

from tests.base_test import BaseTestCase


class PrepareData(BaseTestCase):

    def get_passwords(self, params: dict) -> list:

        # Генерация паролей.
        self.main_page.generate_passwords(params)

        # Получение списка паролей.
        return self.main_page.get_passwords()


class TestGenerationPasswords(PrepareData):

    @pytest.mark.parametrize(
        "params, result_regular",
        [
            ({'usenums': False, 'usecaps': False, 'uselower': False, 'usesymbols': False}, r'^[a-zA-Z0-9]{6}$'),
            ({'usenums': True, 'usecaps': True, 'uselower': True, 'usesymbols': False, 'len': 8}, r'^[a-zA-Z0-9]{8}$'),
            ({'usenums': False, 'usecaps': False, 'uselower': False, 'usesymbols': True, 'len': 10}, r'^[a-zA-Z0-9%*&^:;№\"\'!()?@#$~{}|\/-]{10}$')
        ]
    )
    def test_generate_passwords_by_default_params(self, params: dict, result_regular: str) -> None:
        passwords = self.get_passwords(params=params)

        for password in passwords:
            assert re.match(result_regular, password) is not None
