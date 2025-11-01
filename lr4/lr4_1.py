class Vuzol:
    def __init__(self, prizvische, telephon):
        self.prizvische = prizvische
        self.telephon = telephon
        self.left = None
        self.right = None

class BinarneDerevoPoshuku:
    def __init__(self):
        self.korin = None

    def insert(self, prizvische, telephon):
        self.korin = self._insert(self.korin, prizvische, telephon)

    def _insert(self, vuzol, prizvische, telephon):
        if vuzol is None:
            return Vuzol(prizvische, telephon)
        
        if prizvische < vuzol.prizvische:
            vuzol.left = self._insert(vuzol.left, prizvische, telephon)
        elif prizvische > vuzol.prizvische:
            vuzol.right = self._insert(vuzol.right, prizvische, telephon)
        else:
            vuzol.telephon = telephon
        return vuzol

    def search(self, prizvische):
        return self._search(self.korin, prizvische)

    def _search(self, vuzol, prizvische):
        if vuzol is None:
            return "Абонента не знайдено."
        
        if prizvische == vuzol.prizvische:
            return vuzol.telephon
        elif prizvische < vuzol.prizvische:
            return self._search(vuzol.left, prizvische)
        else:
            return self._search(vuzol.right, prizvische)

    def delete(self, prizvische):
        self.korin = self._delete(self.korin, prizvische)

    def _delete(self, vuzol, prizvische):
        if vuzol is None:
            return vuzol
        
        if prizvische < vuzol.prizvische:
            vuzol.left = self._delete(vuzol.left, prizvische)
        elif prizvische > vuzol.prizvische:
            vuzol.right = self._delete(vuzol.right, prizvische)
        else:
            if vuzol.left is None:
                return vuzol.right
            elif vuzol.right is None:
                return vuzol.left
            
            temp_vuzol = self._find_min(vuzol.right)
            vuzol.prizvische = temp_vuzol.prizvische
            vuzol.telephon = temp_vuzol.telephon
            vuzol.right = self._delete(vuzol.right, temp_vuzol.prizvische)
            
        return vuzol

    def _find_min(self, vuzol):
        current = vuzol
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        self._in_order_traversal(self.korin)

    def _in_order_traversal(self, vuzol):
        if vuzol:
            self._in_order_traversal(vuzol.left)
            print(f"- {vuzol.prizvische}: {vuzol.telephon}")
            self._in_order_traversal(vuzol.right)

def main():
    dovidnyk = BinarneDerevoPoshuku()

    dovidnyk.insert("Чесной", "050 772 53 44")
    dovidnyk.insert("Білоусов", "067 234 56 78")
    dovidnyk.insert("Аксьонов", "093 133 83 77")
    dovidnyk.insert("Бондар", "093 456 78 90")
    dovidnyk.insert("Пилипчук", "063 567 89 01")
    
    print("Вміст довідника (відсортовано за прізвищем):")
    dovidnyk.display()

    print("\n--- 2. Демонстрація пошуку ---")
    prizvische_to_find = "Петренко"
    result = dovidnyk.search(prizvische_to_find)
    print(f"Пошук за прізвищем '{prizvische_to_find}': {result}")

    prizvische_to_find = "Коваленко"
    result = dovidnyk.search(prizvische_to_find)
    print(f"Пошук за прізвищем '{prizvische_to_find}': {result}")

    print("\n--- 3. Демонстрація видалення ---")
    prizvische_to_delete = "Чесной"
    print(f"Видалення абонента: {prizvische_to_delete}")
    dovidnyk.delete(prizvische_to_delete)

    print("\nОновлений вміст довідника:")
    dovidnyk.display()

    print(f"\nПовторний пошук видаленого абонента '{prizvische_to_delete}':")
    result = dovidnyk.search(prizvische_to_delete)
    print(result)

if __name__ == "__main__":
    main()