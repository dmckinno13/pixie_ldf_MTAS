# do not touch this part
INPUT = {}  # ne pas toucher

# stores the title information you wish displayed
INPUT["Title Name"] = "96Y Ground State"
# stores the half life in seconds of the isotope in question
INPUT["Half Life"] = 9.6
# stores the cycle length in seconds
# this is: Collection time + 3*(move time) + measure time + laser time
COLLECTION_TIME = 
TRANSPORT_TIME = 
MTAS_MEASURE_TIME = 
LASER_TIME = 
INPUT["Cycle Length"] = (COLLECTION_TIME + TRANSPORT_TIME + MTAS_MEASURE_TIME + TRANSPORT_TIME + LASER_TIME)
# stores the collection time in seconds
INPUT["Collection Time"] = COLLECTION_TIME
# stores the rampdown time of the high voltage kicker, lets the script account
# for the fact that beam collection does not start at the beginning of the
# collection time but instead after the voltage has ramped down enough for the
# beam to hit the tape
INPUT["Voltage Rampdown Time"] = 0.002
# stores the time the HPGe spectrum was accumulating, in seconds
INPUT["HPGe Integration Time"] = 
# stores the energies (in MeV) of the gammas of interest
INPUT["Gamma Energies"] = [0.146653, 0.3631, 0.6172, 0.63145, 0.9062, 0.9148, 1.1072, 1.2229, 1.7506]
# stores the intensities of the gammas of interest
# if the intensity is 2.56% give 0.0256
INPUT["Gamma Branchings"] = [0.3406, 0.22528, 0.55, 0.748, 0.2024, 0.5896, 0.48136, 0.26752, 0.88]
# stores the counts of the peaks of interest
INPUT["Gamma Areas"] = []
# stores the parameters of the efficiency function
# the function is:
# eff(En) = (a0 + a1*x + a2*x^2 + a3*x^3 + a5*x^5 + a7*x^7)/(En)
# with x = Log_10(en) and En = (Gamma Energy in MeV)
# the format is: [a0, a1, a2, a3, a4, a5]
INPUT["HPGe Efficiency Function"] = [8.17090e-03, 1.84907e-03, -3.28729e-04,
                                     -7.60215e-04, 1.87004e-04, -1.16447e-05]
