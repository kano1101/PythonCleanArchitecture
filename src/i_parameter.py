from abc import abstractmethod, ABC


class IParameter(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()


class IParameterController(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()


class IParameterInteractor(ABC):
    def __init__(self, parameter: IParameter):
        self.parameter = parameter


class IParameterRepository(ABC):
    def __init__(self, parameter: IParameter):
        self.parameter = parameter
