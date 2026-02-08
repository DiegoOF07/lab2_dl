class AFD:
    def __init__(self):
        self.states = []
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()
