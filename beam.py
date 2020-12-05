class beam:
    def __init__(self, E, I, L, type):
        self.E = E
        self.I = I
        self.L = L
        self.type = type

    def __str__(self):
        return f"{self.type} beam with length {self.L}, modulus of elasticity of {self.E} and moment of inertia of {self.I}"

#           w
#      <---------->
#      +----------+ ^
#      |          | | t
#      |  +----+  | V
#      |  |    |  |
#      |  |    |  |
#      |  +----+  |
#      |          |
#      +----------+

def new_shs(E, w, t, L):
    # (bd^3 - hk^3)/12 where b is horizontal width, d is vertical width, h is horizontal inner space, k is vertical inner space
    I = ((2 * w)**3 - ((w * 2)- t)**3) / 12 

    return beam(E, I, L, 'SHS')

#           wh
#      <---------->
#    ^ +----------+ ^
#    | |          | | tv
#    | |  +----+  | V
#    | |  |    |  |
# wv | |  |    |  |
#    | |  |    |  |
#    | |  +----+  |
#    | |          |
#    v +----------+
#      <-->
#       th

def new_rhs(E, wh, wv, th, tv, L): 
    ih = wh - 2 * th
    iv = wv - 2 * tv
    I = ((wh * wv)**3 - (ih * iv)**3) / 12

    return beam(E, I, L, 'RHS')

