/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | foam-extend: Open Source CFD                    |
|  \\    /   O peration     | Version:     4.1                                |
|   \\  /    A nd           | Web:         http://www.foam-extend.org         |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 26.157;

boundaryField
{
    inlet
    {
        type            supersonicInlet;
        value           uniform 26.157;
    }
    outlet1
    {
        type            zeroGradient;
    }
    outlet2
    {
        type            zeroGradient;
    }
    outlet3
    {
        type            zeroGradient;
    }
    wall1
    {
        type            diffusedWall;
        value           uniform 101325;
    }
    wall2
    {
        type            diffusedWall;
        value           uniform 101325;
    }
    defaultFaces
    {
        type            empty;
    }
}
