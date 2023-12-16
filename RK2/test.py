import unittest
from main import *

class Test_Program(unittest.TestCase):

    suppliers = [
    Suppliers(1, "Звезда-Техника"),
    Suppliers(2, "Сибирские Детали"),
    Suppliers(3, "Волжский Агрекат"),
    Suppliers(4, "АгроПром Комбинат"),
    ]

    details = [
        Detail(1, "Винт", 1500, 1),
        Detail(2, "Гайка", 1700, 2),
        Detail(3, "Гайка", 1900, 3),
        Detail(4, "Шайба",2000, 4),
        Detail(5, "Шплинт", 2100, 4),
    ]

    detsup = [
        DetSup(1, 1),
        DetSup(1, 2),
        DetSup(2, 2),
        DetSup(2, 3),
        DetSup(3, 1),
        DetSup(3, 4),
        DetSup(4, 2),
        DetSup(4, 5),
    ]

    def test_a1(self):
        one_to_many = [(p.name, p.price, d.name)
                   for d in suppliers
                   for p in details
                   if p.sup_id == d.id]
        
        self.assertEqual(a1_solution(one_to_many), 
                        [('Шайба', 2000, 'АгроПром Комбинат'), 
                         ('Шплинт', 2100, 'АгроПром Комбинат')])
        
    def test_a2(self):
        one_to_many = [(p.name, p.price, d.name)
                   for d in suppliers
                   for p in details
                   if p.sup_id == d.id]
        
        self.assertEqual(a2_solution(one_to_many), 
                         [('АгроПром Комбинат', 4100), 
                          ('Волжский Агрекат', 1900), 
                          ('Сибирские Детали', 1700),
                          ('Звезда-Техника', 1500)])
        
    def test_a3(self):
        many_to_many_temp = [(d.name, ed.sup_id, ed.det_id)
                         for d in suppliers 
                         for ed in detsup
                         if d.id == ed.sup_id]
    
        many_to_many = [(e.name, e.price, sup_name)
                    for sup_name, sup_id, det_id in many_to_many_temp
                    for e in details
                    if e.id == det_id]
        
        self.assertEqual(a3_solution(many_to_many),
                         {'АгроПром Комбинат': ['Гайка', 'Шплинт'], 
                          'Валжский Агрекат': ['Винт', 'Шайба'], 
                          'Звезда-Техника': ['Винт', 'Гайка'], 
                          'Сибирские Детали': ['Гайка', 'Гайка']})
        
if __name__ == '__main__':
    unittest.main()