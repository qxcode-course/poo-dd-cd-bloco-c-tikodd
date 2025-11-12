from __future__ import annotations

from dataclasses import dataclass
from typing import List, optional

Class CalibreIncomparativeError(ValueError):
    pass
Class BicoOcupadoError(RuntimeError):
    pass

Class SemGrafiteNoBicoError(RunTimeError)

HARDNESS_COMSUMPTION = {
    "HB": 1,
    "2B": 2,
    "4B": 4,
    "6B": 6,
}

Class Grafite:
    def __init__(self, clibre: float, dureza: str, tamanho: float):
        calibre: float
        dureaza: str
        tamanho_mm: int

        def consumir(self, mm: int) -> int:
            consumido = min (self.tamanho_mm, mm)
            self.tamanho_mm -= consumido
            return consumido
        
        def _str_(self) -> str:
            return f"Grafite(calibre={self.calibre}, dureza={self.dureza}, tamanho_mm={self.tamanho_mm})"
        

Class Lapiseira:
    def __init__(self, calibre: float) -> None:
    self.bico: Optional[Grafite] = None
self.tambor: List[Grafite] = []


def inserir_grafite(self, calibre: float, dureza: str, tamanho_mm: int) -> None:
"""Insere um grafite no final do tambor.
Levanta CalibreIncompativelError se o calibre não for compatível.
"""
if abs(float(calibre) - self.calibre) > 1e-6:
raise CalibreIncompativelError(
f"Calibre do grafite ({calibre}) incompatível com lapiseira ({self.calibre})."
)
if dureza not in HARDNESS_CONSUMPTION:
raise ValueError(f"Dureza desconhecida: {dureza}. Opções: {list(HARDNESS_CONSUMPTION.keys())}")
if tamanho_mm <= 0:
raise ValueError("Tamanho do grafite deve ser positivo em mm.")
g = Grafite(float(calibre), dureza, int(tamanho_mm))
self.tambor.append(g)

def puxar_grafite(self) -> None:
    if self.bico is not None:
raise BicoOcupadoError("Já existe um grafite no bico — remova-o antes de puxar outro.")
if not self.tambor:
    raise IndexError("Tambor vazio: não há grafite para puxar.")
self.bico = self.tambor.pop()

def remover_grafite(self) -> Optional[Grafite]:
    return {
"sucesso": True,
"consumido_mm": int(consumido),
"mensagem": "Folha escrita com sucesso.",
"grafite_restante_mm": int(g.tamanho_mm),
}

return {
"sucesso": True,
"consumido_mm": int(consumido),
"mensagem": "Folha escrita com sucesso.",
"grafite_restante_mm": int(g.tamanho_mm),
}


def status(self) -> str:
bico_str = str(self.bico) if self.bico else "(vazio)"
tambor_str = ", ".join(repr(g) for g in self.tambor) if self.tambor else "(vazio)"
return f"Lapiseira {self.calibre}mm | Bico: {bico_str} | Tambor: {tambor_str}"


def __repr__(self) -> str:
return f"Lapiseira(calibre={self.calibre}, bico={self.bico}, tambor={self.tambor})"




if __name__ == "__main__":
# Exemplo de uso
lap = Lapiseira(0.5)
print("Criada:", lap)



# Inserindo grafites corretos e um incorreto
lap.inserir_grafite(0.5, "HB", 60)
lap.inserir_grafite(0.5, "2B", 50)
lap.inserir_grafite(0.5, "4B", 20)
print("Após inserir 3 grafites:", lap)


# Puxar grafite para o bico
lap.puxar_grafite()
print("Após puxar um grafite (último do tambor):", lap)


# Escrever folhas até terminar ou ficar incompleto
while True:
try:
res = lap.escrever_folha()
print(res)
if not res["sucesso"]:
print("A escrita ficou incompleta ou grafite insuficiente — status:", lap)
break
# se o grafite foi removido, poderemos puxar outro
if lap.bico is None:
print("Bico vazio — puxe outro grafite do tambor se houver.")
break
except SemGrafiteNoBicoError as e:
print("Erro:", e)
break


        

