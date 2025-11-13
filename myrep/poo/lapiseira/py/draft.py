
from typing import List, Optional


class Lapiseira:
    def __init__(self, calibre: float) -> None:
        self.calibre = float(calibre)
        # bico holds either None or a dict {'calibre':float,'dureza':str,'tamanho':int}
        self.bico: Optional[dict] = None
        # tambor is a FIFO list of grafite dicts
        self.tambor: List[dict] = []

    def __str__(self) -> str:
        if not self.bico:
            bico_str = '[]'
        else:
            bico_str = f"[{self.bico['calibre']}:{self.bico['dureza']}:{self.bico['tamanho']}]"
        if not self.tambor:
            tambor_str = '<>'
        else:
            tambor_str = '<' + ''.join(f"[{g['calibre']}:{g['dureza']}:{g['tamanho']}]" for g in self.tambor) + '>'
        s = str(self.calibre)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return f"calibre: {s}, bico: {bico_str}, tambor: {tambor_str}"


def main() -> None:
    import sys

    lap: Optional[Lapiseira] = None
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        print(f"${line}")
        parts = line.split()
        cmd = parts[0]
        if cmd == 'end':
            break
        if cmd == 'init':
            if len(parts) >= 2:
                try:
                    calibre = float(parts[1])
                except ValueError:
                    calibre = 0.0
                lap = Lapiseira(calibre)
            else:
                continue
        elif cmd == 'show':
            if lap is None:
                print('lapiseira nao inicializada')
            else:
                print(lap)
        elif cmd == 'pull':
            if lap is None:
                continue
            # if there's already graphite in bico -> fail
            if lap.bico is not None:
                print('fail: ja existe grafite no bico')
            else:
                if not lap.tambor:
                    # nothing to pull
                    continue
                # pull from front of tambor
                g = lap.tambor.pop(0)
                lap.bico = g
        elif cmd == 'remove':
            if lap is None:
                continue
            # remove graphite from bico if present
            lap.bico = None
        elif cmd == 'write':
            if lap is None:
                continue
            if not lap.bico:
                print('fail: nao existe grafite no bico')
            else:
                HARDNESS = {
                    'HB': 1,
                    '2B': 2,
                    '4B': 4,
                    '6B': 6,
                }
                g = lap.bico
                dureza = g['dureza']
                consumo = HARDNESS.get(dureza, 0)
                tamanho = g['tamanho']
                # if already <=10 -> tamanho insuficiente
                if tamanho <= 10:
                    print('fail: tamanho insuficiente')
                    continue
                # usable mm excluding last 10mm
                utilizavel = tamanho - 10
                if utilizavel >= consumo:
                    # full sheet written
                    g['tamanho'] = tamanho - consumo
                    # if becomes <=10 it's still kept in bico (as tests expect)
                else:
                    # consume what is possible and report incomplete
                    # reduce to 10 and report incomplete
                    g['tamanho'] = 10
                    print('fail: folha incompleta')
        elif cmd == 'insert':
            # insert <calibre> <dureza> <tamanho>
            if lap is None:
                # ignore if not initialized
                continue
            if len(parts) < 4:
                # malformed
                continue
            try:
                gcal = float(parts[1])
            except ValueError:
                # malformed calibre
                print('fail: calibre incompatível')
                continue
            dureza = parts[2]
            try:
                tamanho = int(parts[3])
            except ValueError:
                # malformed tamanho
                continue
            # precision compare
            if abs(gcal - lap.calibre) > 1e-6:
                print('fail: calibre incompatível')
                continue
            # accept and append representation to tambor (as last element)
            s = str(gcal)
            if '.' in s:
                s = s.rstrip('0').rstrip('.')
            # store as dict
            lap.tambor.append({'calibre': s, 'dureza': dureza, 'tamanho': tamanho})
        # end command loop


if __name__ == '__main__':
    main()
# ...existing code...