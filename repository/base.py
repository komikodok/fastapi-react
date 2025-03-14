from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def index(self, *args, **kwargs): ...

    @abstractmethod
    def show(self, *args, **kwargs): ...

    @abstractmethod
    def store(self, *args, **kwargs): ...
    
    @abstractmethod
    def update(self, *args, **kwargs): ...
    
    @abstractmethod
    def delete(self, *args, **kwargs): ...