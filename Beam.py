from os.path import dirname, join
import numpy
import math

import textx;
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export

def load_model(code):
    metamodel = textx.metamodel_from_file('Beam.tx')
    return metamodel.model_from_file(code, )

# Define functions for beam calculations
def calculate_reaction_forces(model):
    # Placeholder function
    print("Calculating Resultant forces...")
    sigmaFx = 0.0
    sigmaFy = 0.0
    sigmaMoment = 0.0
    for load in model.loads:
        if load.__class__.__name__ == "PointLoad":
            magnitude = 0.0
            location = 0.0
            theta = 0.0
            for prop in load.properties:
                match prop.name:
                    case "Magnitude":
                        magnitude = prop.value
                    case "Location":
                        location = prop.value
                    case "Angle":
                        theta = prop.value
            Fx = magnitude * math.cos(math.radians(theta))
            Fy = magnitude * math.sin(math.radians(theta))
            moment = Fy * location
            sigmaFx = sigmaFx + Fx
            sigmaFy = sigmaFy + Fy
            sigmaMoment = sigmaMoment + moment
        if load.__class__.__name__ == "Torque":
            magnitude = 0.0
            location = 0.0
            for prop in load.properties:
                match prop.name:
                    case "Magnitude":
                        magnitude = prop.value
                    case "Location":
                        location = prop.value
            sigmaFy = sigmaFy + magnitude/location
        if load.__class__.__name__ == "DistributedLoad":
            length = 0.0
            height = 0.0
            location = 0.0
            for prop in load.properties:
                match prop.name:
                    case "Magnitude":
                        height = prop.value
                    case "Length":
                        length = prop.value
                    case "Location":
                        location = prop.value
            F_Ry = length * height
            moment = F_Ry * (location + length/2)
            sigmaFy += F_Ry
            sigmaMoment += moment

    print(f"Resultant Forces: F_Rx= {round(sigmaFx,2)}N  F_Ry= {round(sigmaFy,2)}N  Moment= {round(sigmaMoment,2)}N*m\n")
    
    print("Calculating Resultant forces...")
    F_Ox = -sigmaFx
    F_Oy = -sigmaFy
    M_O = -sigmaMoment

    print(f"Reaction Forces: F_Ox= {round(F_Ox,2)}N  F_Oy= {round(F_Oy,2)}N  M_O= {round(M_O,2)}N*m")    

    
    

def calculate_shear_force(model, position):
    # Placeholder function
    print(f"Calculating shear force at position {position}...")

def calculate_bending_moment(model, position):
    # Placeholder function
    print(f"Calculating bending moment at position {position}...")



def main(debug=False):

    this_folder = dirname(__file__)

    model = metamodel_from_file(join(this_folder, 'Beam.tx'), debug=False)
    metamodel_export(model, join(this_folder, 'beam.dot'))

    beam_model = model.model_from_file(join(this_folder, 'code.beam'))
    model_export(beam_model, join(this_folder, 'program.dot'))

    # Parse the code and perform beam calculations
    model = load_model('code.beam')
    calculate_reaction_forces(model)
    # calculate_shear_force(model, 2.5)         <--to be implemented
    # calculate_bending_moment(model, 2.5)      <--


if __name__ == "__main__":
    main()
