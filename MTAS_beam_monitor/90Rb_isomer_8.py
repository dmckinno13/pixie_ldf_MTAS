# do not touch this part
INPUT = {}  # ne pas toucher

# stores the title information you wish displayed
INPUT["Title Name"] = "90Rb Isomeric State"
# stores the half life in seconds of the isotope in question
INPUT["Half Life"] = 258.0
# stores the cycle length in seconds
# this is: Collection time + 3*(move time) + measure time + laser time
INPUT["Cycle Length"] = (0.7 + 0.495 + 3.0 + (2.0 * 0.495) + 0.2)
# stores the collection time in seconds
INPUT["Collection Time"] = 0.7
# stores the rampdown time of the high voltage kicker, lets the script account
# for the fact that beam collection does not start at the beginning of the
# collection time but instead after the voltage has ramped down enough for the
# beam to hit the tape
INPUT["Voltage Rampdown Time"] = 0.002
# stores the time the HPGe spectrum was accumulating, in seconds
INPUT["HPGe Integration Time"] = 490.0
# stores the energies (in MeV) of the gammas of interest
INPUT["Gamma Energies"] = [0.82423, 0.83169, 1.06070, 1.66561, 2.1283, 2.7526, 3.3170, 4.13551, 4.36590]
# stores the intensities of the gammas of interest
# if the intensity is 2.56% give 0.0256
INPUT["Gamma Branchings"] = [0.087, 0.94, 0.076, 0.048, 0.052, 0.115, 0.143, 0.00110, 0.00106]
# stores the counts of the peaks of interest
INPUT["Gamma Areas"] = [129.0, 1424.0, 129.0, 49.0, 25.0, 75.0, 54.0, 6.0, 11.0]
# stores the parameters of the efficiency function
# the function is:
# eff(En) = (a0 + a1*x + a2*x^2 + a3*x^3 + a5*x^5 + a7*x^7)/(En)
# with x = Log_10(en) and En = (Gamma Energy in MeV)
# the format is: [a0, a1, a2, a3, a4, a5]
INPUT["HPGe Efficiency Function"] = [8.17090e-03, 1.84907e-03, -3.28729e-04,
                                     -7.60215e-04, 1.87004e-04, -1.16447e-05]
