from dataclasses import dataclass


@dataclass  # dataset 에 붙이는 어노테이션
class Dataset(object):

    context: str
    fname: str
    housing: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def housing(self) -> object: return self._housing

    @housing.setter
    def housing(self, housing): self._housing = housing

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
