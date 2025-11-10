class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

class Market:
    def __init__(self, num_counters: int = 0):
        self.num_counters = num_counters
        # counters: list of Person or None
        self.counters = [None for _ in range(num_counters)]
        # waiting queue: list of Person
        self.waiting = []
        # keep legacy fields if needed later
        self.customers = {}
        self.total_revenue = 0.0

    def __str__(self) -> str:
        # Represent counters: '-----' if None, otherwise person's name
        caixas = [ (c.name if c is not None else '-----') for c in self.counters ]
        espera = [ p.name for p in self.waiting ]
        return f"Caixas: [{', '.join(caixas)}]\nEspera: [{', '.join(espera)}]"


def main():
    import sys
    market = None
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # echo command with $
        print(f"${line}")
        parts = line.split()
        cmd = parts[0]
        if cmd == 'end':
            break
        if cmd == 'init':
            # minimal: create market with given number of counters
            if len(parts) >= 2 and parts[1].isdigit():
                n = int(parts[1])
                market = Market(n)
            else:
                print('fail: argumento invalido')
        elif cmd == 'show':
            if market is None:
                print('fail: mercado nao inicializado')
            else:
                print(market)
        elif cmd == 'arrive':
            if market is None:
                print('fail: mercado nao inicializado')
            else:
                if len(parts) < 2:
                    print('fail: nome ausente')
                else:
                    name = parts[1]
                    person = Person(name)
                    market.waiting.append(person)
        else:
            # ignore other commands for now (not needed for first test)
            continue


if __name__ == '__main__':
    main()
   