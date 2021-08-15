from player import Player
import numpy as np
from config import CONFIG
import copy
import random
import time


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):
        for count in range(len(child.nn.wMatrice)):
            child.nn.wMatrice[count] += np.random.normal(0, 0.8, child.nn.wMatrice[count].shape)
            child.nn.bVector[count] += np.random.normal(0, 0.8, child.nn.bVector[count].shape)
        return child

    def generate_new_population(self, num_players, prev_players=None):
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]
        else:
            new_players = []
            sumFitness = sum(player.fitness for player in prev_players)
            weights = [player.fitness / sumFitness for player in prev_players]
            selectedParents = random.choices(prev_players, weights=weights, k=num_players)
            childs = [copy.deepcopy(parent) for parent in selectedParents]
            for childIndex in range(0, len(childs), 2):
                if random.uniform(0, 1) >= 0.4:
                    tempVector = childs[childIndex].nn.bVector
                    childs[childIndex].nn.bVector = childs[childIndex + 1].nn.bVector
                    childs[childIndex + 1].nn.bVector = tempVector

                if random.uniform(0, 1) >= 0.2:
                    childs[childIndex] = self.mutate(childs[childIndex])
                new_players.append(childs[childIndex])
                
                if random.uniform(0, 1) >= 0.2:
                    childs[childIndex + 1] = self.mutate(childs[childIndex + 1])
                new_players.append(childs[childIndex + 1])

            # TODO (additional): a selection method other than fitness proportionate
            return new_players

    def next_population_selection(self, players, num_players):
        players.sort(reverse=True, key=lambda x: x.fitness)
        minFitness = players[len(players) - 1].fitness
        maxFitness = players[0].fitness
        sumFitness = sum(player.fitness for player in players)
        meanFitness = sumFitness / len(players)
        generationReport = open("generation-" + self.mode + ".txt", "a")
        generationReport.write(str(minFitness) + "," + str(maxFitness) + "," + str(meanFitness) + "\n")
        generationReport.close()

        weights = [player.fitness / sumFitness for player in players]
        
        return list(np.random.choice(players, num_players, p=weights, replace=False))
