"""Benchmarks for interaction functions."""
import torch
from pykeen.nn.modules import DistMultInteraction


class DistMultSuite:
    """Suite for DistMult interaction."""

    # cf. https://asv.readthedocs.io/en/stable/writing_benchmarks.html#parametrized-benchmarks
    param_names = (
        "batch_size",
        "dim",
        "num_entities",
        "num_relations",
    )
    params = (
        (64,),
        (64,),
        (15_000,),
        (237,),
    )

    def setup(self, batch_size, dim, num_entities, num_relations):
        """Prepare."""
        self.instance = DistMultInteraction()
        self.h = torch.rand(batch_size, dim)
        self.r = torch.rand(batch_size, dim)
        self.t = torch.rand(batch_size, dim)
        self.all = torch.rand(num_entities, dim)

    def time_score_hrt(self, batch_size, dim, num_entities, num_relations):
        """Time score_hrt method."""
        self.instance.score_hrt(h=self.h, r=self.r, t=self.t)

    def time_score_h(self, batch_size, dim, num_entities, num_relations):
        """Time score_h method."""
        self.instance.score_h(all_entities=self.all, r=self.r, t=self.t)

    def time_score_t(self, batch_size, dim, num_entities, num_relations):
        """Time score_t method."""
        self.instance.score_t(h=self.h, r=self.r, all_entities=self.all)
