"""Signal InfoWells framework runtime.
The runtime coordinates bounded execution and marketplace capabilities; it does
not claim that passing software checks establishes truth or real-world efficacy.
"""
from .cycle import BuildBounds, CycleAssessment, assess_cycle, assess_promotion
from .marketplace import Marketplace, MarketplaceError, load_marketplace
from .capcut_intent import build_capcut_intent, requires_capcut_intent, write_pmcr_task

__all__ = ["BuildBounds", "CycleAssessment", "Marketplace", "MarketplaceError",
           "assess_cycle", "assess_promotion", "load_marketplace", "build_capcut_intent", "requires_capcut_intent", "write_pmcr_task"]
