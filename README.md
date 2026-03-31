# TD PHYLOGENY

Understanding the molecular evolution of a virus, its genetic diversity, and how it spreads is crucial for controlling outbreaks and designing effective public health strategies and vaccines. One of the most powerful tools in viral genomics and epidemiology is the ability to build phylogenetic trees that illustrate the evolutionary relationships between different strains of a virus based on genetic data.
In this exercise, you will be working with genomics sequences from a virus retrieved from GenBank. Your task is to:

- Align the sequences: You will start by aligning these genomic sequences to identify similarities and differences in the viral genomes.


- Build a phylogenetic tree: Once the sequences are aligned, you will use computational tools to construct a phylogenetic tree, which will reveal how these different virus strains are related to each other. This tree will help us understand the virus’s genetic diversity and how different strains may have evolved over time.


- Visualize the tree: The final step is to visualize the phylogenetic tree and interpret the relationships between strains. This will allow you to identify patterns in the virus’s evolution, such as which strains may have emerged in different geographical regions or times, and how they may have spread.

## Select a dataset

Dataset available :
- chikv    

- mumps          
       
- west-nile-virus  

- zika_virus

- measles  

- yellow-fever

## Dataset visualisation

Questions : 


1) Look at the metadata. Do you think we will cover enough diversity for a phylogenetic tree ?


2) Use bioawk (or another tool), estimate the length of your virus genome. Looking at the data, is there a genome which will have a lot of gaps in the alignment ?	

Tools available :

bioawk : apt install bioawk

any document visualisation : bloc-notes, notepad++ etc


## Align the data

For this exercise, we will use a global aligner to align the data.

3) Can you briefly explain how your alignment tool works?

4) Which options did you use with your tool and why? If you use any options please develop.

5) What is the alignment length? Here, the length of the alignment is the number of total columns (= positions) present in your alignments.

6) Are there regions with many gaps? Should these regions be kept? Why?

Note: Even if you suggest removing a region, we will not do so for the rest of the analysis. The phylogenetic tool will automatically discard regions with too many gaps.

Tools available :

MAFFT : https://mafft.cbrc.jp/alignment/server/index.html

CLUSTAL : https://www.genome.jp/tools-bin/clustalw

MUSCLE : https://www.ebi.ac.uk/jdispatcher/msa/muscle

## Make a phylogenetic tree

Now that your sequences are aligned, build a phylogenetic tree using any tools of your choice. Don't forget to include boostrap options !

7) Which tool did you use and why ?

8) What model did you or the tool selected ? And why ?

9) What is the final likelihood of your tree? How many iterations did it take for the tree to converge?

Tools available :

PhyML : http://www.atgc-montpellier.fr/phyml/

RAxML : https://antonellilab.github.io/raxmlGUI/

IQ-TREE : http://iqtree.cibiv.univie.ac.at/


If you use PhyML, your input should be in .PHYLIP format. From MAFFT, you can easily convert your fasta into PHYLIP format using the buttom "REFORMAT" and then select PHYLIP format.


## Visualize the phylogenetic tree

Now that your tree is built, it’s time to visualize it. Upload the tree to:
 https://itol.embl.de/
iTOL is a visualization tool for phylogenetic trees. Explore different display options: dendrogram, circular tree, etc.

10) You didn’t define an outgroup during tree construction. Looking at the tree, can you identify a potential outgroup for rooting?

11) Display the unrooted tree and include bootstrap values. Add a caption that helps interpret the tree. Bonus points for clear layout and visible bootstrap support.

12) Try rooting your tree in iTOL. Choose an outgroup or use midpoint rooting. Explain your choice.
To root, click a node → "Tree structure" → "Re-root the tree here" or “Root the tree at the midpoint”.

You can color some nodes and branches by clicking on a node, select “Colored ranges”, then “Create a new range”. After selecting your color and a name, it will open a small pop-up window called “Colored ranges”, where you can change the cover.

13) Color two multifurcating nodes (nodes with more than two branches). Plot the tree here, and describe the two nodes. Are the samples close genetically? Does the metadata support this clustering?

 ## Annotation

The metadata includes information like sampling country and authorship. You can annotate the tree in iTOL to improve interpretation. Annotations can be added manually (by clicking on nodes) or in batch using uploaded metadata files.

Templates are available here: https://itol.embl.de/help.cgi#annot

Example annotation file to label countries:

Here is the example of a text file to add a country label in the phylogenetic tree for the sample 1_0081_PF and 1_0087_PF.

——————————————————————————————————
```
DATASET_TEXT
#SEPARATOR TAB
#SEPARATOR SPACE
SEPARATOR COMMA

#label is used in the legend table (can be changed later)
DATASET_LABEL,Country

#dataset color (can be changed later)
COLOR,#ff0000
#=================================================================#
#   	Actual data follows after the "DATA" keyword          	#
#=================================================================#
#the following fields are possible for each node:
#ID,label,position,color,style,size_factor,rotation

#position defines the position of the text label on the tree:
#  -1 = external label
#  a number between 0 and 1 = internal label positioned at the specified value along the node branch (for example, position 0 is exactly at the start of node branch, position 0.5 is in the middle, and position 1 is at the end)
#style can be 'normal',''bold','italic' or 'bold-italic'
#size factor will be multiplied with the standard font size

DATA
1_0087_PF,Oceania,-1,#000000,normal,1,0
1_0181_PF,Oceania,-1,#000000,normal,1,0
```
———————————————————————————————————

(Note: iTOL doesn't support spaces in sample names. Replace spaces with underscores in your Newick file before uploading. Colors use hexadecimal codes, e.g., #000000 for black.)

You will obtain something like this.


<img width="835" height="70" alt="annotation" src="https://github.com/user-attachments/assets/2cac2a44-e7f5-4529-9145-db284a5b13ac" />

## Overall evalutation 

14) Present your dataset, your method to build the phylogenetic tree. What do you think ? Did you choose the good method ?

15) What do you think of the diversity of your viruse ? Is your dataset enough to represent the overall diversity ?

16) If you had more time, what else would you explore?

17) You can compare your tree with the one that contains all of your data at https://nextstrain.org/

