import pytest
from src.phonebook import Phonebook


class TestPhonebook:

    phonebook = Phonebook()
    nome_valido = "Bruno"
    telefone_valido = "999999999"
    nome_valido2 = "Rafael"
    telefone_valido2 = "00000000"

    @pytest.fixture
    def msg_contato_add(self):
        return "Número adicionado"

    @pytest.fixture
    def msg_phonebook_clear(self):
        return "phonebook limpado"

    @pytest.fixture
    def msg_contato_delete(self):
        return "Numero deletado"

    def test_add_contato_valido(self, msg_contato_add):
        resultado = self.phonebook.add(self.nome_valido, self.telefone_valido)
        assert resultado == msg_contato_add
        assert self.phonebook.entries[self.nome_valido] == self.telefone_valido

    def test_lookup_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.lookup(self.nome_valido)
        assert resultado == self.telefone_valido

    def test_get_names_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.get_names()
        assert resultado == ["POLICIA", self.nome_valido]

    def test_get_numbers_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.get_numbers()
        assert resultado == ["190", self.telefone_valido]

    def test_clear_valido(self, msg_phonebook_clear):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.clear()
        assert resultado == msg_phonebook_clear
        assert self.phonebook.entries == {}

    def test_search_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.search(self.nome_valido)
        assert resultado == [{self.nome_valido, self.telefone_valido}]

    def test_get_phonebook_sorted_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        self.phonebook.add(self.nome_valido2, self.telefone_valido2)
        resultado = self.phonebook.get_phonebook_sorted()
        lista_crescente = [self.telefone_valido2, self.telefone_valido]
        assert resultado == lista_crescente

    def test_get_phonebook_reverse_valido(self):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        self.phonebook.add(self.nome_valido2, self.telefone_valido2)
        resultado = self.phonebook.get_phonebook_reverse()
        lista_decrescente = [self.telefone_valido, self.telefone_valido2]
        assert resultado == lista_decrescente

    def test_delete_valido(self, msg_contato_delete):
        self.phonebook.add(self.nome_valido, self.telefone_valido)
        resultado = self.phonebook.delete(self.nome_valido)
        assert resultado == msg_contato_delete
