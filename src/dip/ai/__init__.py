"""Local-first artificial intelligence and machine-learning services."""

from .agents import AgentRuntime
from .documents import DocumentProcessor
from .expert import ExpertSystem
from .generative import Assistant
from .ml import ModelPlatform
from .neural import NeuralNetwork
from .nlp import NLP
from .recommendation import RecommendationEngine
from .vector_store import VectorStore
from .vision import Vision

__all__ = [
    "AgentRuntime",
    "Assistant",
    "DocumentProcessor",
    "ExpertSystem",
    "ModelPlatform",
    "NeuralNetwork",
    "NLP",
    "RecommendationEngine",
    "VectorStore",
    "Vision",
]
