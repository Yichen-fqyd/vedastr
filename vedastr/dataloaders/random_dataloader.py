from torch.utils.data import ConcatDataset

from .registry import DATALOADERS
from .base import BaseDataloader


@DATALOADERS.register_module
class BatchRandomDataloader(BaseDataloader):
    def __init__(self, dataset, batch_size, each_batch_ratio, each_usage, shuffle=False, num_workers=4):
        dataset = [ConcatDataset(dataset)]
        super(BatchRandomDataloader, self).__init__(dataset=dataset,
                                                    each_batch_ratio=each_batch_ratio,
                                                    batch_size=batch_size,
                                                    num_workers=num_workers,
                                                    shuffle=shuffle,
                                                    each_usage=each_usage)
