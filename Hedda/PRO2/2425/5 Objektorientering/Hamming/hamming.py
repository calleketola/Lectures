class Message():

    def __init__(self, data):
        self.message_in = data
        self.message_out = ""

    

    def calculate_redundant_bits(self):
        m = len(self.message_in)
        for r in range(m):
            if 2**r >= m+r+1:
                return r

    def position_redundant_bits(self):
        # Placera extrabitarna på platser
        # motsvarande 2**i
        j = 0
        k = 1
        m = len(self.message_in)
        out = ""

        # Fyll upp datan bakifrån
        for i in range(1, m+r+1):
            if i == 2**j:
                out += '0'
                j += 1
            else:
                out += self.message_in[-1*k]
                k += 1
        return out[::-1] # Vänd rätt datan

