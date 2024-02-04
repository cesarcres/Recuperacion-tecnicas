import unittest
from main import prefijo_sufijo_comun

class TestPrefijoSufijoComun(unittest.TestCase):

    def test_prefijo_sufijo_comun(self):
        nombres = ["Aldolin", "Alendi", "Allomancy", "Alethi"]
        resultado = prefijo_sufijo_comun(nombres)
        self.assertEqual(resultado, ("Al", ""))
        
    def test_un_nombre(self):
        nombres = ["Gato"]
        resultado = prefijo_sufijo_comun(nombres)
        self.assertEqual(resultado, ("Gato", "Gato"))

    def test_dos_nombres_sin_comun(self):
        nombres = ["Jose", "Antonio"]
        resultado = prefijo_sufijo_comun(nombres)
        self.assertEqual(resultado, ("", ""))    

    def test_dos_nombres_con_prefijo_comun(self):
        nombres = ["Gato", "Gas"]
        resultado = prefijo_sufijo_comun(nombres)
        self.assertEqual(resultado, ("Ga", ""))

    def test_varios_nombres_con_prefijo_sufijo_comun(self):
        nombres = ["Pelota", "Piola", "Puerta"]
        resultado = prefijo_sufijo_comun(nombres)
        self.assertEqual(resultado, ("P", "a"))

if __name__ == '__main__':
    unittest.main()