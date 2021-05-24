"""Benchmarks for interaction functions."""
import torch
from pykeen.nn.modules import DistMultInteraction


class DistMultSuite:
    """Suite for DistMult interaction."""

    batch_size: int = 64
    dim: int = 64

    def setup(self):
        """Prepare."""
        self.instance = DistMultInteraction()
        self.h = torch.rand(self.batch_size, self.dim)
        self.r = torch.rand(self.batch_size, self.dim)
        self.t = torch.rand(self.batch_size, self.dim)

    def time_score_hrt(self):
        """Time score_hrt method."""
        self.instance.score_hrt(h=self.h, r=self.r, t=self.t)
