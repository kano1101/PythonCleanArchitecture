import injector
from interactor import OutputData
from i_interactor import IPresenter
from i_presenter import IViewer


class ViewModel:
    def __init__(self, output_data: OutputData):
        pass


class Presenter(IPresenter[OutputData]):
    @injector.inject
    def __init__(self, viewer: IViewer):
        self.viewer = viewer

    def output(self, output_data: OutputData):
        view_model = ViewModel(output_data)
        self.viewer.view(view_model)
