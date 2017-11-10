# coding=utf-8
# --------------------------------------------------------------------------
# A Capacitated Plant Location Model for Reverse Logistics Activities
#
# Authors: Alexsander Antunes, Americo Almeida, Pedro Chitarra, Tulio Araujo
# --------------------------------------------------------------------------

# ------------------------
# Importing libraries
# ------------------------
import sys
import os
import math
import numpy
import db
import random

# ------------------------
# CPLEX API
# ------------------------
import cplex

# -------------------------
# Plot The Given Solution
# -------------------------

class Solver(object):
    # -------------------------
    # Initialize Object
    # -------------------------
    def __init__(self, inputData):
        self.db = db.DB('database.sqlite')

        # Get data for the supply points, facilites and demand points
        self.varParameters = inputData
        self.supplyPoints  = self.db.get_cities_by_population_range(
            self.varParameters["stateId"], self.varParameters["supplyPopMin"], self.varParameters["supplyPopMax"])
        self.facilities    = self.db.get_cities_by_population_range(
            self.varParameters["stateId"], self.varParameters["facilityPopMin"], self.varParameters["facilityPopMax"])
        self.demandPoints  = self.db.get_cities_by_population_range(
            self.varParameters["stateId"], self.varParameters["demandPopMin"], self.varParameters["demandPopMax"])
        
        # Get count for supply points, demand points and facilities
        self.varParameters["i"] = len(self.supplyPoints)
        self.varParameters["j"] = len(self.demandPoints)
        self.varParameters["k"] = len(self.facilities)

        # Set the variables within the selected range for each point
        for supplyPoint in self.supplyPoints:
            supplyPoint["a"] = random.randint(self.varParameters["aMin"], self.varParameters["aMax"])
        
        for facility in self.facilities:
            facility["f"]  = random.uniform(self.varParameters["fMin"], self.varParameters["fMax"])
            facility["fm"] = random.uniform(self.varParameters["fmMin"], self.varParameters["fmMax"])
            facility["m"]  = random.randint(self.varParameters["mMin"], self.varParameters["mMax"])
        
        for demandPoint in self.demandPoints:
            demandPoint["b"] = random.randint(self.varParameters["bMin"], self.varParameters["bMax"])
        print(self.varParameters["i"])
        print(self.varParameters["j"])
        print(self.varParameters["k"])
    # -------------------------
    # Plot the Solution Data on Console
    # -------------------------
    def plot_sol(self):
        w = self.sol["w"]
        x = self.sol["x"]
        y = self.sol["y"]

        print("====================Solution====================")
        print("Facilities installed:", ", ".join(
            map(str, [self.facilities[k]["name"] for k in w])))
        print("================================================")
        print("Supply Points : Corresponding Facility")
        for (i, k) in x:
            print("{:s} : {:s}".format(self.supplyPoints[i]["name"], self.facilities[k]["name"]))
        print("================================================")
        print("Facility : Demand Point : Reprocessed Units Flow")
        totalUnitsReprocessed = 0  # Calculate the number of products remanufactered
        totalUnits = 0  # Calculate the total of units available
        for (k, j, flow) in y:
            print("{:s} : {:s} : {:22.2f}".format(
                self.facilities[k]["name"], self.demandPoints[j]["name"], flow))
            totalUnits += flow
        print("================================================")
        print("Demand Point : Average Cost per Unit")
        totalProductsCost = 0  # Calculate the total cost of products remanufactered
        totalOverflowCost = 0  # Calculate the cost due to overflow
        totalUnitsOverflow = 0  # Calculate the total overflow of units
        for j in range(self.varParameters["j"]):
            facilityUnits = [(k, flow) for (k, j2, flow) in y if j2 == j]
            cost = 0
            totalFlow = 0
            for link in facilityUnits:
                # Calculate the average cost per flow link
                supplyCosts = [self.varParameters["c0"][i][k] for (i, k) in x if k == link[0]]
                cost += ((sum(supplyCosts) / len(supplyCosts)) +
                        self.varParameters["cr"][link[0]][j]) * link[1]
                totalFlow += link[1]
            costPerUnit = cost / totalFlow
            totalProductsCost += cost
            totalUnitsOverflow += (totalFlow - self.demandPoints[j]["b"])
            overflowUnitsCost = (totalFlow - self.demandPoints[j]["b"]) * costPerUnit
            totalOverflowCost += overflowUnitsCost
            print("{:s} : {:>21s}".format(
                self.demandPoints[j]["name"], "${0:.2f}".format(costPerUnit)))
        print("================================================")
        totalFacilitiesCost = 0  # Calculate the total cost of facilities installed
        for k in w:
            totalFacilitiesCost += self.facilities[k]["f"]

        print("Total Facilities Cost : ${:.2f}".format(totalFacilitiesCost))
        print("================================================")

        print("Total Products Cost : ${:.2f}".format(totalProductsCost))
        print("================================================")

        totalCost = totalProductsCost + totalFacilitiesCost

        print("Total Units Overflow : {:.2f}".format(totalUnitsOverflow))
        print("================================================")

        print("Total Overflow Cost : ${:.2f}".format(totalOverflowCost))
        print("================================================")

        print("{:^48}".format("TOTAL COST : ${:.2f}".format(totalCost)))
        print("================================================")

    # -------------------------
    # Execute CPLEX for solution
    # -------------------------
    def exec_cplex(self):
        # Define number of nodes for supply points (I), facilities (K) and demand points (J)
        I = range(self.varParameters["i"])
        J = range(self.varParameters["j"])
        K = range(self.varParameters["k"])
        IK = [(i, k) for i in I for k in K]
        KJ = [(k, j) for k in K for j in J]

        # Calculate the costs and other restriction variables
        c0, cr    = self.calc_costs()                           # Transporting costs per unit
        f         = [self.facilities[k]["f"] for k in K]   # Fixed cost for facility instalation
        fm        = [self.facilities[k]["fm"] for k in K]  # Variable cost per unit of reprocessed product
        m         = [self.facilities[k]["m"] for k in K]   # Facility Capacity
        a         = [self.supplyPoints[i]["a"] for i in I] # Supply quantity
        b         = [self.demandPoints[j]["b"] for j in J] # Demand quantity
        nSupply   = self.varParameters["i"]                # Number of Supply Points
        nFacility = self.varParameters["k"]                # Number of Facilities
        nDemand   = self.varParameters["j"]                # Number of Demand Points

        # Instantiate the costs on the model data
        self.varParameters["c0"] = c0
        self.varParameters["cr"] = cr

        # Instantiate the cplex object
        cpx = cplex.Cplex()

        # Create indexes for the variables vector
        # Enumerate k indexes for variable W
        v_wi = {k: idx for idx, k in enumerate(K)}
        v_xi = {(i, k): idx + len(v_wi) for idx, (i, k) in enumerate(IK)
                }             # Enumerate ik indexes for variable X
        v_yi = {(k, j): idx + len(v_wi) + len(v_xi) for idx, (k, j)
                in enumerate(KJ)}  # Enumerate kj indexes for variable y

        # Create names for the variables
        v_wn = ["w(" + str(k) + ")" for k in K]
        v_xn = ["x(" + str(i) + "," + str(k) + ")" for (i, k) in IK]
        v_yn = ["y(" + str(k) + "," + str(j) + ")" for (k, j) in KJ]

        # Create the variable corresponding to Wk
        cpx.variables.add(obj=[f[k] for k in K],
                        lb=[0.0] * nFacility,
                        ub=[1.0] * nFacility,
                        types=['B'] * nFacility,
                        names=v_wn)

        # Create the variable corresponding to Xik
        cpx.variables.add(obj=[(c0[i][k] + fm[k]) * a[i] for (i, k) in IK],
                        lb=[0.0] * nSupply * nFacility,
                        ub=[1.0] * nSupply * nFacility,
                        types=['B'] * nSupply * nFacility,
                        names=v_xn)

        # Create the variable corresponding to Yik
        cpx.variables.add(obj=[cr[k][j] for (k, j) in KJ],
                        lb=[0.0] * nFacility * nDemand,
                        ub=[cplex.infinity] * nFacility * nDemand,
                        names=v_yn)

        # Add the constraints defined by the model
        [cpx.linear_constraints.add(lin_expr=[cplex.SparsePair(
                                    [v_xi[(i, k)] for i in I] + [v_wi[k]],
                                    [a[i] for i in I] + [-m[k]])],
                                    senses="L",
                                    rhs=[0.0]) for k in K]

        [cpx.linear_constraints.add(lin_expr=[cplex.SparsePair(
                                    [v_xi[(i, k)] for i in I] + [v_yi[(k, j)]
                                                                for j in J],
                                    [a[i] for i in I] + [-1.0 for j in J])],
                                    senses="E",
                                    rhs=[0.0]) for k in K]

        [cpx.linear_constraints.add(lin_expr=[cplex.SparsePair(
                                    [v_yi[(k, j)] for k in K],
                                    [1.0 for k in K])],
                                    senses="G",
                                    rhs=[b[j]]) for j in J]

        [cpx.linear_constraints.add(lin_expr=[cplex.SparsePair(
                                    [v_xi[(i, k)] for k in K],
                                    [1.0 for k in K])],
                                    senses="E",
                                    rhs=[1.0]) for i in I]

        cpx.write("trabalho2.lp")
        cpx.parameters.threads.set(1)
        cpx.solve()
        status = cpx.solution.get_status()
        statusMsg = cpx.solution.get_status_string()

        if (status != cpx.solution.status.optimal) and\
            (status != cpx.solution.status.optimal_tolerance) and\
            (status != cpx.solution.status.MIP_optimal) and\
            (status != cpx.solution.status.MIP_time_limit_feasible) and\
            (status != cpx.solution.status.MIP_dettime_limit_feasible) and\
            (status != cpx.solution.status.MIP_abort_feasible) and\
            (status != cpx.solution.status.MIP_feasible_relaxed_sum) and\
            (status != cpx.solution.status.MIP_feasible_relaxed_inf) and\
            (status != cpx.solution.status.MIP_optimal_relaxed_inf) and\
            (status != cpx.solution.status.MIP_feasible_relaxed_quad) and\
            (status != cpx.solution.status.MIP_optimal_relaxed_sum) and\
            (status != cpx.solution.status.MIP_feasible):

            statusMsg = cpx.solution.get_status_string()
            print(statusMsg)
            sys.exit(-1)
        else:
            of = cpx.solution.get_objective_value()
            x = cpx.solution.get_values()
            sol = {}
            sol["of"] = of
            sol["w"] = [k for k in K if x[v_wi[k]] > 0.9]
            sol["x"] = [(i, k) for (i, k) in IK if x[v_xi[(i, k)]] > 0.9]
            sol["y"] = [(k, j, x[v_yi[(k, j)]])
                        for (k, j) in KJ if x[v_yi[(k, j)]] > 0.001]

        self.sol = sol

    # -------------------------
    # Calculate Costs
    # -------------------------
    def calc_costs(self):
        I = range(self.varParameters["i"])
        J = range(self.varParameters["j"])
        K = range(self.varParameters["k"])
        c0 = [[0 for k in K] for i in I]
        cr = [[0 for j in J] for k in K]
        for i in I:
            for k in K:
                distance = self.db.get_distance(self.supplyPoints[i]["cityId"], self.facilities[k]["cityId"])
                c0[i][k] = distance * random.uniform(self.varParameters["c0Min"], self.varParameters["c0Max"])
        
        for k in K:
            for j in J:
                distance = self.db.get_distance(self.demandPoints[j]["cityId"], self.facilities[k]["cityId"])
                cr[k][j] = distance * random.uniform(self.varParameters["crMin"], self.varParameters["crMax"])
        return c0, cr