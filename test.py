from main import Produto
import unittest


class TestUnitProduto(unittest.TestCase):

    # Verifiando se os valores estão iguais
    def teste_if_name_field_is_equals_to_value(self):

        prod1 = Produto(codigo=1,
                        nome='mouse',
                        categoria='perifericos',
                        preco=199.99)

        self.assertEqual(prod1.nome, 'mouse')

    def teste_if_codigo_field_is_equals_to_value(self):
        prod1 = Produto(codigo=1,
                        nome='mouse',
                        categoria='perifericos',
                        preco=199.99)
        prod1.codigo = 1
        self.assertEqual(prod1.codigo,1)


    def teste_i_categoria_field_is_equals_to_value(self):

        prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99) 
        
        self.assertEqual(prod1.categoria,'perifericos')


    def teste_if_preco_field_is_equals_to_value(self):

        prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99) 
        
        self.assertEqual(prod1.preco,199.99)

    #Verificando se o valor é FALSO
    def teste_if_disponivel_field_is_false(self):

        prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99) 
        
        self.assertFalse(prod1.disponivel)


    #Testando tipo  de variaveis
    def test_if_codigo_is_int_type(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            self.assertIsInstance(prod1.codigo, int)


    def test_if_nome_is_str_type(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            self.assertIsInstance(prod1.nome, str)

    def test_if_categoria_is_str_type(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            self.assertIsInstance(prod1.categoria, str)


    def test_if_preco_is_float_type(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            self.assertIsInstance(prod1.preco, float)


    #Testando se é um produto
    def test_if_prod1_is_instance_of_produto_class(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            self.assertIsInstance(prod1, Produto)

    #Testando ativação e desativação do produto
    def test_if_disponivel_is_false_when__deactivate_product(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            prod1.desativar()
            self.assertFalse(prod1.disponivel)


    def test_if_disponivel_is_true_when__deactivate_product(self):
            prod1 = Produto(codigo=1,
                        nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
            prod1.ativar()
            self.assertTrue(prod1.disponivel)
    

    #testeando erro

    # def test_if_is_invalid_codigo(self):
    #         with self.assertRaises(ValueError):
    #             prod1 = Produto(codigo=-1,
    #                     nome= 'mouse',
    #                     categoria='perifericos',
    #                     preco= 199.99)
            

    def test_if_codigo_is_different(self):
        prod1 = Produto(nome= 'mouse',
                        categoria='perifericos',
                        preco= 199.99)
        prod2 = Produto(	nome= 'teclado',
                        categoria='perifericos',
                        preco= 250.55)
        self.assertNotEqual(prod1.codigo,prod2.codigo)
























