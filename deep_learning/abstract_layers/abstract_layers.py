from abc import ABC, abstractmethod

class abstract_layers(ABC) :
    
    def __call__(self, inputs) :
        raise NotImplementedError("methode non implémenté")
    
    @abstractmethod
    def get_params(self) :
        raise NotImplementedError(f"Vous devez implémenter la méthode get_params pour la classe : {self.__name__}")
   