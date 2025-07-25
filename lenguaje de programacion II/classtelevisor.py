from abc import ABC,abstractmethod
class dispositivoselectronicos(ABC):
    @abstractmethod
    def encender(self):
        pass
    @abstractmethod
    def apagar(self):
    
        pass
class televisor ():
    def encender(self):
        print("televisor encendido")

    def apagar(self):
        print("televisor apagado")

tv=televisor()
tv.encender()