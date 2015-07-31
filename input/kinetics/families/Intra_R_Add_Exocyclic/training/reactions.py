#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""






entry(
    index = 1,
    label = "[CH2]CC!C0r1 <=> [CH2]C1CC10p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (632000000.0, 's^-1', '*|/', 2.51189),
        n = 0.97,
        Ea = (8.9, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 2,
    label = "C!CC[CH]C1r1 <=> [CH2]C1CC1C1p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (556000000.0, 's^-1', '*|/', 2.51189),
        n = 1,
        Ea = (9.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 3,
    label = "C!CC[C](C)C2r1 <=> [CH2]C1CC1(C)C2p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (247000000.0, 's^-1', '*|/', 2.51189),
        n = 1.11,
        Ea = (9.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 4,
    label = "[CH2]CC!CC3r1 <=> C[CH]C1CC13p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1680000000.0, 's^-1', '*|/', 2.51189),
        n = 0.84,
        Ea = (9.2, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 5,
    label = "[CH2]C(C)C!C4r1 <=> [CH2]C1CC1C4p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1080000000.0, 's^-1', '*|/', 2.51189),
        n = 0.9,
        Ea = (7.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 6,
    label = "[CH2]CC(!C)C5r1 <=> [CH2]C1(C)CC15p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (852000000.0, 's^-1', '*|/', 2.51189),
        n = 0.89,
        Ea = (10.4, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 7,
    label = "[CH2]C(C)(C)C!C6r1 <=> [CH2]C1CC1(C)C6p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1850000000.0, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (6.2, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 8,
    label = "[CH2]CC!C(C)C7r1 <=> C[C](C)C1CC17p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2900000000.0, 's^-1', '*|/', 2.51189),
        n = 0.79,
        Ea = (8.5, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 9,
    label = "[CH2]CCC!C8r1 <=> [CH2]C1CCC18p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2070000.0, 's^-1', '*|/', 2.51189),
        n = 1.46,
        Ea = (14.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 10,
    label = "C!CCC[CH]C9r1 <=> [CH2]C1CCC1C9p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4730000.0, 's^-1', '*|/', 2.51189),
        n = 1.31,
        Ea = (13.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 11,
    label = "C!CCC[C](C)C10r1 <=> [CH2]C1CCC1(C)C10p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (102000.0, 's^-1', '*|/', 2.51189),
        n = 1.8,
        Ea = (11.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 12,
    label = "[CH2]CCC!CC11r1 <=> C[CH]C1CCC111p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8650000.0, 's^-1', '*|/', 2.51189),
        n = 1.3,
        Ea = (13.8, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 13,
    label = "[CH2]C(C)CC!C12r1 <=> [CH2]C1CC(C)C112p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (65200000.0, 's^-1', '*|/', 2.51189),
        n = 1,
        Ea = (13.0, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 14,
    label = "[CH2]CC(C)C!C13r1 <=> [CH2]C1CCC1C13p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31500000.0, 's^-1', '*|/', 2.51189),
        n = 1.08,
        Ea = (12.7, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 15,
    label = "[CH2]CCC(!C)C14r1 <=> [CH2]C1(C)CCC114p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6480000.0, 's^-1', '*|/', 2.51189),
        n = 1.25,
        Ea = (15, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 16,
    label = "[CH2]C(C)(C)CC!C15r1 <=> [CH2]C1CC(C)(C)C115p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6200000.0, 's^-1', '*|/', 2.51189),
        n = 1.3,
        Ea = (11.7, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 17,
    label = "[CH2]CC(C)(C)C!C16r1 <=> [CH2]C1CCC1(C)C16p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26000000.0, 's^-1', '*|/', 2.51189),
        n = 1.13,
        Ea = (12.4, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 18,
    label = "[CH2]CCC!C(C)C17r1 <=> C[C](C)C1CCC117p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (55300000.0, 's^-1', '*|/', 2.51189),
        n = 1.02,
        Ea = (13.5, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 19,
    label = "[CH2]CCCC!C18r1 <=> [CH2]C1CCCC118p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (698000.0, 's^-1', '*|/', 2.51189),
        n = 1.33,
        Ea = (4.7, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 20,
    label = "C!CCCC[CH]C19r1 <=> [CH2]C1CCCC1C19p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (187000.0, 's^-1', '*|/', 2.51189),
        n = 1.48,
        Ea = (3.9, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 21,
    label = "C!CCCC[C](C)C20r1 <=> [CH2]C1CCCC1(C)C20p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126000.0, 's^-1', '*|/', 2.51189),
        n = 1.48,
        Ea = (3.7, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 22,
    label = "[CH2]CCCC!CC21r1 <=> C[CH]C1CCCC121p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1720000.0, 's^-1', '*|/', 2.51189),
        n = 1.2,
        Ea = (4.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 23,
    label = "[CH2]CCCC(!C)C22r1 <=> [CH2]C1(C)CCCC122p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (184000.0, 's^-1', '*|/', 2.51189),
        n = 1.4,
        Ea = (6.2, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 24,
    label = "[CH2]C(C)CCC!C23r1 <=> [CH2]C1CCC(C)C123p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1250000.0, 's^-1', '*|/', 2.51189),
        n = 1.22,
        Ea = (3.7, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 25,
    label = "[CH2]CC(C)CC!C24r1 <=> [CH2]C1CCC(C)C124p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8070000.0, 's^-1', '*|/', 2.51189),
        n = 1.02,
        Ea = (3.9, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 26,
    label = "[CH2]CCC(C)C!C25r1 <=> [CH2]C1CCCC1C25p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6750000.0, 's^-1', '*|/', 2.51189),
        n = 1.04,
        Ea = (4.5, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 27,
    label = "[CH2]C(C)(C)CCC!C26r1 <=> [CH2]C1CCC(C)(C)C126p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7050000.0, 's^-1', '*|/', 2.51189),
        n = 1.03,
        Ea = (3.2, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 28,
    label = "[CH2]CC(C)(C)CC!C27r1 <=> [CH2]C1CCC(C)(C)C127p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33700000.0, 's^-1', '*|/', 2.51189),
        n = 0.85,
        Ea = (4.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 29,
    label = "[CH2]CCC(C)(C)C!C28r1 <=> [CH2]C1CCCC1(C)C28p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11800000.0, 's^-1', '*|/', 2.51189),
        n = 0.99,
        Ea = (4.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 30,
    label = "[CH2]CCCC!C(C)C29r1 <=> C[C](C)C1CCCC129p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20100000.0, 's^-1', '*|/', 2.51189),
        n = 0.9,
        Ea = (4.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 31,
    label = "[CH2]CCCCC!C30r1 <=> [CH2]C1CCCCC130p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (153000.0, 's^-1', '*|/', 2.51189),
        n = 1.26,
        Ea = (5.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 32,
    label = "C!CCCCC[CH]C31r1 <=> [CH2]C1CCCCC1C31p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18700.0, 's^-1', '*|/', 2.51189),
        n = 1.43,
        Ea = (4.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 33,
    label = "[CH2]C(C)(C)CCCC!C32r1 <=> [CH2]C1CCCC(C)(C)C132p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2020.0, 's^-1', '*|/', 2.51189),
        n = 1.67,
        Ea = (2.6, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 34,
    label = "[CH2]CCCCC!CC33r1 <=> C[CH]C1CCCCC133p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (414000.0, 's^-1', '*|/', 2.51189),
        n = 1.14,
        Ea = (5, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 35,
    label = "[CH2]CCCCC(!C)C34r1 <=> [CH2]C1(C)CCCCC134p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24600.0, 's^-1', '*|/', 2.51189),
        n = 1.32,
        Ea = (6.1, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)


entry(
    index = 36,
    label = "[CH2]CCCCC!C(C)C35r1 <=> C[C](C)C1CCCCC135p1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000.0, 's^-1', '*|/', 2.51189),
        n = 1.18,
        Ea = (4.3, 'kcal/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    reference = Article(
    authors = ["K. Wang", "S. Villano", "A. Dean"],
    title = u'Reactivity Structure Based Rate Estimation Rules for Alkyl Radical H-atom Shift and Alkenyl Radical Cycloaddition Reactions',
    journal = "J. Phys. Chem. A",
    volume = "119",
    pages = """7205-7221""",
    year = "2015",
),
    rank = 3,
    referenceType = "theory",
    shortDesc =u' CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)',
    longDesc = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)