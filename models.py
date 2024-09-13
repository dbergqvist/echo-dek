from dataclasses import dataclass

@dataclass
class Artist:
    id: str
    name: str

@dataclass
class Album:
    id: str
    title: str