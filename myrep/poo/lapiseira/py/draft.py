
from typing import List, Optional


class Lapiseira:
    def __init__(self, calibre: float) -> None:
        self.calibre = float(calibre)
        # bico represented as list for compatibility with expected string 'bico: []' or '[grafite]'
        self.bico: List[str] = []
        # tambor as list of grafite representations
        self.tambor: List[str] = []

    def __str__(self) -> str:
        # For the first test we only need empty representations
        bico_str = '[]' if not self.bico else f"[{self.bico[0]}]"
        tambor_str = '<>' if not self.tambor else '<' + ''.join(self.tambor) + '>'
        # calibre should be printed as in input (e.g., 0.5)
        calibre_str = (str(self.calibre)).rstrip('0').rstrip('.') if '.' in str(self.calibre) else str(self.calibre)
        return f"calibre: {calibre_str}, bico: {bico_str}, tambor: {tambor_str}"


def main() -> None:
    import sys

    lap: Optional[Lapiseira] = None
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # echo command
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
                # ignore malformed
                continue
        elif cmd == 'show':
            if lap is None:
                print('lapiseira nao inicializada')
            else:
                print(lap)


if __name__ == '__main__':
    main()
