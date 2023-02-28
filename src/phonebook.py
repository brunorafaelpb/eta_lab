class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        """
        MELHORIA: Padronizar e corrigir os textos de retorno e diminuir a quantidade de "if"
        """
        if ('#' or '@' or '!' or '$' or '%') in name:
            return 'Nome inválido'

        if len(number) < 0:
            return 'Número inválido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Número adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        """
        MELHORIA: Padronizar o texto de retorno e diminuir a quantidade de "if"
        """
        if ('#' or '@' or '!' or '$' or '%') in name:
            return 'Nome inválido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook

        return self.entries.keys()
        """
        """
        CORREÇÃO: Os nomes agora são retornados em uma lista
        """
        lista_nomes = []
        for name in self.entries.keys():
            lista_nomes.append(name)
        return lista_nomes

    def get_numbers(self):
        """

        :return: return all numbers in phonebook

        return self.entries.values()
        """

        """
        CORREÇÃO: Os números agora são retornados em uma lista
        """
        lista = []
        for number in self.entries.values():
            lista.append(number)
        return lista


    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        """
        CORREÇÃO: O if não pode ser "not in", ele deve ser apenas "in"
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        return self.entries

        """
        """
        CORREÇÃO: O método agora retorna apenas os números em ordem crescente.
        """
        lista = self.get_numbers()
        lista.sort()
        return lista

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order

        return self.entries
        """

        """
        CORREÇÃO: O método agora retorna apenas os números em ordem decrescente.
        """
        lista = self.get_numbers()
        lista.sort(reverse=True)
        return lista

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
