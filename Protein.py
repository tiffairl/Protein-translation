"""Made to translate RNA sequences into proteins. There are 64 codons."""

PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    """Each codon translates to an amino acid."""
    protein_list = []

    for index in range(0, len(strand), 3):
        codon = strand[index:index + 3]
        protein = PROTEINS[codon]

        if protein == "STOP":
            break

        protein_list.append(protein)

    return protein_list