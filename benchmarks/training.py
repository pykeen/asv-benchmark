# -*- coding: utf-8 -*-

"""Benchmarks for training."""

import random
from multiprocessing import cpu_count

from torch.optim import Adam

from pykeen.datasets import get_dataset
from pykeen.losses import MarginRankingLoss
from pykeen.models import DistMult
from pykeen.sampling import BasicNegativeSampler
from pykeen.training import SLCWATrainingLoop
from pykeen.utils import resolve_device


class SLCWATrainingSuite:
    """Benchmark training with the sLCWA."""

    param_names = (
        "dataset",
        "filtered",
        "ratio",
        "workers",
    )
    params = (
        ["countries", "nations", "wn18rr", "wn18"],
        [False, True],
        [10],
        [False, True],
    )

    #: The number of training epochs
    num_epochs: int = 1
    #: The embedding dimension of the DistMult model
    embedding_dim: int = 8

    def setup(self, dataset: str, filtered: bool, ratio: int, workers: bool):
        """Prepare."""
        self.device = resolve_device("cpu")
        self.dataset = get_dataset(dataset=dataset)
        self.loss = MarginRankingLoss()
        self.model = DistMult(
            triples_factory=self.dataset.training,
            preferred_device=self.device,
            embedding_dim=self.embedding_dim,
            loss=self.loss,
            random_seed=random.randint(0, 2 ** 32 - 1),  # so there's no warning
        )
        self.optimizer = Adam(self.model.parameters())
        negative_sampler = BasicNegativeSampler(
            triples_factory=self.dataset.training,
            num_negs_per_pos=ratio,
            filtered=filtered,
        )
        self.trainer = SLCWATrainingLoop(
            model=self.model,
            optimizer=self.optimizer,
            triples_factory=self.dataset.training,
            negative_sampler=negative_sampler,
        )

    def time_train(self, dataset: str, filtered: bool, ratio: int, workers: bool):
        """Time training."""
        self.trainer.train(
            triples_factory=self.dataset.training,
            num_epochs=self.num_epochs,
            use_tqdm=False,
            num_workers=cpu_count() - 1 if workers else 0,
        )
