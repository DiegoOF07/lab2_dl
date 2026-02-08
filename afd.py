class AFD:
    def __init__(self):
        self.states = []
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def simulate(self, input_string, verbose=False):
        current = self.start_state

        if verbose:
            print(f"Inicio en estado {current}")

        for char in input_string:
            if (current, char) not in self.transitions:
                if verbose:
                    print(f"No hay transición con '{char}', rechazo")
                return False

            next_state = self.transitions[(current, char)]
            if verbose:
                print(f"{current} --{char}--> {next_state}")
            current = next_state

        if current in self.accept_states:
            if verbose:
                print(f"Estado final alcanzado: {current}")
            return True
        else:
            if verbose:
                print(f"Estado no final: {current}")
            return False
