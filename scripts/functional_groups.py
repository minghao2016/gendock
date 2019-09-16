# all groups are listed as :
# "SMILES": mass,

# starting functional groups

s_dict = {
    "c1([*])c([**])cccc1": 77,
    "c1([*])cc([**])ccc1": 77,
    "c1([*])ccc([**])cc1": 77,
    "C1([*])=CC=C([**])C=C1([***])": 76,
    "C1([*])=CN=C([**])C=C1([***])": 77,
    "C1([*])=CN=C([**])N=C1([***])": 78,
    "c1([*])cccc2c([**])ccnc21": 127,
    "c1([*])c2c(cccc2)nc3ccccc31": 128,
    "C1([*])CCc2c1cccc2": 117,
    "C([*])(C1)Cc2c1cccc2": 117,
    "C([*])(CC1[**])c2c1cccc2": 117,
    "c1([*])c2c(cccc2)ccc1": 127,
    "c1([*])c2c(cccc2)ccc1[**]": 127,
    "c1([*])ccc2c(c1)cc([**])cc2": 127,
    "c1([*])cc2c(cccc2)cc1": 127,
    "N([*])C1=C(C(C2=C(C=C3)O)=O)C(C(C2=C3O)=O)=C(N[**])C=C1": 268,
    "O=C1C2=C(C([*])=NN2[**])N=C([***])N1": 136,
    "C1([*])=NC(C([**])=NN2[***])=C2C=N1": 120,
    "C1([*])=NC(C([**])=NN2[***])=C2C=C1": 119,
    "C1([*])=CC(C([**])=NN2[***])=C2C=C1": 118,
    "C1([*])=NC(C([**])=CN2[***])=C2C=C1": 118
}

# non-terminal groups

nt_dict = {
    "c1c([*])cccc1": 77,
    "c1cc([*])ccc1": 77,
    "c1ccc([*])cc1": 77,
    "OC([*])": 30,
    "C(=O)OC([*])": 44,
    "CC(=O)C([*])": 57,
    "C([*])": 14,
    "CS(=O)(=O)O([*])": 95,
    "C/C=C/[*]": 41,
    "CC#C[*]": 39,
    "CS([*])": 47,
    "CC(=O)N([*])": 58,
    "CN([*])": 30,
    "C1OC1[*]": 44,
    "C1SC1[*]": 56,
    "N=N[*]": 28,
    "C=N[*]": 26,
    "C(=O)OC(=O)[*]": 72,
    "CC[*]": 28,
    "N1CCN([*])CC1": 86
}

# terminal groups

t_dict = {
    "Br": 80,
    "Cl": 35.5,
    "F": 19,
    "C(=O)": 29,
    "O": 17,
    "CC#C": 40,
    "C#N": 26,
    "C(O)(=O)": 45,
    "[N+]([O-])(=O)": 46,
    "c1ccccc1": 77,
    "N1C=CC=C1": 66,
    "c1ccccn1": 78,
    "C1CCCCC1": 83,
    "C(N=[N+]=[N-])": 42,
    "[N]": 16,
    "C(Cl)(=O)": 62,
    "C(=O)C": 43,
    "S": 32,
    "N=C=O": 42,
    "C1=NC=CS1": 85,
    "N1C=NC=N1": 69,
    "c1ccccc1(Cl)": 112,
    "N1CCN(C)CC1": 102,
    "N1CCOCC1": 88,
    "c1cc(F)c(F)cc1(F)": 132,
    "CO": 31,
    "COC": 45,
    "C1CC(O)C(CO)C1": 116,
    "C1CC1": 9
}