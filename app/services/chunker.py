from typing import List


class Chunker():
    @staticmethod
    def chunk_fixed_size(text: str, size = 200, overlap = 50):
        words = text.split()
        chunks: List[str] = []
        
        step = size - overlap
        for i in range(0, len(words), step):
            chunk = " ".join(words[i:i + size])
            chunks.append(chunk)
            
        return chunks
