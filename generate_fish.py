from Geometry.auto_tendonFish import generate_xml, SYSTEMPARAMETERS

SYSTEMPARAMETERS["fluidCoef"] = [0.4, 7.79, 2.81, 3.84, 0.27]
generate_xml(SYSTEMPARAMETERS, "Geometry/exampleFish.xml")