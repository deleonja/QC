(* ::Package:: *)

(* ::Section:: *)
(*Component erasing maps package*)


(* ::Input::Initialization:: *)
(*Author: Jos\[EAcute] Alfredo de Le\[OAcute]n*)
(*Date: August 07, 2020*)
BeginPackage["quantumJA`"]

Reshuffle::usage=
"Reshuffle[SqMatrix] reshuffles the matrix SqMatrix."
Pauli::usage=
"Pauli[Indices_List] gives the tensor product of Pauli Matrices with indices in Indices_List."
PCE::usage=
"PCh[diagElements, qubitsNum] calculates the matrix representation of a map in the tensor product of Pauli matrices given the
diagonal elements of the matrix in computational basis."
CubePositions::usage=
"CubePositions[diagElPos] gives the positions of the painted cubes given the positions of the 1's in the diagonal of the quantum channel."
Cube3q::usage=
"Cube3q[pauliDiagonal] graphs the 3-qubit board given the indices of the painted cubes."
CPtest::usage=
"CPtest[points] returns True if CP, False if not."
PtestM::usage=
"Ptest[A] evaluates the positive-semidefiniteness of A using the principal minors criterion."
PTest::usage=
"PTest[A] evaluates the positive-semidefiniteness of A with its eigenvalues."
Dirac::usage=
"Dirac[vector] returns vector in Dirac notation in computational basis."
TwoQBoard::usage=
"TwoQBoard[diagonalPCE] returns a two qubits board."

Begin["`Private`"]
Reshuffle[SqMatrix_]:=1/Power[2,Log[4,Length[SqMatrix]]]*ArrayFlatten[ArrayFlatten/@Partition[Partition[ArrayReshape[#,{Sqrt[Dimensions[SqMatrix][[1]]],Sqrt[Dimensions[SqMatrix][[1]]]}]&/@SqMatrix,Sqrt[Dimensions[SqMatrix][[1]]]],Sqrt[Dimensions[SqMatrix][[1]]]],1];

Pauli[0]=Pauli[{0}]={{1,0},{0,1}};
Pauli[1]=Pauli[{1}]={{0,1},{1,0}};
Pauli[2]=Pauli[{2}]={{0,-I},{I,0}};
Pauli[3]=Pauli[{3}]={{1,0},{0,-1}};
Pauli[Indices_List]:=KroneckerProduct@@(Pauli/@Indices);

PCE[pauliDiagonal_List]:=Module[{indices,n,pauliToComp},
n=Log[4,Length[pauliDiagonal]];
indices=Tuples[Range[0,3],n];
pauliToComp=Transpose[Map[Flatten[Pauli[#]]&,indices]];
pauliToComp.DiagonalMatrix[pauliDiagonal].Inverse[pauliToComp]
]

CubePositions[diagElPos_]:=
Position[ArrayReshape[SparseArray[diagElPos->ConstantArray[1,Length[diagElPos]],{64}]//Normal,{4,4,4}],1]-1

Cube3q[pauliDiagonal_]:=Module[{cubeIndices},
cubeIndices=Position[ArrayReshape[pauliDiagonal,{4,4,4}],1]-1;
Graphics3D[{If[Count[#,0]==3,{Black,Cube[#]},
If[Count[#,0]==2,{RGBColor["#CC0000"],Cube[#]},
If[Count[#,0]==1,{RGBColor["#004C99"],Cube[#]},
If[Count[#,0]==0,{RGBColor["#99FF33"],Cube[#]}]]]]&/@cubeIndices,
{Thickness[0.012],Line[{{{-0.5,-0.5,-0.5},{-0.5,-0.5,3.5}},{{-0.5,-0.5,-0.5},{-0.5,3.5,-0.5}},{{-0.5,-0.5,-0.5},{3.5,-0.5,-0.5}},
{{3.5,-0.5,-0.5},{3.5,-0.5,3.5}},
{{-0.5,-0.5,3.5},{3.5,-0.5,3.5}},
{{-0.5,3.5,-0.5},{3.5,3.5,-0.5}},
{{3.5,3.5,-0.5},{3.5,3.5,3.5}},
{{3.5,3.5,3.5},{-0.5,3.5,3.5}},
{{-0.5,3.5,3.5},{-0.5,3.5,-0.5}},
{{-0.5,3.5,3.5},{-0.5,-0.5,3.5}},
{{3.5,3.5,3.5},{3.5,-0.5,3.5}},
{{3.5,3.5,-0.5},{3.5,-0.5,-0.5}}}]}},
Axes->False,AxesLabel->{"x","y","z"},LabelStyle->Directive[Bold,Medium,Black],PlotRange->{{-0.5,3.5},{-0.5,3.5},{-0.5,3.5}},AxesOrigin->{0.5,0.5,0.5},AxesStyle->Thickness[0.005],ImageSize->Medium,ImagePadding->45]
]

CPtest[points_]:=If[(PCE[SparseArray[points+1->ConstantArray[1,{points//Length}],{4,4,4}]//Normal//Flatten,3]//Reshuffle//Eigenvalues//Min)>=0,True,False]

PtestM[A_]:=AllTrue[(Diagonal[Map[Reverse,Minors[A,#],{0,1}]]&/@Range[Length[A]]),#>=0&,2]

PTest[A_]:=Min[Eigenvalues[A]]>=0

Dirac[vector_List]:=(vector[[#]]Ket[IntegerString[(#-1),2,Log[2,Length[vector]]]])&/@Delete[Range[Length[vector]],Position[vector,0]]//Total

TwoQBoard[diagonalPCE_List]:=ArrayPlot[SparseArray[Position[ArrayReshape[diagonalPCE,{4,4}],1]->(If[#[[1]]==1\[And]#[[2]]==1,Black,If[#[[1]]==1\[Or]#[[2]]==1,RGBColor["#CC0000"],If[#[[1]]!=1\[And]#[[2]]!=1,RGBColor["#004C99"],Nothing]]]&/@Position[ArrayReshape[diagonalPCE,{4,4}],1]),{4,4}]]
End[];
EndPackage[]


(* ::InheritFromParent:: *)
(*"PauliToComp[qbitsNum] calculates the change of basis matrix for a qubit-system map from computational to tensor product of Pauli matrices basis."*)
