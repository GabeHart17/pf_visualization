class AnimatedDataLoader:
    def __init__(self, raw_data):  # raw data is string read from file
        raw_field, raw_beacons, raw_states = raw_data.split("*")
        self.field = self.parse_field(raw_field)
        self.beacons = self.parse_beacons(raw_beacons)
        self.states = self.parse_states(raw_states)

    def parse_field(self, s):
        return [float(i) for i in s.split(',')]

    def parse_beacons(self, s):
        return [[float(i) for i in j.split(',')] for j in s.strip().split('\n')]

    def parse_states(self, s):
        separated_states = s.strip().split('~')[:-1]
        parsed_states = []
        for state in separated_states:
            particles = [[float(i) for i in j.split(',')] for j in state.strip().split('\n')[:-1]]
            predicted = particles.pop(-1)
            actual = [float(i) for i in state.strip().rsplit('\n', maxsplit=1)[-1].split(',')]
            parsed_states.append([particles, predicted, actual])
        return parsed_states
