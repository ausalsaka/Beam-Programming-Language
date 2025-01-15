# Quick Summary
 Run simulations of simple beams

 There is a description of the language inside the file "ReadMe.pdf"

 This language uses textx.
 The grammar for the language is defined in the file "Beam.tx"
 The interpreter is in "Beam.py"
 
 <br />
 
# *Beam* Programming Language:
The *Beam* programming language is aimed at structural engineers who commonly work with beams. *Beam* allows engineers to define a beam’s loading conditions to quickly run calculations to find commonly needed values such as support reaction forces and internal shear and bending moment.

At its current stage of development, *Beam* offers support for:
1.	Cantilever Beams
2.	Point loads at any angle
3.	Rectangular Distributed Loads
4.	Point Torques
5.	Finding Resultant Forces
6.	Finding Reaction Forces

<br />

## Sample Programs:

The following beam will be represented in *Beam*.
![SampleBeam1](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleBeam1.PNG)

![SampleProgram1](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleProgram1.PNG)

This sample program is for a cantilever beam with a 10kg point load at a location 10 meters from its support.

It outputs the following:
![SampleResults1](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleResults1.PNG)

<br />

### Here is another sample program:
The following beam will be represented in *Beam*.
![SampleBeam2](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleBeam2.PNG)

![SampleProgram2](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleProgram2.PNG)

This program is for a cantilever beam with a rectangular distributed load that starts at a distance 5 meters from the support and continues for another 5 meters. The load has a magnitude of 2 Newtons per meter (N/m) in the negative y direction.

It outputs the following:
![SampleResults2](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleResults2.PNG)

<br />

### Complex Sample Program:

The following complexly loaded beam will be represented in *Beam*.
![SampleBeam3](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleBeam3.PNG)

![SampleProgram3](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleProgram3.PNG)

Here is the output:

![SampleResults3](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/SampleResults3.PNG)

<br />

*Beam* was developed using python and the textX meta-language.

Here is the .tx file containing the grammar of *Beam*:

![Grammar](https://github.com/ausalsaka/Beam-Programming-Language/blob/77cf9d9efc6785f3d17e149fe3b439decaf5a9a9/images/Grammar.PNG)

Here is the .py file containing the interpreter of *Beam*:

![Interpreter](https://github.com/ausalsaka/Beam-Programming-Language/blob/f250bc45843e21aff2576ff92f27e30965f9dd20/images/Interpreter.png)
