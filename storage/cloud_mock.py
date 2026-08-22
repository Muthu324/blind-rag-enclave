from typing import Dict, List

class UntrustedCloudDatastore:
    """Simulates an external cloud indexing engine containing no plaintext access properties."""
    def __init__(self):
        self._index_registry: Dict[str, List[float]] = {}

    def upload_blind_vector(self, token_id: str, dimension_coordinates: List[float]):
        """Persists safe tracking points across public tables."""
        self._index_registry[token_id] = dimension_coordinates

    def get_all_records(self) -> Dict[str, List[float]]:
        return self._index_registry
