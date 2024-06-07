import pandas as pd

# Define the grading function
def grade_apf_definition(content):
    content = content.lower()
    if "ratio of volume of atom" in content and "volume of unit cell" in content:
        return 3
    elif "ratio" in content and "volume of atom" in content:
        return 2
    elif "space occupied" in content or "total volume" in content:
        return 1
    else:
        return 0

# Load the dataset
data = {
    'Paper_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
    'Paper_content': [
        "APF is defined as the ratio of volume of atom in the unit cell to the volume of unit cell.",
        "APF is space occurwd by atoms in unit cell.",
        "the percentage of total space filled by particle is called packing fraction .the total number of atom that make struture",
        "effective number of atom are the total number of atoms that constitute to make a crystal solid",
        "atomic packing factor is the ratio of volume of atoms in aunit cell and volume of unit cell .",
        "APF is a factor that gives us the idea that hoe=w much the struture is filled in different crystalline struture",
        "APF stand for atomic packing fraction .it is defined as the total volume of unit cell to the unit cell.",
        "APF is atomic packing fraction is defined as the ratio of volume of atom or molecule of unit cell to the volume of unit cell",
        "APF refers to the space occupied by an atom of a unit cell in a crystal lattice",
        "it can be defined as the ability of crystal of having no. of atoms in it. Such as face centered . Body centered , simple cubic .",
        "atomic packing fraction pr APF is the volume or space acquired by the atoms present in one cubic cell with respect to the total space of cubic cell",
        "the no. of atoms present in per unit of space",
        "APF  is defined as the ratio of volume of the atoms in the crystal to the volume of crystal",
        "APF  refers to the  atomic packing fraction ehic means volume of atoms by volume of atomic lattice",
        "APF is that value when a atom is coverd in uts boby .",
        "APF is defined as the ratio of volume of atom divided by volume of cubic cell",
        "APF is space occurwd by atoms in unit cell.",
        "APF is defined as the ratio of volume occupied by the unit cell to the total volume",
        "it is the ratio of the volume of surface to the volume of cube",
        "APF is defined as the ratio of volume of effective atom to a unit cell. It is also known as relative density",
        "APF is a factor that gives us the idea that hoe=w much the struture is filled in different crystalline struture",
        "APF is equal to yhe volume of atoms in a unit cell divided by the volume of unit cell",
        "APF  is defined as the ratio of volume of the atoms in the crystal to the volume of crystal",
        "APF is the efficiancy of a lattice to the unit cell which is packed together with respect to the total volume of the crystal  lattice",
        "APF is nothing but the ratio of volume of atoms present in a unit cell to the total volume of unit cell",
        "it is defined as the way to find out how efficiently/closely atoms are packed together in a crystal lattice",
        "APF is the space accumulated by the atoms out of total space in lattice",
        "APF is a type of substance by which we can remove dislocated pairs of atoms while effetive number of atom can be defined as the dislocation of a single atom",
        "APF is the space occupied by the atoms out of total sphere",
        "APF stands for atomic packing fraction and is the ratio of the volume of effective number of atom to the volume of the unit cell",
        "it is nothing but the ratio of volume of atoms in aunit cell to the unit cell",
        "APF  refers to the  atomic packing fraction ehic means volume of atoms by volume of atomic lattice",
        "it is defined as the way to find out how efficiently/closely atoms are packed together in a crystal lattice",
        "it is defined as the space occupied by a group of atoms in a unit cell to the volume of unit cell",
        "APF  is defined as the ratio of volume of the atoms in the crystal to the volume of crystal",
        "APF is the ratio of the volume of all the atoms that are in the cubic centerd by the volume of the unit cell",
        "it is the  ratio of volume of atoms to the lattice",
        "the percentage of total space filled by particle is called packing fraction .the total number of atom that make struture",
        "APF stand for atomic packing fraction .it is defined as the total volume of unit cell to the unit cell.",
        "APF  refers to the  atomic packing fraction ehic means volume of atoms by volume of atomic lattice",
        "APF stand for atomic packing fraction .it is the percentage packing fraction in a crystalline structure",
        "APF  is defined as the ratio of volume of the atoms in the crystal to the volume of crystal",
        "it is defined as the ratio of volume of atom in unit cell to the volume of unit  cell",
        "APF is defined as the total no. of atoms present upon total volume of a unit cell",
        "it is atomic packing frequency and is defined by ratio of n. of unit cell to the total volume",
        "APF can be defined as the total no. of atoms present upon the total volume of unit cell",
        "it is the ratio of the volume of atom divoded by volue of unit cell",
        "APF is defined as the atomic packing fraction it is the percentage of the packing fraction of a cube lattice structure",
        "APF stand for atomic packing fraction .it is the percentage packing fraction in a crystalline structure",
        "it can be defined as the ability of crystal of having no. of atoms in it. Such as face centered . Body centered , simple cubic .",
        "APF is efficiency that is calculated by the formula for a cubic lattice which determines the overall packing efficiency os atoms in a space lattice of acube",
        "it is defined a the total volume of  the cubic structure with respect to the volume of cube"
    ],
    'Marks_obtained': [3, 2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 3, 2, 3, 1, 3, 3, 0, 2, 1, 1, 1, 3, 2, 3, 3, 2, 1, 3, 2, 2, 2, 3, 3, 1, 3, 1, 1, 2, 3, 3, 3, 3]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Apply the grading function
df['Automated_Marks'] = df['Paper_content'].apply(grade_apf_definition)

# Compare the automated marks with the original marks
df['Correctly_Graded'] = df['Marks_obtained'] == df['Automated_Marks']

# Display the DataFrame with the new columns
print(df)

# Save the DataFrame to a new CSV file
df.to_csv('graded_apf_data.csv', index=False)
