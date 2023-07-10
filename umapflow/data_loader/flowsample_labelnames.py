class GateCollection:

    GATE_BLAST34 = "blast34"
    GATE_BLAST = "blast"
    GATE_BLASTEN = "blasten"
    GATE_BLASTOTHER = "blastother"
    GATE_ADENOMINATOR = "adenominator"
    GATE_INTACT = "intact"
    GATE_CD7pos = "cd7+"
    GATE_BERMUDE = "bermude"
    GATE_BERMUDEA = "bermudea"
    GATE_CD34TOTAL = "cd34total"
    GATE_CD34ALLPOS = "cd34allpos"
    GATE_CD34REAL = "cd34real"
    GATE_PROMY = "promy"
    GATE_GRANULOCYTES = "granulocytes"
    GATE_MONOCYTES = "monocytes"
    GATE_PROERY = "proery"
    GATE_CD34NORMAL = "cd34normal"
    PHONETYPE_GATES = [GATE_PROMY, GATE_GRANULOCYTES, GATE_MONOCYTES, GATE_PROERY, GATE_CD34NORMAL]
    PHONETYPE_GATES_WITH_BLASTS = PHONETYPE_GATES + [GATE_BLASTOTHER, GATE_BLAST34]
    BERMUDEA_GATES_WITH_BLASTS = [GATE_PROMY, GATE_GRANULOCYTES, GATE_MONOCYTES, GATE_PROERY, GATE_BLASTOTHER]
    CD34_GATES = [GATE_CD34NORMAL, GATE_BLAST34]


class MarkerCollection:
    ALL_VIE = ["CD10", "CD19", "CD20", "CD34", "CD38", "CD45", "FSC-A", "FSC-W", "SSC-A", "SY41", "APC-CY7-A"]
    AML_LAIP = ['FSC-A', 'SSC-A', 'CD15', 'CD34', 'CD117', 'CD33', 'CD14', 'CD11B', 'HLA-DR', 'CD45']
    AML_CFU = ['FSC-A', 'SSC-A', 'CD38', 'CD99', 'CD371','CD34', 'CD117', 'CD33', 'CD123', 'CD45RA', 'HLA-DR', 'CD45']
    AML_COMMON = ["FSC-A", "SSC-A", "CD34", "CD117", "CD33", "CD45", "HLA-DR"]
