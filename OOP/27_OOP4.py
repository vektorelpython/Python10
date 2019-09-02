class Sınıf():
    #Sınıf niteliği Class Atrribute
    sinif_ozelligi = ""

    """__init__ fonksiyonu 
    örnek üretme sırasında çalışır ve 
    self(self adında olması bir gelenek)
    bütün değişkenlere erişimi sağlayacak 
    taşıyıcıdır, ilk parametre olduğu için 
    bu görevi üstlenmiştir. """
    def __init__(self):
        # örnek niteliği instance attribute
        self.adi = "örnek özellik"
    
    #Örnek metod instance method
    def ornekMetod(self):
        pass

    # Sınıf Metodu class method
    """ @ işareti ile başlaması bu ifadenin bir 
    decorator olduğunu gösterir class metodlarda
    cls parametresi selfte olduğu gibi bir gelenektir
    ve ilk parametre olduğu için 
    bu görevi üstlenmiştir."""
    @classmethod
    def SınıfMetodu(cls):
        pass


