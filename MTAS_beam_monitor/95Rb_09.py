# do not touch this part
INPUT = {}  # ne pas toucher

# stores the title information you wish displayed
INPUT["Title Name"] = "95Rb"
# stores the half life in seconds of the isotope in question
INPUT["Half Life"] = 0.3777
# stores the cycle length in seconds
# this is: Collection time + 3*(move time) + measure time + laser time
INPUT["Cycle Length"] = (0.7 + 0.495 + 1.4 + (1.0 * 0.495) + 0.2)
# stores the collection time in seconds
INPUT["Collection Time"] = 0.7
# stores the rampdown time of the high voltage kicker, lets the script account
# for the fact that beam collection does not start at the beginning of the
# collection time but instead after the voltage has ramped down enough for the
# beam to hit the tape
INPUT["Voltage Rampdown Time"] = 0.002
# stores the time the HPGe spectrum was accumulating, in seconds
INPUT["HPGe Integration Time"] = 730.0
# stores the energies (in MeV) of the gammas of interest
INPUT["Gamma Energies"] = [0.204, 0.3287, 0.35201, 0.6807, 0.769]
# stores the intensities of the gammas of interest
# if the intensity is 2.56% give 0.0256
INPUT["Gamma Branchings"] = [0.151844, 0.09367, 0.493, 0.149379, 0.04437]
# stores the counts of the peaks of interest
INPUT["Gamma Areas"] = [1549.0, 850.0, 3623.0, 630.0, 232.0]
# stores the parameters of the efficiency function
# the function is:
# eff(En) = (a0 + a1*x + a2*x^2 + a3*x^3 + a5*x^5 + a7*x^7)/(En)
# with x = Log_10(en) and En = (Gamma Energy in MeV)
# the format is: [a0, a1, a2, a3, a4, a5]
INPUT["HPGe Efficiency Function"] = [8.17090e-03, 1.84907e-03, -3.28729e-04,
                                     -7.60215e-04, 1.87004e-04, -1.16447e-05]
